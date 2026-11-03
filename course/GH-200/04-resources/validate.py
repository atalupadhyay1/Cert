#!/usr/bin/env python3
"""Comprehensive validator and blueprint alignment report generator for Microsoft / GitHub Exam GH-200."""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from bank import (  # noqa: E402
    ALLOCATIONS,
    BANK,
    COMPLETION_FLOOR,
    DOMAINS,
    EXAM_CODE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    SKILLS,
    SKILL_PLAN,
    STUDY_GUIDE_DATE,
    SUBTITLES,
    TERMS,
)
from build import ALLOWED_TYPES, EXPORT_PLAN, HEADER  # noqa: E402

ROOT = HERE.parent
SETS_DIR = ROOT / '03-practice-sets'
SAMPLE_CSV = ROOT / '05-sample-upload' / 'sample-upload.csv'
BLUEPRINT_MD = ROOT / '02-curriculum' / 'blueprint-alignment.md'
SUMMARY_MD = HERE / 'SUMMARY.md'
REPORT_JSON = HERE / 'validation-report.json'

SIBLING_COURSES = (
    'PL-900', 'PL-200', 'PL-400', 'PL-500', 'PL-600',
    'AZ-204', 'AZ-400', 'AZ-401',
    'DP-300', 'DP-600', 'DP-900',
    'GH-900', 'GH-100',
)

BANNED_PHRASES = (
    'all of the above',
    'none of the above',
    'both a and b',
    'true or false',
    'lorem ipsum',
    'dummy',
    'todo',
    'tbd',
    'placeholder',
    'drag ',
    'drop ',
    'click ',
    'yes / no',
    'sample question',
    'case study —',
)

MS_GH_BANNED_COMPANIES = (
    'contoso',
    'fabrikam',
    'adventureworks',
    'adventure works',
    'tailspin',
    'tailwind traders',
    'northwind',
    'wide world importers',
    'fourth coffee',
    'litware',
    'woodgrove',
    'proseware',
    'adatum',
    'margie',
    'wingtip',
    'humongous insurance',
    'coho vineyard',
    'coho winery',
    'baldwin museum',
    'trey research',
    'lucerne publishing',
    'consolidated messenger',
    'alpine ski house',
    'vanarsdel',
    'relecloud',
    'munson',
    'lamna',
    'octoacme',
    'octodemo',
    'mona ',
)

STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'have',
    'in', 'into', 'is', 'it', 'its', 'must', 'of', 'on', 'or', 'that', 'the', 'their',
    'this', 'to', 'using', 'via', 'wants', 'when', 'which', 'with', 'you', 'your',
    'select', 'two', 'three', 'what', 'should', 'recommend', 'need', 'needs', 'company',
    'github', 'actions', 'workflow', 'workflows', 'repository', 'team', 'engineer', 'organization',
    'proposed', 'solution', 'meet', 'goal', 'does', 'how', 'job', 'step', 'run',
}


def _tokens(text: str) -> set[str]:
    words = re.findall(r'[a-z0-9_]+', text.lower())
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


