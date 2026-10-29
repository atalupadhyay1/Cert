"""Load 600 authored Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric items.

Aligned to the official Microsoft Learn Study Guide for Exam DP-600
(Skills measured as of October 19, 2026; study guide updated September 18, 2026;
credential page updated October 19, 2026). Passing Exam DP-600 earns the
Associate-level `Microsoft Certified: Fabric Analytics Engineer Associate`
credential (no prerequisite certification required; 700 / 1000 scaled passing
score; 100 minutes exam time; annual free online renewal on Microsoft Learn).

Every 100-item mock exam allocates 26 / 47 / 27 items across the three official
functional groups and tests all 41 official sub-skills in a strict 1-to-1
mapping, combining single-choice scenarios, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL
completion items, `Proposed solution:` evaluation items, `Select two.`/`Select three.`
multi-select items, `→` ordered action sequences, and four original 3-question
enterprise Microsoft Fabric case studies.
"""
from pathlib import Path
import re
from terms import TERMS
import sequences as _sequences  # noqa: F401 — populates SEQUENCES into TERMS

HERE = Path(__file__).resolve().parent

DOMAINS = {
    1: 'Maintain a data analytics solution',
    2: 'Prepare data',
    3: 'Implement and manage semantic models',
}

DOMAIN_NOTES = {
    1: 'Workspace & Item Access, OneLake/SQL/DAX RLS-CLS-OLS-File Security, Purview Sensitivity Labels, Endorsement, Git & .pbip/TMDL, Deployment Pipelines, Impact Analysis, XMLA Endpoint & Reusable Assets (25–30%)',
    2: 'Connections & Gateways, OneLake Catalog & Real-Time Hub, Shortcuts/Mirroring/Pipelines/Dataflow Gen2/Eventstream, Store Selection, Eventhouse & Semantic Model OneLake Integration, Star Schema/SCD2/Transforms, and Visual/SQL/KQL/DAX Querying (45–50%)',
    3: 'Storage Modes, Semantic Star Schema, Bridge/Many-to-Many/USERELATIONSHIP, Advanced DAX & Windowing, Calculation Groups/Dynamic Formats/Field Parameters, Large & Composite Models, Performance/VertiPaq Tuning, Direct Lake on OneLake vs SQL & Incremental Refresh (25–30%)',
}

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Omnichannel Retail, Global Inventory Lakehouses, and Direct Lake Merchandising',
    2: 'Healthcare Claims Warehousing, Clinical IoT Eventhouses, and HIPAA Governance',
    3: 'Global FinTech Ledger Mirroring, Fraud KQL Streams, and Enterprise XMLA ALM',
    4: 'Smart Manufacturing, Connected Fleet Telemetry, and Supply-Chain Composite Models',
    5: 'Subscription Media Streaming, Ad-Tech Attribution, and Multi-Source Direct Lake',
    6: 'Renewable Energy Grids, Telecom Network Analytics, and Public-Sector Open Data',
}

# 41 local study-map skills mapped 1-to-1 to all 41 bullets in the October 19, 2026 DP-600 Study Guide.
SKILLS = {
    # Domain 1: Maintain a data analytics solution (25–30% -> 26 items)
    '1.1': 'Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)',
    '1.2': 'Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)',
    '1.3': 'Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models',
    '1.4': 'Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption',
    '1.5': 'Endorse Items Using Promoted, Certified, and Master Data Governance Badges',
    '1.6': 'Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)',
    '1.7': 'Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene',
    '1.8': 'Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys',
    '1.9': 'Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models',
    '1.10': 'Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)',
    '1.11': 'Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)',

    # Domain 2: Prepare data (45–50% -> 47 items)
    '2.1': 'Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)',
    '2.2': 'Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator',
    '2.3': 'Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams',
    '2.4': 'Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)',
    '2.5': 'Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models',
    '2.6': 'Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views',
    '2.7': 'Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns',
    '2.8': 'Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)',
    '2.9': 'Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables',
    '2.10': 'Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables',
    '2.11': 'Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins',
    '2.12': 'Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)',
    '2.13': 'Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)',
    '2.14': 'Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning',
    '2.15': 'Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views',
    '2.16': 'Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)',
    '2.17': 'Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)',
    '2.18': 'Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)',

    # Domain 3: Implement and manage semantic models (25–30% -> 27 items)
    '3.1': 'Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)',
    '3.2': 'Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)',
    '3.3': 'Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity',
    '3.4': 'Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE',
    '3.5': 'Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)',
    '3.6': 'Identify Use Cases for and Configure Large Semantic Model Storage Format',
    '3.7': 'Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)',
    '3.8': 'Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)',
    '3.9': 'Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction',
    '3.10': 'Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback',
    '3.11': 'Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)',
    '3.12': 'Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)',
}
VALID_TASKS = set(SKILLS)

# Official percentage bands published in the October 19, 2026 DP-600 Study Guide.
OFFICIAL_RANGES = {
    1: (25, 30),
    2: (45, 50),
    3: (25, 30),
}

# Exact 100-item allocation landing strictly inside every published range: 26 + 47 + 27 = 100.
ALLOCATIONS = {
    n: {1: 26, 2: 47, 3: 27}
    for n in range(1, 7)
}

SKILL_PLAN = {
    # Domain 1 = 26
    '1.1': 3, '1.2': 2, '1.3': 4, '1.4': 2, '1.5': 2,
    '1.6': 2, '1.7': 2, '1.8': 3, '1.9': 2, '1.10': 2, '1.11': 2,
    # Domain 2 = 47
    '2.1': 2, '2.2': 2, '2.3': 4, '2.4': 3, '2.5': 2,
    '2.6': 3, '2.7': 3, '2.8': 4, '2.9': 2, '2.10': 3, '2.11': 3, '2.12': 3, '2.13': 2, '2.14': 2,
    '2.15': 2, '2.16': 3, '2.17': 2, '2.18': 2,
    # Domain 3 = 27
    '3.1': 2, '3.2': 2, '3.3': 3, '3.4': 4, '3.5': 3, '3.6': 2, '3.7': 2,
    '3.8': 2, '3.9': 2, '3.10': 2, '3.11': 2, '3.12': 1,
}

# Multi-select spread across Domains 1-3: 4 + 8 + 4 = 16 (13 M2 + 3 M3).
MULTI_PLAN = {1: 4, 2: 8, 3: 4}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'multi-select': 16, 'ordering': 8}
CASE_STUDIES = 4
CASE_SIZE = 3
CODE_FILL_FLOOR = 18
PROPOSED_SOL_FLOOR = 6
ITEM_TOTAL = sum(TYPE_PLAN.values())

BANK = {}
for number in TOPICS:
    records = []
    path = HERE / 'questions' / f'{number}.txt'
    if path.is_file():
        for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip() or line.startswith('#'):
                continue
            parts = [x.strip().replace('\\|', '|') for x in re.split(r'(?<!\\)\|', line)]
            if len(parts) != 6:
                raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
            skill, kind, answers, distractors, question, reason = parts
            answer_keys = [x.strip() for x in answers.split(',') if x.strip()]
            distractor_keys = [x.strip() for x in distractors.split(',') if x.strip()]
            records.append(dict(
                id=f'T{number}-Q{len(records) + 1:03}',
                task=skill,
                domain=int(skill.split('.')[0]),
                kind=kind,
                answers=answer_keys,
                distractors=distractor_keys,
                keys=answer_keys + distractor_keys,
                question=question,
                reason=reason,
                line=line_number,
            ))
    BANK[number] = records
