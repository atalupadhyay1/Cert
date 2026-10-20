#!/usr/bin/env python3
"""Build six deterministic CSVs and readable practice tests; Python stdlib only."""
import csv
import json
import random
from collections import Counter
from pathlib import Path
from bank import ITEMS, TERMS, OVERRIDES

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    1: 'Fundamentals of AI and ML',
    2: 'Fundamentals of GenAI',
    3: 'Applications of Foundation Models',
    4: 'Guidelines for Responsible AI',
    5: 'Security, Compliance, and Governance for AI Solutions',
}
WEIGHTS = {1: 20, 2: 24, 3: 28, 4: 14, 5: 14}
GUIDE = 'https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/'
HEADER = ['Question', 'Question Type']
for i in range(1, 7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']

# Direct AWS reading links complement the exam-domain source on every item.
READINGS = {
    'textract': 'https://docs.aws.amazon.com/textract/latest/dg/what-is.html',
    'rekognition': 'https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html',
    'transcribe': 'https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html',
    'polly': 'https://docs.aws.amazon.com/polly/latest/dg/what-is.html',
    'translate': 'https://docs.aws.amazon.com/translate/latest/dg/what-is.html',
    'comprehend': 'https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html',
    'groundtruth': 'https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html',
    'bedrock': 'https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html',
    'qbusiness': 'https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html',
    'qdeveloper': 'https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html',
    'kb': 'https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html',
    'rag': 'https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html',
    'agent': 'https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html',
    'guardrails': 'https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html',
    'clarify': 'https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html',
    'modelcard': 'https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html',
    'iam': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html',
    'kms': 'https://docs.aws.amazon.com/kms/latest/developerguide/overview.html',
    'cloudtrail': 'https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html',
    'cloudwatch': 'https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html',
    'macie': 'https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html',
    'artifact': 'https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html',
    'privatelink': 'https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html',
    'shared': 'https://aws.amazon.com/compliance/shared-responsibility-model/',
    'least': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html',
}

def is_multi(record):
    return record['reason'].startswith('Select TWO.')

def make_rows(set_number):
    rng = random.Random(41001 + set_number)
    records = list(enumerate(ITEMS, 1))
    rng.shuffle(records)
    # Balance single-answer positions explicitly instead of relying on chance.
    positions = [i % 4 for i in range(90)]
    rng.shuffle(positions)
    rows, mapping = [], []
    for objective, record in records:
        record = OVERRIDES.get((set_number, objective), record)
        keys = record['keys'][:]
        multi = is_multi(record)
        correct = set(keys[:2] if multi else keys[:1])
        if multi:
            rng.shuffle(keys)
        else:
            answer = keys.pop(0)
            rng.shuffle(keys)
            keys.insert(positions.pop(), answer)
        row = dict.fromkeys(HEADER, '')
        row['Question'] = record['prompts'][set_number - 1]
        row['Question Type'] = 'multi-select' if multi else 'multiple-choice'
        for i, key in enumerate(keys, 1):
            label, meaning = TERMS[key]
            status = 'Correct' if key in correct else 'Incorrect for this question'
            row[f'Answer Option {i}'] = label
            row[f'Explanation {i}'] = f'{status}. {label}: {meaning}'
        row['Correct Answers'] = ','.join(str(i) for i, key in enumerate(keys, 1) if key in correct)
        labels = '; '.join(TERMS[k][0] for k in record['keys'] if k in correct)
        reason = record['reason'].removeprefix('Select TWO. ')
        source = GUIDE + f"ai-practitioner-01-domain{record['domain']}.html"
        reading = record.get('ref') or READINGS.get(record['keys'][0])
        references = source + (f' Further reading: {reading}' if reading else '')
        row['Overall Explanation'] = f'Answer: {labels}. {reason} Reference: {references}'
        row['Domain'] = DOMAINS[record['domain']]
        rows.append(row)
        mapping.append({'question': len(rows), 'objective': objective, 'domain': record['domain'],
                        'correct_terms': sorted(correct), 'option_terms': keys})
    return rows, mapping

def render_test(number, rows):
    lines = [f'# AIF-C01 — Practice Set {number}', '',
             '100 questions · Suggested time: 140 minutes · Practice target: 80%', '',
             'Select one answer unless the question says Select TWO. Answers and explanations follow all questions.', '',
             'These are original learning questions, not actual AWS exam questions.', '', '## Questions', '']
    for n, row in enumerate(rows, 1):
        lines += [f"### {n}. {row['Question']}", '', f"Domain: {row['Domain']}", '']
        for i in range(1, 7):
            if row[f'Answer Option {i}']:
                lines.append(f"- {chr(64+i)}. {row[f'Answer Option {i}']}")
        lines.append('')
    lines += ['---', '', '## Answer key and explanations', '']
    for n, row in enumerate(rows, 1):
        letters = ', '.join(chr(64 + int(i)) for i in row['Correct Answers'].split(','))
        lines += [f'### Question {n} — {letters}', '', row['Overall Explanation'], '']
        for i in range(1, 7):
            if row[f'Explanation {i}']:
                lines.append(f"- **{chr(64+i)}:** {row[f'Explanation {i}']}")
        lines.append('')
    return '\n'.join(lines)

def main():
    if len(ITEMS) != 100 or Counter(i['domain'] for i in ITEMS) != Counter(WEIGHTS):
        raise ValueError('Expected 100 objectives in the 20/24/28/14/14 distribution')
    all_prompts = []
    for item in [*ITEMS, *OVERRIDES.values()]:
        if len(item['prompts']) != 6:
            raise ValueError('Every objective requires six prompts')
        expected_options = 5 if is_multi(item) else 4
        if len(item['keys']) != expected_options or len(set(item['keys'])) != expected_options:
            raise ValueError(f"Invalid options: {item['keys']}")
        for key in item['keys']:
            if key not in TERMS:
                raise ValueError(f'Undefined term: {key}')
        if item in ITEMS:
            all_prompts.extend(p.casefold().strip() for p in item['prompts'])
    if len(set(all_prompts)) != 600:
        raise ValueError('Duplicate question wording found')
    manifest = {}
    for number in range(1, 7):
        rows, mapping = make_rows(number)
        folder = ROOT / '03-practice-sets' / f'set-{number}'
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / f'practice-set-{number}.csv').open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(rows)
        (folder / f'practice-set-{number}.md').write_text(render_test(number, rows), encoding='utf-8')
        (folder / 'README.md').write_text(
            f'# Practice Set {number}\n\n100 questions: 90 single-answer + 10 select-two.\n\n'
            '| Domain | Questions |\n|---|---:|\n' +
            '\n'.join(f'| {DOMAINS[d]} | {n} |' for d, n in WEIGHTS.items()) +
            f'\n\nUpload `practice-set-{number}.csv`; use `practice-set-{number}.md` for offline review.\n'
            '\nSuggested custom practice duration: 140 minutes. Practice target: 80%; not an AWS scaled score.\n'
            '\nCore objectives recur across sets with differently worded scenarios; these are not independent psychometric exam forms.\n',
            encoding='utf-8')
        manifest[str(number)] = mapping
        print(f'Built set {number}: {len(rows)} questions')
    (ROOT / '04-resources' / 'answer-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
