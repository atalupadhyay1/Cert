#!/usr/bin/env python3
"""Offline export checks, not independent factual or difficulty certification."""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from build import ROOT,HEADER,DOMAINS,GUIDE,make_rows

def normalize(text):
    return re.sub(r'\W+',' ',text.casefold()).strip()

def validate_rows(rows,expected=None):
    errors=[]
    if len(rows)!=100: errors.append(f'Expected 100 rows, found {len(rows)}')
    if any(r.get('Domain') not in DOMAINS.values() for r in rows):
        errors.append('Unknown official domain label')
    if expected is not None and Counter(r.get('Domain') for r in rows)!=Counter(r.get('Domain') for r in expected):
        errors.append('Domain counts differ from topical source')
    if Counter(r.get('Question Type') for r in rows)!=Counter({'multiple-choice':100}):
        errors.append('Expected 100 single-answer multiple-choice questions')
    seen=set()
    positions=Counter()
    for n,row in enumerate(rows,1):
        tag=f'Question {n}'
        if set(row)!=set(HEADER): errors.append(f'{tag}: unexpected or missing columns')
        question=normalize(row.get('Question',''))
        if not question or question in seen: errors.append(f'{tag}: empty or duplicate question')
        seen.add(question)
        options=[row.get(f'Answer Option {i}','').strip() for i in range(1,7)]
        if any(not x for x in options[:4]) or any(options[4:]):
            errors.append(f'{tag}: expected four contiguous options')
        if len({x.casefold() for x in options[:4]})!=4:
            errors.append(f'{tag}: duplicate options')
        for i in range(1,7):
            if bool(options[i-1])!=bool(row.get(f'Explanation {i}','').strip()):
                errors.append(f'{tag}: option/explanation mismatch at {i}')
        answer=row.get('Correct Answers','')
        if not re.fullmatch('[1-4]',answer): errors.append(f'{tag}: invalid correct-answer index')
        else: positions[int(answer)]+=1
        overall=row.get('Overall Explanation','')
        if GUIDE not in overall:
            errors.append(f'{tag}: missing official CCAO-F exam-guide reference')
        if expected is not None and n<=len(expected) and row!=expected[n-1]:
            errors.append(f'{tag}: differs from authored source/build output')
    if positions!=Counter({1:25,2:25,3:25,4:25}):
        errors.append('Single-answer slots are not balanced at 25 each')
    return errors

def validate_files(paths):
    failures,summaries,all_questions=[],[],[]
    for path in paths:
        match=re.fullmatch(r'practice-set-([1-6])\.csv',path.name)
        number=int(match[1]) if match else None
        with path.open(encoding='utf-8-sig',newline='') as f:
            reader=csv.DictReader(f)
            header=reader.fieldnames
            rows=list(reader)
        errors=[] if header==HEADER else ['CSV header/order differs from 17-column template']
        errors.extend(validate_rows(rows,make_rows(number)[0] if number else None))
        failures.extend(f'{path.name}: {e}' for e in errors)
        all_questions.extend(normalize(r.get('Question','')) for r in rows)
        summaries.append(dict(file=str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            questions=len(rows),status='FAIL' if errors else 'PASS',
            types=dict(Counter(r.get('Question Type') for r in rows)),
            domains=dict(Counter(r.get('Domain') for r in rows))))
    if len(set(all_questions))!=len(all_questions):
        failures.append('Duplicate normalized question wording across supplied files')
    return failures,summaries

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files',nargs='*',type=Path)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args()
    paths=args.files or sorted((ROOT/'03-practice-sets').glob('set-*/practice-set-*.csv'))
    if not paths: parser.error('No CSV files found')
    failures,summaries=validate_files(paths)
    if not args.files and len(paths)!=6: failures.append('Expected six CSV files')
    report=dict(status='FAIL' if failures else 'PASS',sets=len(paths),
        total_questions=sum(x['questions'] for x in summaries),
        checks=['17-column header','100 questions per set','topical-source domain counts',
                'four unique options','single-answer keys','per-option explanations',
                'CCAO-F exam-guide references','source consistency','normalized duplicate wording',
                '25 correct answers per slot'],
        limitations=['No independent factual certification','No difficulty calibration against real exam',
                     'No exhaustive semantic duplicate detection','No Udemy account import performed',
                     'No continuous live URL verification'],files=summaries,errors=failures)
    if args.report: args.report.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    for entry in summaries: print(f"{entry['status']}: {entry['file']} — {entry['questions']} questions")
    if failures:
        for failure in failures: print('ERROR:',failure)
        raise SystemExit(1)
    print(f"PASS: {report['sets']} sets / {report['total_questions']} questions")

if __name__=='__main__': main()
