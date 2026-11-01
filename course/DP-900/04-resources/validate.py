#!/usr/bin/env python3
"""Comprehensive validator and blueprint alignment report generator for Microsoft Exam DP-900."""
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
    CERTIFICATION_URL,
    COMPLETION_FLOOR,
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    EXAM_URL,
    EXPIRATION_POLICY_URL,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PREREQUISITES,
    PROPOSED_SOL_FLOOR,
    SKILLS,
    SKILL_PLAN,
    SKILL_SOURCES,
    STUDY_GUIDE_DATE,
    STUDY_GUIDE_URL,
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

MS_BANNED_COMPANIES = (
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
)

STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'have',
    'in', 'into', 'is', 'it', 'its', 'must', 'of', 'on', 'or', 'that', 'the', 'their',
    'this', 'to', 'using', 'via', 'wants', 'when', 'which', 'with', 'you', 'your',
    'select', 'two', 'three', 'what', 'should', 'recommend', 'need', 'needs', 'company',
    'azure', 'data', 'microsoft', 'database', 'service', 'storage', 'proposed', 'solution',
    'meet', 'goal', 'does', 'team',
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
                if len(exp) > 560:
                    errors.append(f'{path.name} Q{idx}: Explanation {slot} length {len(exp)} > 560')
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
        for comp in MS_BANNED_COMPANIES:
            if comp in haystack:
                errors.append(f'{path.name} Q{idx}: contains Microsoft fictional company {comp!r}')

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
                errors.append(f'Duplicate overall reason between {all_reasons[norm_r]} and {it["id"]}')
            all_reasons[norm_r] = it['id']
            for k in it['keys']:
                used_terms[k] += 1
            token_cache.append((it['id'], _tokens(it['question'])))

    validate_csv_file(SAMPLE_CSV, 12, False, errors)

    unused = sorted(set(TERMS) - set(used_terms))
    if unused:
        errors.append(f'Unused TERMS keys ({len(unused)}): {unused[:15]}')

    for i in range(len(token_cache)):
        id_a, tok_a = token_cache[i]
        for j in range(i + 1, len(token_cache)):
            id_b, tok_b = token_cache[j]
            union = len(tok_a | tok_b)
            if not union:
                continue
            jac = len(tok_a & tok_b) / union
            if jac > stats['max_jaccard']:
                stats['max_jaccard'] = jac
                stats['max_pair'] = (id_a, id_b)
            if jac >= 0.72:
                errors.append(f'High stem similarity ({jac:.2f}) between {id_a} and {id_b}')

    stats['total_questions'] = len(all_stems)
    stats['terms_used'] = len(used_terms)
    stats['terms_total'] = len(TERMS)
    return errors, stats


