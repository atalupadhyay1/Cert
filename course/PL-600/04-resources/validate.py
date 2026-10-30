#!/usr/bin/env python3
"""Comprehensive validator and blueprint/alignment report generator for Microsoft Exam PL-600."""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

from bank import (
    ALLOCATIONS,
    BANK,
    CASES,
    CASE_SIZE,
    CASE_STUDIES,
    CERTIFICATION_URL,
    CODE_FILL_FLOOR,
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    EXAM_URL,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PREREQUISITES,
    PROPOSED_SOL_FLOOR,
    RETIREMENT_DATE,
    RETIREMENT_URL,
    SKILLS,
    SKILL_PLAN,
    SKILL_SOURCES,
    STUDY_GUIDE_DATE,
    STUDY_GUIDE_URL,
    SUBTITLES,
    SUCCESSOR_EXAM,
    SUCCESSOR_URL,
    TERMS,
)
from build import HEADER

ROOT = Path(__file__).resolve().parent.parent
SETS_DIR = ROOT / '03-practice-sets'
SAMPLE_CSV = ROOT / '05-sample-upload' / 'case-study-sample.csv'
REPORT_PATH = ROOT / '02-curriculum' / 'blueprint-alignment.md'

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
)

MS_BANNED_COMPANIES = (
    'contoso',
    'fabrikam',
    'adventureworks',
    'adventure works',
    'tailspin',
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
    'baldwin museum',
    'trey research',
    'lucerne publishing',
    'consolidated messenger',
    'alpine ski house',
    'vanarsdel',
    'relecloud',
    'munson',
)

STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'have',
    'in', 'into', 'is', 'it', 'its', 'must', 'of', 'on', 'or', 'that', 'the', 'their',
    'this', 'to', 'using', 'via', 'wants', 'when', 'which', 'with', 'you', 'your',
    'select', 'two', 'three', 'what', 'should', 'recommend', 'need', 'needs', 'company',
    'power', 'platform', 'microsoft', 'dataverse', 'solution', 'architect', 'environment',
    'case', 'study', 'proposed', 'meet', 'goal', 'does',
}


def _tokens(text: str) -> set[str]:
    words = re.findall(r'[a-z0-9_]+', text.lower())
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


