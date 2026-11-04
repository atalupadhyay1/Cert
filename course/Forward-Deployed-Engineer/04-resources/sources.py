"""Authoritative primary sources for Forward Deployed Engineer (FDE) 6x100 course."""

GSDC_CFDE_URL = 'https://www.gsdcouncil.org/certified-forward-deployed-engineer'
AWS_FDE_URL = (
    'https://aws.amazon.com/blogs/apn/'
    'new-fde-pathways-for-aws-partners-get-ready-for-production-agentic-ai-delivery/'
)

SKILL_SOURCES = {
    # Domain 1 — Client Discovery, Problem Structuring, and Engagement Scoping (15%)
    '1.1': (GSDC_CFDE_URL, AWS_FDE_URL),
    '1.2': (GSDC_CFDE_URL, 'https://aws.amazon.com/architecture/well-architected/'),
    '1.3': (
        'https://www.anthropic.com/research/building-effective-agents',
        AWS_FDE_URL,
    ),
    '1.4': ('https://sre.google/sre-book/service-level-objectives/', GSDC_CFDE_URL),
    '1.5': ('https://aws.amazon.com/architecture/cost-optimization/', GSDC_CFDE_URL),
    '1.6': ('https://www.nist.gov/itl/ai-risk-management-framework', AWS_FDE_URL),
    # Domain 2 — Production Software, APIs, and Enterprise System Integration (16%)
    '2.1': ('https://docs.pydantic.dev/latest/', 'https://docs.pytest.org/en/stable/'),
    '2.2': ('https://fastapi.tiangolo.com/', 'https://spec.openapis.org/oas/latest.html'),
    '2.3': (
        'https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig',
        'https://microservices.io/patterns/data/transactional-outbox.html',
    ),
    '2.4': (
        'https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/',
        'https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/',
    ),
    '2.5': ('https://12factor.net/', 'https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/'),
    '2.6': (GSDC_CFDE_URL, 'https://fastapi.tiangolo.com/advanced/custom-response/'),
    # Domain 3 — Enterprise Data Engineering, Ontologies, and Grounded RAG ("Ground") (18%)
    '3.1': ('https://debezium.io/documentation/', AWS_FDE_URL),
    '3.2': ('https://www.palantir.com/docs/foundry/ontology/overview/', AWS_FDE_URL),
    '3.3': ('https://scikit-learn.org/stable/modules/calibration.html', 'https://mlflow.org/docs/latest/'),
    '3.4': ('https://www.pinecone.io/learn/hybrid-search-intro/', AWS_FDE_URL),
    '3.5': ('https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html', AWS_FDE_URL),
    '3.6': ('https://platform.openai.com/docs/guides/optimizing-llm-accuracy', AWS_FDE_URL),
    '3.7': ('https://arxiv.org/abs/2307.03172', GSDC_CFDE_URL),
    # Domain 4 — LLM Workflows, Tool Design, and Agentic Orchestration ("Orchestrate") (20%)
    '4.1': ('https://modelcontextprotocol.io/introduction', GSDC_CFDE_URL),
    '4.2': ('https://www.anthropic.com/research/building-effective-agents', AWS_FDE_URL),
    '4.3': ('https://modelcontextprotocol.io/docs/concepts/tools', 'https://www.anthropic.com/engineering/writing-tools-for-agents'),
    '4.4': ('https://datatracker.ietf.org/doc/html/rfc8693', AWS_FDE_URL),
    '4.5': ('https://docs.temporal.io/workflows', AWS_FDE_URL),
    '4.6': ('https://www.anthropic.com/research/building-effective-agents', AWS_FDE_URL),
    '4.7': ('https://www.anthropic.com/research/building-effective-agents', 'https://modelcontextprotocol.io/introduction'),
    # Domain 5 — Cloud/Hybrid Deployment, CI/CD, Observability, and Reliability (15%)
    '5.1': ('https://docs.vllm.ai/en/latest/', 'https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html'),
    '5.2': ('https://martinfowler.com/bliki/CanaryRelease.html', 'https://slsa.dev/spec/v1.0/'),
    '5.3': ('https://sre.google/sre-book/monitoring-distributed-systems/', 'https://opentelemetry.io/docs/specs/semconv/gen-ai/'),
    '5.4': ('https://aws.amazon.com/builders-library/implementing-health-checks/', GSDC_CFDE_URL),
    '5.5': ('https://docs.vllm.ai/en/latest/', 'https://sre.google/sre-book/service-level-objectives/'),
    # Domain 6 — AI Security, Evaluation Harnesses, Governance, and Production Handover ("Prove") (16%)
    '6.1': ('https://www.nist.gov/itl/ai-risk-management-framework', AWS_FDE_URL),
    '6.2': ('https://genai.owasp.org/llm-top-10/', 'https://www.nist.gov/itl/ai-risk-management-framework'),
    '6.3': ('https://airc.nist.gov/AI_RMF_Knowledge_Base', AWS_FDE_URL),
    '6.4': ('https://www.prosci.com/methodology/adkar', 'https://www.kotterinc.com/methodology/8-steps/'),
    '6.5': ('https://sre.google/workbook/implementing-slos/', AWS_FDE_URL),
    '6.6': (AWS_FDE_URL, GSDC_CFDE_URL),
}