def write_reports(stats: dict) -> None:
    lines = [
        f'# {EXAM_CODE}: {EXAM_TITLE} — Blueprint Alignment Report',
        '',
        '## Official Exam & Fundamentals Credential Metadata',
        '',
        f'- **Exam:** `{EXAM_CODE}: {EXAM_TITLE}` *(Active — Retirement date: none)*',
        f'- **Credential:** `{CREDENTIAL_TITLE}`',
        f'- **Prerequisite & Expiration Policy:** {PREREQUISITES} ({EXPIRATION_POLICY_URL})',
        f'- **Current Official Study Guide Baseline:** `{STUDY_GUIDE_DATE}` ({STUDY_GUIDE_URL})',
        f'- **Certification Overview:** {CERTIFICATION_URL}',
        f'- **Exam Overview:** {EXAM_URL}',
        f'- **Live Fundamentals Exam Format:** `45 minutes` exam time (`~65 minutes` seat duration), `40–60` standalone questions, `700 / 1000` scaled pass, `$99 USD` (US), **closed-book** (no split-screen Microsoft Learn access), **0 case studies**, **0 live labs**',
        f'- **Course Bank Volume:** `6 practice exams x 100 questions = {stats["total_questions"]} unique questions` (`0` duplicate stems, `0` duplicate explanations, `0` artificial case studies)',
        f'- **Option Library Coverage:** `{stats["terms_used"]} / {stats["terms_total"]}` canonical terms exercised (`100.0%`), max pairwise stem Jaccard similarity `{stats["max_jaccard"]:.3f}` (`{stats["max_pair"][0]}` vs `{stats["max_pair"][1]}`)',
        '',
        '## Domain Weighting Verification (Every Practice Set = 100 Questions)',
        '',
        '| Domain | Official Weight | Target / Set | Set 1 | Set 2 | Set 3 | Set 4 | Set 5 | Set 6 | Total (600) |',
        '| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |',
    ]
    for d, name in DOMAINS.items():
        lo, hi = OFFICIAL_RANGES[d]
        c = [stats['sets'][n]['domains'][d] for n in range(1, 7)]
        lines.append(
            f'| **Domain {d}:** {name} | {lo}–{hi}% | {ALLOCATIONS[1][d]}% | '
            + ' | '.join(str(x) for x in c)
            + f' | **{sum(c)}** ({sum(c)/6:.1f}%) |'
        )
    lines.append('| **Total** | **100%** | **100** | **100** | **100** | **100** | **100** | **100** | **100** | **600** |')
    lines.extend([
        '',
        '## Question-Format & Pattern Telemetry Across Practice Sets',
        '',
        '| Set | Focus | Single (`S`) | Sequence (`O`) | Multi-2 (`M2`) | Multi-3 (`M3`) | `____` Completions | `Proposed solution:` | Max Q Chars | MC Key Pos `1/2/3/4` |',
        '| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |',
    ])
    for n in range(1, 7):
        s = stats['sets'][n]
        pos = s['mc_pos']
        pos_str = f"{pos.get(1,0)}/{pos.get(2,0)}/{pos.get(3,0)}/{pos.get(4,0)}"
        lines.append(
            f"| {n} | {SUBTITLES[n]} | {s['kinds']['S']} | {s['kinds']['O']} | "
            f"{s['kinds']['M2']} | {s['kinds']['M3']} | {s['completions']} | "
            f"{s['prop_sols']} | {s['max_q_chars']} | `{pos_str}` |"
        )

    lines.extend([
        '',
        '## Granular Skill Coverage Across All 30 Official July 21, 2026 Study-Guide Skills',
        '',
        '| Skill ID | Domain | Official Skill Measured | Per Set | 6-Set Total | Primary Microsoft Learn Reference |',
        '| :---: | :---: | :--- | :---: | :---: | :--- |',
    ])
    for skill_id, skill_name in SKILLS.items():
        d = int(skill_id.split('.')[0])
        per_set = SKILL_PLAN[skill_id]
        src_title, src_url = SKILL_SOURCES[skill_id]
        lines.append(
            f'| `{skill_id}` | D{d} | {skill_name} | {per_set} | {per_set * 6} | [{src_title}]({src_url}) |'
        )

    report_text = '\n'.join(lines) + '\n'
    BLUEPRINT_MD.parent.mkdir(parents=True, exist_ok=True)
    BLUEPRINT_MD.write_text(report_text, encoding='utf-8')
    SUMMARY_MD.write_text(report_text, encoding='utf-8')
    REPORT_JSON.write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true', help='Write blueprint-alignment.md, SUMMARY.md, and validation-report.json')
    args = parser.parse_args()

    errors, stats = validate_all()
    if errors:
        print(f'VALIDATION FAILED with {len(errors)} error(s):', file=sys.stderr)
        for err in errors[:50]:
            print(f'  - {err}', file=sys.stderr)
        return 1

    if args.report:
        write_reports(stats)
        print(f'Wrote {BLUEPRINT_MD}, {SUMMARY_MD}, and {REPORT_JSON}')

    print(
        f"OK: {EXAM_CODE} validated — {stats['total_questions']} unique questions across 6 sets, "
        f"{stats['terms_used']}/{stats['terms_total']} terms used, max Jaccard {stats['max_jaccard']:.3f}"
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