def validate_csv_file(path: Path, expected_rows: int, check_balance: bool, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f'Missing CSV file: {path}')
        return {}
    raw = path.read_bytes()
    if not raw.startswith(b'\xef\xbb\xbf'):
        errors.append(f'{path.name}: missing UTF-8 BOM')
    if b'\r\n' in raw or b'\r' in raw:
        errors.append(f'{path.name}: contains CR/CRLF line endings; expected LF')

    with path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            errors.append(f'{path.name}: header mismatch {reader.fieldnames}')
            return {}
        rows = list(reader)
    if len(rows) != expected_rows:
        errors.append(f'{path.name}: expected {expected_rows} rows, got {len(rows)}')

    dom_counts = Counter()
    type_counts = Counter()
    slot_counts = Counter()
    valid_domains = set(DOMAINS.values())

    for idx, row in enumerate(rows, start=1):
        q = row['Question']
        qtype = row['Question Type']
        dom = row['Domain']
        overall = row['Overall Explanation']
        if qtype not in ALLOWED_TYPES:
            errors.append(f'{path.name} Q{idx}: invalid Question Type {qtype!r}')
        type_counts[qtype] += 1
        if dom not in valid_domains:
            errors.append(f'{path.name} Q{idx}: invalid Domain {dom!r}')
        dom_counts[dom] += 1
        if not q.strip() or len(q) > 995:
            errors.append(f'{path.name} Q{idx}: Question length {len(q)} outside 1..995')
        if not overall.strip() or len(overall) > 1400 or 'https://learn.microsoft.com/' not in overall:
            errors.append(f'{path.name} Q{idx}: Overall Explanation missing Microsoft Learn URL or >1400 chars')

        opts, exps = [], []
        seen_empty = False
        for slot in range(1, 7):
            opt = row[f'Answer Option {slot}']
            exp = row[f'Explanation {slot}']
            if opt:
                if seen_empty:
                    errors.append(f'{path.name} Q{idx}: non-contiguous Answer Option at slot {slot}')
                opts.append(opt)
                if not exp:
                    errors.append(f'{path.name} Q{idx}: missing Explanation {slot}')
                if len(opt) > 260:
                    errors.append(f'{path.name} Q{idx}: Option {slot} length {len(opt)} > 260')
                if len(exp) > 580:
                    errors.append(f'{path.name} Q{idx}: Explanation {slot} length {len(exp)} > 580')
                exps.append(exp)
            else:
                seen_empty = True
                if exp:
                    errors.append(f'{path.name} Q{idx}: Explanation {slot} populated for empty option')

        lowered = [o.casefold() for o in opts]
        if len(lowered) != len(set(lowered)):
            errors.append(f'{path.name} Q{idx}: duplicate option labels within row')

        try:
            ans_nums = [int(x) for x in row['Correct Answers'].split(',')]
        except ValueError:
            errors.append(f'{path.name} Q{idx}: invalid Correct Answers {row["Correct Answers"]!r}')
            continue
        if ans_nums != sorted(set(ans_nums)) or any(a < 1 or a > len(opts) for a in ans_nums):
            errors.append(f'{path.name} Q{idx}: unsorted, duplicate, or out-of-range Correct Answers {ans_nums}')
        if qtype == 'multiple-choice':
            if len(opts) != 4 or len(ans_nums) != 1:
                errors.append(f'{path.name} Q{idx}: multiple-choice requires 4 options and 1 answer')
            else:
                slot_counts[ans_nums[0]] += 1
        elif qtype == 'multi-select':
            if len(opts) not in (5, 6) or len(ans_nums) not in (2, 3):
                errors.append(f'{path.name} Q{idx}: multi-select requires 5-6 options and 2-3 answers')

        haystack = ' '.join([q, overall] + opts + exps).casefold()
        for phrase in BANNED_PHRASES:
            if phrase in haystack:
                errors.append(f'{path.name} Q{idx}: contains banned phrase {phrase!r}')
        for comp in MS_GH_BANNED_COMPANIES:
            if comp in haystack:
                errors.append(f'{path.name} Q{idx}: contains banned sample company {comp!r}')

    if check_balance:
        expected_domains = {DOMAINS[d]: cnt for d, cnt in ALLOCATIONS[1].items()}
        if dict(dom_counts) != expected_domains:
            errors.append(f'{path.name}: domain mismatch {dict(dom_counts)} vs {expected_domains}')
        if dict(type_counts) != EXPORT_PLAN:
            errors.append(f'{path.name}: type mix mismatch {dict(type_counts)} vs {EXPORT_PLAN}')
        if dict(slot_counts) != {1: 21, 2: 21, 3: 21, 4: 21}:
            errors.append(f'{path.name}: MC answer slots {dict(slot_counts)} != 21/21/21/21')

    return {
        'file': path.relative_to(ROOT).as_posix(),
        'rows': len(rows),
        'mc_slots': dict(slot_counts),
        'max_question_chars': max((len(r['Question']) for r in rows), default=0),
        'max_option_chars': max(
            (len(r[f'Answer Option {s}']) for r in rows for s in range(1, 7) if r[f'Answer Option {s}']),
            default=0,
        ),
        'max_overall_chars': max((len(r['Overall Explanation']) for r in rows), default=0),
    }