def _validate_csv_file(path: Path, expected_rows: int, errors: list[str]) -> list[list[str]]:
    if not path.is_file():
        errors.append(f'Missing CSV file: {path}')
        return []
    raw = path.read_text(encoding='utf-8')
    if '\r' in raw:
        errors.append(f'{path.name}: contains CR line endings')
    rows = list(csv.reader(raw.splitlines()))
    if not rows:
        errors.append(f'{path.name}: empty CSV')
        return []
    if rows[0] != HEADER:
        errors.append(f'{path.name}: header mismatch')
    body = rows[1:]
    if len(body) != expected_rows:
        errors.append(f'{path.name}: expected {expected_rows} data rows, got {len(body)}')
    for idx, row in enumerate(body, start=2):
        if len(row) != 17:
            errors.append(f'{path.name}:{idx}: expected 17 columns, got {len(row)}')
            continue
        stem, qtype = row[0], row[1]
        opts = [row[2 * i] for i in range(1, 7)]
        exps = [row[2 * i + 1] for i in range(1, 7)]
        corr, overall, dom = row[14], row[15], row[16]
        if not stem.strip():
            errors.append(f'{path.name}:{idx}: blank Question')
        if qtype not in ('multiple-choice', 'multi-select'):
            errors.append(f'{path.name}:{idx}: invalid Question Type {qtype!r}')
        non_empty = [i for i, o in enumerate(opts, start=1) if o.strip()]
        if non_empty != list(range(1, len(non_empty) + 1)) or len(non_empty) < 4:
            errors.append(f'{path.name}:{idx}: non-contiguous or <4 options: {non_empty}')
        for i in range(1, 7):
            if bool(opts[i - 1].strip()) != bool(exps[i - 1].strip()):
                errors.append(f'{path.name}:{idx}: option/explanation {i} presence mismatch')
        try:
            c_idx = [int(x) for x in corr.split(',')]
        except ValueError:
            errors.append(f'{path.name}:{idx}: invalid Correct Answers {corr!r}')
            c_idx = []
        if c_idx != sorted(set(c_idx)) or any(c < 1 or c > len(non_empty) for c in c_idx):
            errors.append(f'{path.name}:{idx}: unsorted, out-of-range, or duplicate Correct Answers {corr!r}')
        if qtype == 'multiple-choice' and len(c_idx) != 1:
            errors.append(f'{path.name}:{idx}: multiple-choice requires 1 answer, got {corr!r}')
        if qtype == 'multi-select' and len(c_idx) < 2:
            errors.append(f'{path.name}:{idx}: multi-select requires >=2 answers, got {corr!r}')
        if not overall.strip() or 'learn.microsoft.com' not in overall:
            errors.append(f'{path.name}:{idx}: missing Microsoft Learn citation in Overall Explanation')
        if dom not in DOMAINS.values():
            errors.append(f'{path.name}:{idx}: unknown Domain {dom!r}')
        joined = ' '.join(row).lower()
        for phrase in BANNED_PHRASES:
            if phrase in joined:
                errors.append(f'{path.name}:{idx}: contains banned phrase {phrase!r}')
        for comp in MS_BANNED_COMPANIES:
            if comp in joined:
                errors.append(f'{path.name}:{idx}: contains Microsoft fictional company {comp!r}')
    return body


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
        std_body = _validate_csv_file(sdir / f'practice-set-{set_num}.csv', ITEM_TOTAL, errors)
        emb_body = _validate_csv_file(sdir / f'case-embedded-set-{set_num}.csv', ITEM_TOTAL, errors)
        for extra in (sdir / f'practice-set-{set_num}-review.md', sdir / 'README.md'):
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

        code_fills = sum(1 for it in items if '____' in it['question'])
        prop_sols = sum(1 for it in items if 'Proposed solution:' in it['question'])
        case_items = sum(1 for it in items if it['question'].startswith('Case study \u2014 '))
        if code_fills < CODE_FILL_FLOOR:
            errors.append(f'Set {set_num}: code/expression completions {code_fills} < {CODE_FILL_FLOOR}')
        if prop_sols < PROPOSED_SOL_FLOOR:
            errors.append(f'Set {set_num}: Proposed solution items {prop_sols} < {PROPOSED_SOL_FLOOR}')
        if case_items != CASE_STUDIES * CASE_SIZE:
            errors.append(f'Set {set_num}: case study items {case_items} != {CASE_STUDIES * CASE_SIZE}')

        mc_pos = Counter()
        for row in std_body:
            if row[1] == 'multiple-choice':
                mc_pos[int(row[14])] += 1
        if dict(mc_pos) != {1: 21, 2: 21, 3: 21, 4: 21}:
            errors.append(f'Set {set_num}: MC answer slots {dict(mc_pos)} != 21/21/21/21')

        for std_r, emb_r in zip(std_body, emb_body):
            if std_r[1:] != emb_r[1:]:
                errors.append(f'Set {set_num}: standard vs embedded mismatch outside column 1')

        stats['sets'][set_num] = {
            'domains': dict(doms),
            'kinds': dict(kinds),
            'ms_domains': dict(ms_doms),
            'code_fills': code_fills,
            'prop_sols': prop_sols,
            'case_items': case_items,
            'mc_pos': dict(mc_pos),
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
            body_text = re.sub(r'^Case study \u2014 [^:]+:\s*', '', it['question'])
            token_cache.append((it['id'], _tokens(body_text)))

    _validate_csv_file(SAMPLE_CSV, 12, errors)

    unused = sorted(set(TERMS) - set(used_terms))
    if unused:
        errors.append(f'Unused TERMS keys ({len(unused)}): {unused[:10]}')

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


def write_report(stats: dict) -> None:
    lines = [
        f'# {EXAM_CODE}: {EXAM_TITLE} — Blueprint Alignment Report',
        '',
        '## Official Exam & Lifecycle Metadata',
        '',
        f'- **Exam:** `{EXAM_CODE}: {EXAM_TITLE}`',
        f'- **Credential:** `{CREDENTIAL_TITLE}`',
        f'- **Mandatory Prerequisite:** {PREREQUISITES}',
        f'- **Final Official Study Guide Revision:** `{STUDY_GUIDE_DATE}` ({STUDY_GUIDE_URL})',
        f'- **Lifecycle & Retirement Notice:** Exam `{EXAM_CODE}` and `{CREDENTIAL_TITLE}` retired on **`{RETIREMENT_DATE}`** ({RETIREMENT_URL}). Microsoft introduced **`{SUCCESSOR_EXAM}`** ({SUCCESSOR_URL}) as the successor AI-first Business Applications architect certification.',
        f'- **Certification Overview:** {CERTIFICATION_URL}',
        f'- **Exam Overview:** {EXAM_URL}',
        f'- **Course Bank Volume:** `6 practice exams x 100 questions = {stats["total_questions"]} unique questions` (`0` duplicate stems, `0` duplicate explanations)',
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
        '| Set | Focus | Single (`S`) | Sequence (`O`) | Multi-2 (`M2`) | Multi-3 (`M3`) | `____` Completions | `Proposed solution:` | Case Items (`4x3`) | MC Key Pos `1/2/3/4` |',
        '| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |',
    ])
    for n in range(1, 7):
        s = stats['sets'][n]
        pos = s['mc_pos']
        pos_str = f"{pos.get(1,0)}/{pos.get(2,0)}/{pos.get(3,0)}/{pos.get(4,0)}"
        lines.append(
            f"| {n} | {SUBTITLES[n]} | {s['kinds']['S']} | {s['kinds']['O']} | "
            f"{s['kinds']['M2']} | {s['kinds']['M3']} | {s['code_fills']} | "
            f"{s['prop_sols']} | {s['case_items']} | `{pos_str}` |"
        )

    lines.extend([
        '',
        '## Granular Skill Coverage Across All 43 Official September 23, 2024 Study-Guide Skills',
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

    lines.extend([
        '',
        '## Original Multi-Question Case Studies (24 Case Studies = 72 Case Items)',
        '',
        '| Set | Case Study 1 | Case Study 2 | Case Study 3 | Case Study 4 |',
        '| :---: | :--- | :--- | :--- | :--- |',
    ])
    for n in range(1, 7):
        names = list(CASES[n].keys())
        lines.append(f'| **Set {n}** | {names[0]} (`3 Qs`) | {names[1]} (`3 Qs`) | {names[2]} (`3 Qs`) | {names[3]} (`3 Qs`) |')

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true', help='Write 02-curriculum/blueprint-alignment.md')
    args = parser.parse_args()

    errors, stats = validate_all()
    if errors:
        print(f'VALIDATION FAILED with {len(errors)} error(s):', file=sys.stderr)
        for err in errors[:50]:
            print(f'  - {err}', file=sys.stderr)
        return 1

    if args.report:
        write_report(stats)
        print(f'Wrote {REPORT_PATH}')

    print(
        f"OK: {EXAM_CODE} validated — {stats['total_questions']} unique questions across 6 sets, "
        f"{stats['terms_used']}/{stats['terms_total']} terms used, max Jaccard {stats['max_jaccard']:.3f}"
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
