"""Load 600 authored PL-300 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Prepare the data',
         2:'Model the data',
         3:'Visualize and analyze the data',
         4:'Manage and secure Power BI'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Connecting to Data Sources and Shared Semantic Models','1.2':'Choosing Import, DirectQuery, or DirectLake',
 '1.3':'Data Source Settings, Credentials, Privacy Levels, and Parameters','1.4':'Evaluating Data with Profiling and Column Statistics',
 '1.5':'Resolving Inconsistencies, Nulls, and Import Errors','1.6':'Column Data Types, Custom Columns, and Grouping',
 '1.7':'Pivot, Unpivot, Transpose, and Semi-Structured Data','1.8':'Merge and Append, Reference and Duplicate, Relationship Keys',
 '2.1':'Designing a Star Schema and Table Properties','2.2':'Relationship Cardinality and Cross-Filter Direction',
 '2.3':'Date Tables and Role-Playing Dimensions','2.4':'Measures, Calculated Columns, and Filter Context',
 '2.5':'CALCULATE and Filter Modifiers','2.6':'Time Intelligence and Semi-Additive Measures',
 '2.7':'Statistical Functions, Quick Measures, and Calculation Groups','2.8':'Model Performance and Granularity',
 '3.1':'Selecting and Formatting Visuals','3.2':'Slicers, Filters, and Visual Interactions',
 '3.3':'Bookmarks, Buttons, and Report Navigation','3.4':'Drillthrough, Drill-Down, and Tooltips',
 '3.5':'Accessibility, Mobile Layout, Personalization, and Export','3.6':'Sorting, Conditional Formatting, Themes, and the Selection Pane',
 '3.7':'Analyze Features, Grouping, Binning, and Forecasting','3.8':'AI Visuals, Anomaly Detection, Q&A, and Copilot',
 '4.1':'Workspaces and Workspace Roles','4.2':'Apps and Distribution Methods',
 '4.3':'Dashboards, Subscriptions, and Data Alerts','4.4':'Gateways and Scheduled Refresh',
 '4.5':'Row-Level Security','4.6':'Sensitivity Labels, Endorsement, and Item Access'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(25,30),2:(25,30),3:(25,30),4:(15,20)}
# 100-item exams: 28/28/28/16 percent, all inside the published ranges.
ALLOCATIONS={n:{1:28,2:28,3:28,4:16} for n in range(1,7)}
TYPE_PLAN={'multiple-choice':76,'multi-select':16,'ordering':8}
CASE_STUDIES=4          # four case studies of three questions per exam
ITEM_TOTAL=sum(TYPE_PLAN.values())
BANK={}
for number in TOPICS:
    records=[]
    path=HERE/'questions'/f'{number}.txt'
    for line_number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip() or line.startswith('#'):continue
        parts=[x.strip() for x in line.split('|')]
        if len(parts)!=6:raise ValueError(f'{path.name}:{line_number}: expected 6 fields')
        skill,kind,answers,distractors,question,reason=parts
        answer_keys=[x.strip() for x in answers.split(',') if x.strip()]
        distractor_keys=[x.strip() for x in distractors.split(',') if x.strip()]
        records.append(dict(id=f'T{number}-Q{len(records)+1:03}',task=skill,
                            domain=int(skill.split('.')[0]),kind=kind,
                            answers=answer_keys,distractors=distractor_keys,
                            keys=answer_keys+distractor_keys,
                            question=question,reason=reason,line=line_number))
    BANK[number]=records