def validate_all() -> tuple[list[str], dict]:
    errors: list[str] = []
    stats: dict = {'sets': {}, 'max_jaccard': 0.0, 'max_pair': ('', '')}

    all_stems = {}
    all_reasons = {}
    used_terms = Counter()
    token_cache = []

    for set_num in range(1, 7):
        items = BANK[set_num]
        if len(items) != ITEM_TOTAL:
            errors.append(f'Set {set_num}: expected {ITEM_TOTAL} items, got {len(items)}')
            continue
        sdir = SETS_DIR / f'set-{set_num}'
        csv_stats = validate_csv_file(sdir / f'practice-set-{set_num}.csv', ITEM_TOTAL, True, errors)
        for extra in (sdir / f'practice-set-{set_num}.md', sdir / 'README.md'):
            if not extra.is_file():
                errors.append(f'Missing file: {extra}')

        kinds = Counter(it['kind'] for it in items)
        if dict(kinds) != KIND_PLAN:
            errors.append(f'Set {set_num}: kinds {dict(kinds)} != {KIND_PLAN}')
        doms = Counter(it['domain'] for it in items)
        if dict(doms) != ALLOCATIONS[set_num]:
            errors.append(f'Set {set_num}: domains {dict(doms)} != {ALLOCATIONS[set_num]}')
        for d, cnt in doms.items():
            lo, hi = OFFICIAL_RANGES[d]
            if not (lo <= cnt <= hi):
                errors.append(f'Set {set_num}: domain {d} count {cnt} outside official {lo}-{hi}%')
        ms_doms = Counter(it['domain'] for it in items if it['kind'] in ('M2', 'M3'))
        if dict(ms_doms) != MULTI_PLAN:
            errors.append(f'Set {set_num}: multi-select domain split {dict(ms_doms)} != {MULTI_PLAN}')
        skills = Counter(it['task'] for it in items)
        if dict(skills) != SKILL_PLAN:
            errors.append(f'Set {set_num}: skill counts mismatch SKILL_PLAN')

        completions = sum(1 for it in items if '____' in it['question'])
        prop_sols = sum(1 for it in items if 'Proposed solution:' in it['question'])
        if completions < COMPLETION_FLOOR:
            errors.append(f'Set {set_num}: completions {completions} < {COMPLETION_FLOOR}')
        if prop_sols < PROPOSED_SOL_FLOOR:
            errors.append(f'Set {set_num}: Proposed solution items {prop_sols} < {PROPOSED_SOL_FLOOR}')

        stats['sets'][set_num] = {
            'domains': dict(doms),
            'kinds': dict(kinds),
            'ms_domains': dict(ms_doms),
            'completions': completions,
            'prop_sols': prop_sols,
            'mc_pos': csv_stats.get('mc_slots', {}),
            'max_q_chars': csv_stats.get('max_question_chars', 0),
        }

        for it in items:
            norm_q = re.sub(r'\s+', ' ', it['question'].strip().lower())
            norm_r = re.sub(r'\s+', ' ', it['reason'].strip().lower())
            if norm_q in all_stems:
                errors.append(f'Duplicate stem between {all_stems[norm_q]} and {it["id"]}')
            all_stems[norm_q] = it['id']
            if norm_r in all_reasons:
                errors.append(f'Duplicate reason between {all_reasons[norm_r]} and {it["id"]}')
            all_reasons[norm_r] = it['id']
            if 'case study' in norm_q:
                errors.append(f'{it["id"]}: artificial case study prohibited on GH-200')
            for k in it['keys']:
                used_terms[k] += 1
            token_cache.append((it['id'], _tokens(it['question'])))

    validate_csv_file(SAMPLE_CSV, 15, False, errors)

    # Cross-course stem check across all 13 sibling Microsoft / GitHub 6x100 courses
    courses_dir = ROOT.parent
    for sib in SIBLING_COURSES:
        sib_dir = courses_dir / sib / '03-practice-sets'
        if not sib_dir.is_dir():
            continue
        for cpath in sorted(sib_dir.glob('set-*/practice-set-*.csv')):
            with cpath.open('r', encoding='utf-8-sig', newline='') as f:
                for row in csv.DictReader(f):
                    nq = re.sub(r'\s+', ' ', row['Question'].strip().lower())
                    if nq in all_stems:
                        errors.append(f'Cross-course stem collision with {sib}/{cpath.name}: {all_stems[nq]}')

    unused = sorted(set(TERMS) - set(used_terms))
    if unused:
        errors.append(f'{len(unused)} unused TERMS keys: {unused[:15]}')

    max_j = 0.0
    max_pair = ('', '')
    for i in range(len(token_cache)):
        id_a, tok_a = token_cache[i]
        if not tok_a:
            continue
        for j in range(i + 1, len(token_cache)):
            id_b, tok_b = token_cache[j]
            inter = len(tok_a & tok_b)
            if not inter:
                continue
            jac = inter / len(tok_a | tok_b)
            if jac > max_j:
                max_j = jac
                max_pair = (id_a, id_b)
            if jac > 0.72:
                errors.append(f'Stem Jaccard {jac:.3f} > 0.72 between {id_a} and {id_b}')

    stats['total_questions'] = len(all_stems)
    stats['terms_used'] = len(used_terms)
    stats['terms_total'] = len(TERMS)
    stats['unused_terms'] = unused
    stats['max_jaccard'] = round(max_j, 4)
    stats['max_pair'] = list(max_pair)
    return errors, stats


def write_reports(stats: dict) -> None:
    BLUEPRINT_MD.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f'# Official Exam {EXAM_CODE} Blueprint Alignment & Telemetry (`{STUDY_GUIDE_DATE}`)',
        '',
        '| Domain # | Official Functional Group | Published Weight | Items / Set | Multi-Select / Set | 6-Set Total |',
        '| :---: | :--- | :---: | :---: | :---: | :---: |',
    ]
    for d, name in DOMAINS.items():
        lo, hi = OFFICIAL_RANGES[d]
        cnt = ALLOCATIONS[1][d]
        ms = MULTI_PLAN[d]
        lines.append(f'| `{d}` | **{name}** | `{lo}–{hi}%` | `{cnt}` (`{cnt}%`) | `{ms}` | `{cnt * 6}` |')
    lines += [
        f'| **Total** | **All 5 Functional Groups · {len(SKILLS)} Official Skills** | **100%** | **100** | **16** | **600** |',
        '',
        '## Per-Set Telemetry',
        '',
        '| Set | Theme | MC (`S`+`O`) | MS (`M2`+`M3`) | `____` Fills | `Proposed solution:` | Case Items | Max Q Chars |',
        '| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |',
    ]
    for s in range(1, 7):
        st = stats['sets'][s]
        lines.append(
            f'| `{s}` | {SUBTITLES[s]} | `84` (`21/21/21/21`) | `16` | `{st["completions"]}` | `{st["prop_sols"]}` | `0` | `{st["max_q_chars"]}` |'
        )
    lines += [
        '',
        '## Bank-Wide Uniqueness & Term Coverage',
        '',
        f'- **Total authored questions:** `{stats["total_questions"]}` (`0` duplicate stems, `0` duplicate rationales, `0` artificial case studies)',
        f'- **Canonical `TERMS` exercised:** `{stats["terms_used"]} / {stats["terms_total"]}` (`100.0%`)',
        f'- **Max pairwise stem Jaccard similarity:** `{stats["max_jaccard"]}` (`{stats["max_pair"][0]}` vs `{stats["max_pair"][1]}`, ceiling `<= 0.72`)',
        '',
    ]
    md = '\n'.join(lines)
    BLUEPRINT_MD.write_text(md, encoding='utf-8')
    SUMMARY_MD.write_text(md, encoding='utf-8')
    REPORT_JSON.write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {BLUEPRINT_MD}, {SUMMARY_MD}, and {REPORT_JSON}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true', help='Write SUMMARY.md, blueprint-alignment.md, and validation-report.json')
    args = parser.parse_args()
    errors, stats = validate_all()
    if errors:
        for e in errors[:40]:
            print(f'ERROR: {e}', file=sys.stderr)
        if len(errors) > 40:
            print(f'... and {len(errors) - 40} more errors', file=sys.stderr)
        sys.exit(1)
    if args.report:
        write_reports(stats)
    print(
        f'OK: {EXAM_CODE} validated — {stats["total_questions"]} unique questions across 6 sets, '
        f'{stats["terms_used"]}/{stats["terms_total"]} terms used, max Jaccard {stats["max_jaccard"]}'
    )


if __name__ == '__main__':
    main()
