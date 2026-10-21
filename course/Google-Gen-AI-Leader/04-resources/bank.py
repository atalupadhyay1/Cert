"""Original business-level Google Generative AI Leader learning bank.
Six authored scenarios per objective. Concepts intentionally recur across sets.
No actual, recalled, or copied examination questions.
"""
TERMS={}
ITEMS=[]
OVERRIDES={}
def term(key,label,explanation):
    if key in TERMS: raise ValueError(f'Duplicate term {key}')
    TERMS[key]=(label,explanation)
def item(domain,keys,reason,prompts,task):
    questions=[q.strip() for q in prompts.strip().splitlines() if q.strip()]
    assert len(questions)==6,(keys,len(questions))
    ITEMS.append(dict(domain=domain,keys=keys.split(),reason=reason,prompts=questions,
                      task=task,correct=1,ref=None))

term('gen','Generative AI','Creates new content from learned patterns; generated content still needs appropriate review.')
term('classification','Classification','Assigns inputs to predefined categories rather than generating open-ended content.')
term('regression','Regression','Predicts a numeric quantity rather than producing new prose, images, or video.')
term('rules','Deterministic rule-based processing','Applies explicit rules and is suitable when an exact prescribed result is required without probabilistic generation.')
term('ml','Machine learning','Learns useful patterns from data instead of requiring every decision rule to be manually programmed.')
term('deep','Deep learning','Is a subset of machine learning using neural networks with multiple layers to learn representations.')
term('ai','Artificial intelligence','Is the broad field of systems performing tasks associated with human intelligence; it includes more than generative models.')
term('supervised','Supervised learning','Learns from examples paired with known target labels or outcomes.')
term('unsupervised','Unsupervised learning','Finds patterns or groupings without supplied target labels.')
term('reinforcement','Reinforcement learning','Learns actions through interaction and reward or penalty feedback.')
term('structured','Structured data','Uses a predefined organization such as rows and typed columns in a relational table.')
term('unstructured','Unstructured data','Includes free-form content such as prose, audio, and images without a fixed tabular schema.')
term('labeled','Labeled data','Pairs examples with assigned tags, categories, or target outcomes; a structured file is not automatically labeled.')
term('unlabeled','Unlabeled data','Lacks supplied target annotations; it may still contain useful patterns and can be structured or unstructured.')
term('quality','Improve data accuracy, completeness, consistency, and relevance','Addresses defects in the source evidence; greater model capacity does not automatically repair incorrect data.')
term('access','Ensure authorized data is available in a usable format','Makes relevant evidence practically usable while retaining permissions and governance; accessibility does not mean public access.')
term('ingest','Data ingestion','Collects or brings source information into the data workflow before later processing.')
term('prepare','Data preparation','Cleans, transforms, and organizes collected data for its intended use.')
term('train','Model training','Learns model parameters from data; it is different from serving a trained model to users.')
term('deploy','Model deployment','Makes a trained or selected model available for application use.')
term('manage','Model management','Monitors, versions, maintains, and improves models after deployment as conditions change.')
term('inference','Inference','Uses a trained model to produce an output for new input without inherently updating its weights.')
term('fm','Foundation model','Is broadly pretrained and can support or be adapted to multiple downstream tasks.')
term('llm','Large language model','Is designed to process and generate language using learned patterns; fluency is not proof of truth.')
term('multi','Multimodal foundation model','Can work with multiple input or output modalities, subject to the selected model capabilities.')
term('diffusion','Diffusion model','Learns to reverse a noise process and is commonly used for image generation.')
term('choose','Evaluate model fit against business and operational requirements','Considers modality, quality, context, security, availability, customization, latency, and total cost.')
term('largest','Choose only the largest available model','Can increase cost or latency without establishing task suitability or meeting governance requirements.')
term('cheapest','Choose only the lowest token price','Ignores quality, retries, review effort, latency, and other costs of the full solution.')
term('infra','Infrastructure layer','Provides compute, accelerators, storage, networking, and supporting resources used to train and serve AI systems.')
term('platform','Platform layer','Provides APIs and services for developing, deploying, and managing models and AI applications.')
term('agent','Agent layer','Combines a model or decision logic with tools and a goal-oriented workflow to observe and act.')
term('application','Application layer','Provides the user-facing experience that embeds AI capabilities into a business workflow.')
term('gemini','Gemini model family','Supports broad multimodal and language tasks, with specific modalities and limits depending on the chosen model.')
term('gemma','Gemma model family','Offers open-weight model options for compatible customized or local deployments, subject to license and hardware requirements.')
term('imagen','Imagen model family','Focuses on generating and editing images from supported inputs, rather than serving as a video-generation family.')
term('veo','Veo model family','Focuses on video generation from supported prompts or image inputs, subject to model availability and capabilities.')
term('draft','Use generative AI to draft content with suitable review','Fits open-ended content creation when quality, rights, and risk controls are addressed.')
term('biggerdata','Add more data without checking its quality','Can amplify errors or irrelevant content and is not a substitute for data validation.')
term('prompt','Prompt engineering','Refines instructions, examples, and context at inference time without changing learned model weights.')

item(1,'gen classification regression rules','The defining requirement is new content, not a fixed label or numeric forecast.', '''A marketing team wants new campaign headlines from a creative brief. Which AI capability most directly fits?
A learning team needs fresh practice scenarios based on course objectives. Which capability is this?
A product team wants original draft descriptions from product attributes. Which AI capability fits?
A designer asks a system to create an image that does not yet exist. Which capability is being used?
A support assistant drafts a new response tailored to a customer message. Which AI capability fits?
A publisher creates candidate summaries and new introductory paragraphs from source material. Which capability fits?''','1.1')
item(1,'ml rules infra application','Learning a decision pattern from examples is machine learning rather than exclusively hand-written rules.', '''A retailer builds a predictor that learns purchasing patterns from past transactions. Which concept describes this approach?
An insurer replaces manually coded scoring rules with a model fitted to historical examples. Which concept fits?
A factory trains a detector from observed examples instead of listing every possible defect rule. Which approach is this?
A business system improves predictions by learning relationships from data. Which field most directly describes this?
A service learns how inputs relate to outcomes rather than requiring a programmer to specify every relationship. Which approach fits?
A manager describes software that learns patterns from experience represented in datasets. Which concept is this?''','1.1')
item(1,'deep rules supervised structured','Multiple neural-network layers distinguish deep learning; supervision is a separate description of the training signal.', '''A presentation describes a model that learns representations through many neural-network layers. Which term fits?
An image system uses a neural network with multiple hidden layers. Which ML category is this?
A leader asks what distinguishes a multi-layer neural representation model from ML in general. Which term fits?
A training architecture uses stacked neural layers to extract complex patterns. Which concept fits?
A team uses a many-layer neural network for speech processing. Which category is most specific to that architecture?
A diagram places multi-layer neural-network methods inside the wider machine-learning field. What is this inner category?''','1.1')
item(1,'supervised unsupervised reinforcement rules','Known target outcomes supply the training signal for supervised learning.', '''A team has customer records labeled churned or retained. Which learning approach can use these targets?
A document classifier trains on files paired with verified categories. Which learning approach fits?
A lender supplies historical applications with known repayment outcomes. Which learning approach fits?
A support team labels reviews positive or negative before training a predictor. Which learning approach is this?
A factory has measurements paired with confirmed defect labels. Which learning approach fits?
A model learns from examples that include the correct expected answer. Which learning approach is being used?''','1.1')
item(1,'unsupervised supervised reinforcement rules','Discovering structure without supplied target labels is unsupervised learning.', '''A retailer wants natural customer segments but has no segment labels. Which learning approach fits?
A publisher explores unlabeled articles to discover groups of related topics. Which learning approach fits?
A company wants to identify patterns in usage records without known output categories. Which approach fits?
An analyst groups similar stores using their behavior rather than predefined labels. Which learning approach is this?
A research team explores structure in unlabeled measurements. Which learning approach fits?
A marketing team seeks previously unknown clusters in purchase histories. Which approach fits?''','1.1')
item(1,'reinforcement supervised unsupervised prepare','Reward-driven learning through actions and feedback differs from fitting fixed labeled examples.', '''A simulated agent receives rewards for completing tasks safely and penalties for failures. Which learning approach fits?
A game-playing system improves by receiving a score after taking actions. Which approach fits?
A simulated robot learns behavior from rewards for successful deliveries. Which learning approach is this?
A decision agent explores actions and receives feedback about long-term success. Which learning approach fits?
A controller learns a policy through reward signals from its environment. Which approach fits?
An interactive simulator provides penalties for unsafe moves and rewards for reaching a goal. Which learning approach fits?''','1.1')
item(1,'structured unstructured labeled unlabeled','A fixed schema is the key property; label availability is a separate distinction.', '''A sales dataset has typed columns for date, SKU, quantity, and price. Which data category best describes its organization?
A bank stores transactions in rows with consistent fields and data types. Which data structure is this?
An inventory system uses a relational table with a predefined schema. Which data category fits?
A dashboard reads numeric measures from uniformly organized database records. Which data category fits?
A finance team uses a table with fixed account and amount columns. Which data organization is this?
A customer database enforces a defined set of fields for each record. Which data category fits?''','1.2')
item(1,'unstructured structured labeled regression','Free-form prose, audio, and imagery require processing beyond assuming a consistent row-and-column schema.', '''A company wants to analyze free-form call recordings. Which data category best describes the source content?
An archive contains scanned photos and narrative letters rather than uniform table records. Which data category fits?
A business collects long customer emails with no fixed field layout. Which data organization fits?
A media library consists of video clips and spoken interviews. Which data category fits?
A legal team has narrative documents rather than a consistent table of facts. Which data category fits?
A research project uses images and free-text comments as source content. Which data category fits?''','1.2')
item(1,'labeled structured unlabeled unstructured','Supplied target annotations make the examples labeled regardless of whether the underlying inputs are text, images, or tables.', '''Photos are paired with human-assigned object categories. What property makes this a labeled dataset?
A spreadsheet includes a verified fraud outcome for every example. Which data category describes the target annotations?
A set of customer messages includes reviewer-assigned sentiment tags. Which description fits these examples?
Recordings are paired with verified text transcripts for training. Which data property is present?
A dataset includes examples and their approved expected outputs. Which description fits?
An image collection has a checked defect category attached to each image. Which target-data category fits?''','1.2')
item(1,'quality biggerdata largest prompt','Incorrect, missing, or inconsistent evidence requires source-data improvement rather than merely changing generation settings.', '''An assistant gives conflicting answers because the source catalog contains duplicate products with contradictory prices. What should be prioritized?
A model project has missing customer fields and inconsistent units. Which action addresses the source issue?
A business wants reliable AI results from incomplete and inaccurate records. Which foundation should it improve first?
A document assistant repeats outdated procedures mixed with approved ones. Which data practice addresses the root problem?
An analysis pipeline uses contradictory date formats and mislabeled records. Which improvement fits?
A generative application draws from irrelevant and incomplete documents. Which foundational action should lead remediation?''','1.2')
item(1,'access quality biggerdata largest','Useful data must be available to authorized workflows in an accessible format; mere existence does not make it usable.', '''Approved knowledge exists but is locked in an unusable format unavailable to the application. Which issue should be addressed?
A pilot has clean source records but no authorized connection to retrieve them. Which data foundation is missing?
A company owns relevant documents but its AI workflow cannot access the approved repository. Which action fits?
An analyst cannot use licensed evidence because the required interface is not available. Which data requirement needs attention?
A business has high-quality data but cannot deliver it to the permitted application in time. Which constraint should be addressed?
A team must make approved knowledge usable without making it public. Which data-access approach fits?''','1.2')
item(1,'ingest prepare train deploy','Bringing source data into a workflow is ingestion; cleaning or model fitting happens later.', '''A pipeline first collects files from approved repositories into its data workflow. Which lifecycle activity is this?
A team imports permitted customer feedback from several source systems. Which data lifecycle stage is this?
A business assembles raw records before any cleaning or transformation. Which stage is this?
An AI project brings approved source documents into its processing environment. Which activity is this?
A scheduled process gathers newly authorized records from business systems. Which lifecycle activity fits?
A data team loads raw observations from source platforms for later processing. Which stage is this?''','1.1')
item(1,'prepare ingest train deploy','Cleaning and transforming already collected information is data preparation.', '''A team standardizes dates, removes corrupt records, and normalizes source fields. Which lifecycle activity fits?
Collected documents are cleaned and converted into a usable format. Which stage is this?
A pipeline fixes inconsistent units before model training. Which lifecycle activity is this?
An analyst removes invalid duplicates and transforms fields after collection. Which stage fits?
A project organizes raw records and corrects formatting defects for model use. Which activity is this?
A company converts gathered source material into consistent training-ready data. Which lifecycle stage fits?''','1.1')
item(1,'train inference deploy manage','Learning weights or parameters from data is training rather than serving predictions.', '''A learning job updates a model's weights using approved examples. Which lifecycle activity is occurring?
A model learns patterns from historical data before it serves users. Which stage is this?
A team optimizes internal model parameters against training examples. Which activity is this?
An adaptation run changes learned values in a model using task data. Which lifecycle activity fits?
A development process fits a predictive model to historical observations. Which activity is this?
A company runs a job that learns a model from data rather than merely calling it. Which stage fits?''','1.1')
item(1,'deploy train ingest prepare','Making a model available to applications is deployment rather than learning weights or collecting data.', '''A trained model is made available through an application endpoint. Which lifecycle activity is this?
A team publishes a selected model so an approved service can call it. Which stage fits?
A pilot moves from an offline model artifact to a usable application service. Which activity is this?
A business enables its trained predictor for operational requests. Which lifecycle stage fits?
A release makes a model available for inference by authorized applications. Which activity is this?
A project transitions a tested model into a serving environment. Which lifecycle activity fits?''','1.1')
item(1,'manage train ingest prepare','Deployed systems still need monitoring, versioning, maintenance, and reassessment.', '''A deployed model is monitored for changing performance and updated under version control. Which lifecycle stage fits?
A business checks whether an operational AI system still meets quality goals. Which ongoing activity is this?
A team maintains released model versions and investigates declining results. Which lifecycle stage fits?
An application model needs ongoing tracking and controlled improvement after launch. Which lifecycle activity fits?
A company schedules reviews of its deployed AI quality and maintenance needs. Which stage is this?
A production model is monitored and maintained as input conditions change. Which lifecycle activity fits?''','1.1')
item(1,'fm classification rules infra','Broad pretraining and reuse across downstream tasks distinguish foundation models from narrow task-specific rules.', '''A broadly pretrained model supports summarization, question answering, and later adaptation. Which model category fits?
A team wants a reusable pretrained starting point for several business tasks. Which model type fits?
An AI model learns general patterns from diverse data before task-specific customization. Which category fits?
A business reuses one broad base model across many applications. Which model category is this?
An organization selects a pretrained base that can be adapted instead of training every task from scratch. Which type fits?
A vendor supplies a broadly trained model capable of many downstream uses. Which category fits?''','1.1')
item(1,'llm regression structured infra','A language model is suited to language understanding and generation, not a guarantee of factual accuracy.', '''A business needs a model primarily designed to understand and generate natural language. Which category fits?
A writing assistant predicts language continuations and drafts paragraphs. Which model category is relevant?
A team needs text summarization and conversational language responses. Which model category fits?
A documentation tool generates natural-language explanations from instructions. Which model category fits?
A model's main role is processing and producing sequences of language. Which category fits?
An assistant rewrites text and answers questions in prose. Which model category is a natural fit?''','1.1')
item(1,'multi llm regression structured','Multiple modalities are required when the same interaction includes distinct types such as images and text.', '''An assistant must interpret a chart image together with a written question. Which model capability is required?
A business wants to ask questions about both audio and text content using a suitable model. Which capability fits?
An inspection assistant needs to combine a photo with an employee's typed description. Which model category fits?
A learning application accepts diagrams as well as written questions. Which model capability matters?
A model must relate a visual product design to a natural-language brief. Which capability fits?
A system processes video frames and accompanying language in a supported workflow. Which model capability is relevant?''','1.1')
item(1,'diffusion regression classification supervised','Iterative generation by reversing a noise process is characteristic of diffusion; supervision is not the defining model family.', '''An image generator starts with noise and progressively denoises it into a picture. Which model family fits?
A training explanation describes learning to reverse a gradual image-noising process. Which generative approach is this?
A visual system creates samples through repeated denoising steps. Which model family fits?
A model synthesizes images by removing noise under prompt guidance. Which approach is this?
A design presentation describes iterative denoising for picture generation. Which model family is relevant?
A generator learns the reverse of a corruption process to create new images. Which approach fits?''','1.1')
item(1,'choose largest cheapest biggerdata','The best business choice must meet actual capability and operating requirements, not win one size or price ranking.', '''A company needs image understanding, approved data handling, and low response time. How should it select a foundation model?
A cheap model produces errors that require expensive review. Which model-selection approach is more appropriate?
A procurement team assumes the largest model is best for every task. Which selection principle should replace that assumption?
A regulated assistant has specific reliability, security, and context requirements. Which model-selection approach fits?
A team compares models that differ in quality, modality, and customization options. Which decision method fits?
A business must choose a model that supports its task and operating constraints. Which selection strategy fits?''','1.1')
item(1,'infra platform agent application','Accelerators, servers, networking, and storage form the enabling infrastructure layer.', '''A diagram groups TPUs, GPUs, networking, and storage together. Which gen AI landscape layer is this?
A leader asks which layer supplies physical compute for training and inference. Which layer fits?
A proposal focuses on data centers and accelerator capacity rather than model APIs. Which landscape layer is this?
A cost analysis separates hardware and cloud compute from application features. Which layer contains those resources?
An enterprise invests in servers, storage, and networking used by AI systems. Which landscape layer is this?
A team evaluates the underlying compute foundation for model training and serving. Which layer is being evaluated?''','1.3')
item(1,'platform infra agent application','Model-development and management APIs belong to the platform layer rather than the user-facing business interface.', '''A service provides model APIs, deployment tooling, and lifecycle management. Which gen AI landscape layer fits?
A team needs a managed bridge between underlying compute and application development. Which layer fits?
A diagram highlights model management and development services rather than hardware. Which layer is this?
An enterprise adopts APIs and tools to simplify building and operating AI applications. Which landscape layer fits?
A system offers developers model selection and deployment capabilities. Which layer is this?
A leader distinguishes a managed AI development environment from the final employee application. Which layer contains the environment?''','1.3')
item(1,'agent application platform infra','An agent pursues a goal using a reasoning or decision loop and permitted tools, rather than only displaying a response.', '''A system plans steps, checks inventory with a tool, and completes a permitted task. Which landscape layer best describes that goal-directed component?
A software component observes results and selects another permitted action toward a goal. Which layer fits?
A workflow combines model decisions with tools to act on a business request. Which landscape component is this?
A service can choose among approved tools and iterate toward a task outcome. Which component fits?
A business distinguishes goal-directed tool use from a simple user interface. Which landscape layer contains that capability?
An assistant reasons about next steps and invokes permitted external functions. Which landscape component fits?''','1.3')
item(1,'application platform infra fm','The business user interface is the application layer; the model and platform power it behind the scenes.', '''Employees use a branded help portal that embeds generative AI. Which landscape layer is the portal itself?
A sales team interacts with a user-facing proposal-drafting product. Which gen AI layer contains this experience?
A retailer exposes an AI shopping experience through its website. Which landscape layer is the user-facing product?
A company builds a document-review interface on top of model APIs. Which layer is that interface?
A business user opens an AI-enabled workflow tool rather than calling a model API directly. Which layer is being used?
A product team designs the screens and business workflow that present AI features to users. Which landscape layer fits?''','1.3')
item(1,'gemini gemma imagen veo','Gemini is the broad multimodal model family; the chosen variant must still support the required inputs and limits.', '''A team needs a Google model family for broad multimodal understanding and conversational tasks. Which family fits?
A leader wants a Google foundation-model family for text reasoning and supported image understanding. Which family fits?
An application needs a broad Google conversational model rather than a specialist video generator. Which family fits?
A business wants a Google model family for varied language and multimodal use cases. Which family fits?
A team selects a Google foundation-model family for supported cross-modal question answering. Which family fits?
A product combines language generation with understanding of supported visual inputs. Which broad Google model family fits?''','1.4')
item(1,'gemma gemini imagen veo','An open-weight deployment requirement points to Gemma; license, hardware, and operational fit still need review.', '''A developer needs a Google open-weight model option for a compatible local deployment. Which family should be evaluated?
A business wants to customize and host a suitable Google open-weight model under its license. Which family fits?
A project prioritizes compatible self-hosted deployment rather than a managed-only model interface. Which Google family is relevant?
An organization needs a compact open-weight Google model option for a specialized environment. Which family fits?
A team wants model-weight deployment flexibility and will assess hardware and licensing. Which Google family fits?
A developer evaluates Google's open-weight models for a local application. Which family should be considered?''','1.4')
item(1,'imagen veo gemma classification','The requirement is image generation, not video generation or classification of an existing picture.', '''A marketing team needs still images generated from text briefs. Which Google model family fits most directly?
A designer wants product-concept artwork created from a written description. Which family fits?
A retailer needs generated campaign images rather than video clips. Which Google model family fits?
A creative team wants an image-focused Google generation family. Which one fits?
A business needs illustrations produced from supported prompts. Which Google model family is the most direct fit?
A company wants to generate still visual assets from a creative brief. Which Google model family fits?''','1.4')
item(1,'veo imagen gemma classification','The defining deliverable is generated video rather than a still image or a label.', '''A creative team needs a short video generated from a supported prompt. Which Google model family fits?
A marketing brief calls for moving video content rather than a still image. Which Google family fits?
A company wants to turn a supported text or image input into generated video. Which model family is relevant?
A media team evaluates Google's video-generation capabilities. Which model family fits?
A product campaign needs generated video sequences from supported creative inputs. Which family fits?
A designer wants a Google video-generation family for a visual storytelling concept. Which one fits?''','1.4')
item(1,'rules draft agent fm','An exact prescribed calculation or rule is usually better executed deterministically, even if a generative interface surrounds it.', '''A business must calculate tax using an exact approved formula. Which approach should perform the calculation itself?
A workflow requires an identical legally prescribed arithmetic result for the same inputs. Which processing approach fits?
An invoice system must apply fixed discount rules without creative variation. Which approach should handle that step?
A company needs an exact checksum rather than a plausible generated explanation. Which approach should compute it?
A payment process must enforce a precise threshold rule on every request. Which approach should implement the rule?
A leader proposes a generative model for an exact deterministic fee calculation. Which processing approach is more suitable for the calculation?''','1.1')
term('tpu','Google Tensor Processing Units (TPUs)','Are Google-designed accelerators optimized for supported machine-learning workloads; suitability still depends on the workload.')
term('gpu','Graphics processing units (GPUs)','Provide parallel acceleration widely used for compatible training and inference workloads.')
term('cpu','General-purpose CPUs','Handle general computation but do not denote a specialized parallel AI accelerator family.')
term('managed','Use managed cloud capacity with workload-aware scaling','Can reduce infrastructure operating burden while capacity, quotas, reliability, and cost still require planning.')
term('open','Evaluate model and framework choice through an open ecosystem','Supports flexibility across eligible first-party, third-party, and open models rather than assuming one model suits every use case.')
term('controls','Assess enterprise security, privacy, governance, and service controls','Checks the actual service, account, configuration, and terms instead of assuming all AI products handle data identically.')
term('lowcode','Use supported prebuilt APIs and low-code or no-code tools','Can lower development barriers for suitable tasks without eliminating testing, governance, or all technical work.')
term('gems','Gems in the Gemini app','Provide reusable personalized assistant instructions for supported tasks; they are not automatically a fully deployed enterprise agent platform.')
term('geminiapp','Gemini app','Provides a conversational user-facing assistant experience; its features and data terms depend on account and offering.')
term('workspace','Gemini for Google Workspace','Brings supported AI assistance into Workspace applications such as Gmail and Docs, subject to edition and availability.')
term('enterprise','Gemini Enterprise','Supports enterprise information discovery and custom agent experiences across authorized organizational sources, subject to configuration.')
term('notebook','Gemini Notebook source-grounded research capabilities','Help users work with selected source materials through summaries and source-oriented questions, subject to the available offering.')
term('search','Agent Search on Gemini Enterprise Agent Platform','Provides managed enterprise search and retrieval capabilities for supported business content and applications.')
term('googlesearch','Google Search and supported Search grounding','Provides access to public world information; it does not automatically grant access to confidential enterprise repositories.')
term('conversational','Conversational Agents','Supports customer-facing conversational experiences and task interactions, subject to configured capabilities and integrations.')
term('assist','Agent Assist','Provides supported guidance and assistance to human contact-center agents during their work.')
term('insights','Conversational Insights','Analyzes customer conversations to identify themes, patterns, and operational improvement opportunities.')
term('ccaas','Google Cloud Contact Center as a Service','Provides cloud-based contact-center capabilities rather than merely analyzing historical conversation text.')
term('garden','Model Garden on Agent Platform','Helps teams discover and evaluate supported Google, third-party, and open models, subject to model-specific terms and availability.')
term('automl','Agent Platform AutoML','Supports training suitable models with reduced manual model-development effort; it is not a general guarantee that every task can be automated.')
term('customagents','Use Agent Platform to build a controlled custom agent','Combines model capabilities, approved tools, knowledge, and orchestration for a purpose-specific business workflow.')
term('ragapi','Use supported RAG APIs for a custom retrieval workflow','Provides building blocks for retrieving and supplying external evidence when a team needs application-specific integration.')
term('agentstudio','Agent Studio','Is positioned in the retrieved guide for building production-oriented AI applications with cloud platform capabilities.')
term('aistudio','Google AI Studio','Supports rapid prototyping and experimentation with supported Gemini capabilities; a prototype alone does not establish production readiness.')
term('storage','Cloud Storage','Provides object storage for files and datasets rather than a complete conversation agent or a transactional relational database.')
term('run','Cloud Run','Provides managed hosting for compatible containerized applications and services, subject to runtime and service configuration.')
term('functions','Cloud Run functions / Cloud Functions','Supports suitable event-driven functions and tool implementations; naming varies across guide and service generations.')
term('stt','Speech-to-Text API','Converts supported speech audio into text rather than synthesizing spoken output.')
term('tts','Text-to-Speech API','Converts text into supported synthesized speech rather than transcribing input audio.')
term('translation','Translation API','Translates supported text between languages; it does not by itself constitute structured document extraction.')
term('doctranslation','Document Translation','Translates supported formatted documents while aiming to preserve document layout, subject to format limitations.')
term('docai','Document AI','Extracts and processes information from supported documents, including structured fields for suitable processors.')
term('vision','Cloud Vision API','Analyzes supported image content, such as objects, text, and landmarks; it is distinct from generating a new image.')
term('video','Cloud Video Intelligence API','Analyzes supported video content and extracts useful annotations rather than generating new video.')
term('nlp','Natural Language API','Analyzes existing text for supported tasks such as sentiment, entities, and classification.')
term('database','Use an authorized database lookup tool','Retrieves authoritative structured business records through enforced access rather than inventing live facts from model weights.')
term('tool','Use a validated function or extension to an external service','Lets trusted application code perform an authorized real-world operation; generated text claiming success is not proof of execution.')

item(2,'tpu gpu cpu storage','TPUs are Google-designed machine-learning accelerators; accelerator choice still needs workload evaluation.', '''A leader asks which Google-designed chip family accelerates supported machine-learning workloads. Which option fits?
An infrastructure proposal names Google's custom tensor-processing accelerators. Which component is this?
A business reviews Google's specialized ML accelerator family rather than general storage. Which option fits?
A team wants to identify Google's custom-designed tensor hardware in the AI infrastructure stack. Which component fits?
A presentation describes Google-developed accelerators optimized for supported tensor operations. Which hardware family fits?
An executive compares GPUs with Google's own ML-oriented accelerator design. Which option names that design?''','2.1')
item(2,'gpu cpu storage database','GPUs provide widely used parallel acceleration; they are distinct from the specifically Google-designed TPU family.', '''A team needs a widely supported parallel processor family for a compatible deep-learning framework. Which option fits?
A proposal uses graphics processors to accelerate supported model computation. Which hardware family is this?
A business reviews GPU-backed infrastructure for training and inference. Which option describes the accelerator?
An application needs parallel acceleration supported by its GPU-oriented model stack. Which component fits?
A leader wants to distinguish graphics accelerators from general-purpose processors. Which option identifies the former?
An AI workload relies on a compatible ecosystem of graphics-processing accelerators. Which hardware family fits?''','2.1')
item(2,'managed largest cheapest storage','Managed services can reduce operational work, but scale and cost still need workload-specific planning.', '''A company wants to avoid operating every AI server while retaining capacity and cost planning. Which infrastructure approach fits?
A startup needs scalable AI hosting without building its own data center. Which cloud approach should it evaluate?
A leader wants less infrastructure administration but understands that quotas still apply. Which approach fits?
An enterprise needs to adapt AI capacity to workload demand without owning all hardware. Which approach fits?
A business wants managed AI infrastructure while defining reliability and spending goals. Which approach fits?
A team seeks lower infrastructure operating burden without assuming unlimited free capacity. Which strategy fits?''','2.1')
item(2,'open largest cheapest rules','An open ecosystem offers flexibility and choice, not an obligation to use one proprietary model for every task.', '''A company wants to compare supported first-party, third-party, and open models. Which Google Cloud ecosystem benefit is most relevant?
A leader wants flexibility to use different compatible model and framework options. Which platform approach fits?
A business avoids assuming one model must serve every workload. Which ecosystem principle supports that decision?
An enterprise values the ability to evaluate eligible models from multiple sources. Which platform benefit fits?
A procurement team asks why model choice matters for avoiding unnecessary dependence on one option. Which approach is relevant?
A solution team wants compatible open and commercial model choices under their respective terms. Which ecosystem principle fits?''','2.1')
item(2,'controls geminiapp largest biggerdata','Enterprise readiness must be evaluated at the selected service and configuration, not inferred from a brand name alone.', '''A regulated company is choosing an AI offering for confidential business data. What should it evaluate before adoption?
A manager assumes a personal chatbot account has the same data terms as an enterprise service. Which review should correct this?
An enterprise needs evidence of data handling, access, and governance controls for its AI deployment. Which action fits?
A team wants to know whether an AI service meets privacy and reliability requirements. Which assessment is appropriate?
A company plans to move internal records into an AI workflow. Which service-specific review should lead the decision?
A procurement group needs to compare enterprise AI offerings beyond their demos. Which assessment fits?''','2.1')
item(2,'lowcode train infra largest','Prebuilt APIs and suitable low-code tools reduce entry barriers, but do not remove responsibility for quality and governance.', '''A business team wants to prototype an AI workflow without building a model from scratch. Which platform approach can help?
A small company lacks a large ML engineering team but has a suitable standard use case. Which development approach should it evaluate?
A leader wants business specialists to participate in building supported AI solutions. Which capability lowers development barriers?
A department needs a simple supported AI workflow and wants to minimize custom model development. Which approach fits?
An organization wants to democratize AI development while retaining oversight. Which tooling approach fits?
A team can use standard AI capabilities rather than create every component manually. Which approach reduces the implementation barrier?''','2.1')
item(2,'gems workspace automl garden','Reusable personal assistant instructions inside the Gemini app point to Gems, not model training or model discovery.', '''A user repeatedly gives the Gemini app the same writing instructions and wants a reusable personalized assistant. Which feature fits?
An employee wants a tailored Gemini assistant for a recurring briefing task. Which feature fits?
A team member needs to reuse a specific instruction style in the Gemini app. Which feature is relevant?
A user wants a personalized assistant setup for repeated editing tasks within Gemini. Which capability fits?
A professional wants to save task guidance for a recurring Gemini interaction. Which feature fits?
A user asks for a reusable instruction-based assistant in the Gemini app rather than a custom training job. Which feature fits?''','2.2')
item(2,'workspace enterprise garden automl','Assistance inside familiar Workspace productivity applications fits Gemini for Google Workspace.', '''Employees need AI assistance composing emails in Gmail and drafting text in Docs. Which offering fits?
A company wants supported AI features embedded in its existing Workspace applications. Which product fits?
A leader prioritizes writing help in familiar productivity tools rather than a custom application. Which offering fits?
An organization wants supported meeting and document assistance in Google Workspace. Which solution fits?
A department needs AI-enabled productivity without leaving its existing supported Workspace apps. Which offering fits?
A team wants everyday AI assistance within Gmail and Docs, subject to edition availability. Which product fits?''','2.2')
item(2,'enterprise workspace googlesearch garden','Cross-source enterprise discovery and agent experiences require organizational connectors and permissions, not only public web search.', '''Employees need an enterprise AI experience across authorized internal repositories and custom agents. Which offering fits?
A company wants a business knowledge assistant spanning several permitted organizational sources. Which product fits?
An enterprise needs internal discovery and agent capabilities beyond editing a single Workspace document. Which offering fits?
A leader wants an organizational AI entry point grounded in permitted company knowledge. Which product fits?
A business wants employees to find and use information across connected internal systems with access controls. Which offering fits?
A firm seeks an enterprise search-and-agent experience for internal knowledge rather than public-only search. Which product fits?''','2.2')
item(2,'notebook garden automl ccaas','A source-oriented research assistant fits notebook capabilities; it is not a model catalog or contact-center platform.', '''An analyst wants summaries and questions focused on a selected collection of source materials. Which capability fits?
A researcher needs assistance understanding a bounded set of supplied documents. Which offering category fits?
A business user wants to explore and summarize chosen reference files through a notebook-style research experience. Which capability fits?
A team needs source-oriented study of approved uploaded materials rather than model training. Which capability fits?
An employee wants a research assistant centered on selected documents, subject to the available enterprise offering. Which capability fits?
A user wants to work through key points and questions from a chosen source collection. Which capability fits?''','2.2')
item(2,'search googlesearch garden automl','Managed search over business content fits Agent Search; model discovery is a different function.', '''A retailer wants managed search over its approved product content for an external customer experience. Which offering fits?
A company needs enterprise retrieval over a configured business content source. Which service category fits?
A business wants search and discovery for its own supported content rather than a general web search. Which offering fits?
A customer portal needs managed retrieval over approved company information. Which offering fits?
A team needs a prebuilt business-search foundation rather than implementing all retrieval components itself. Which offering fits?
An organization wants managed search capabilities on Agent Platform for supported content. Which product fits?''','2.3')
item(2,'googlesearch search enterprise notebook','Public world information calls for web search or supported Search grounding; confidential sources need separate authorized access.', '''An assistant needs current publicly available information from the web rather than internal records. Which source approach fits?
A user asks for recent public announcements unavailable in the company's document store. Which grounding source fits?
A business wants answers informed by relevant public web evidence. Which source approach fits?
An application needs world information rather than privileged enterprise files. Which grounding option fits?
A leader wants to distinguish public-information retrieval from connected internal search. Which option serves public information?
An assistant must consult current public sources through a supported grounding capability. Which approach fits?''','2.3')
item(2,'conversational assist insights ccaas','A customer-facing conversational interaction differs from helping a human agent or analyzing completed calls.', '''A company needs a customer-facing conversational assistant for routine support requests. Which offering category fits?
A service team wants a supported virtual conversational experience for customers. Which product fits?
A business wants customers to interact with an automated conversational agent. Which offering fits?
A support site needs a task-oriented conversation interface rather than only retrospective analytics. Which capability fits?
A company plans a customer-facing chatbot connected to permitted business workflows. Which offering category fits?
A leader needs a conversational self-service experience rather than guidance only for human call-center staff. Which offering fits?''','2.3')
item(2,'assist conversational insights ccaas','Real-time support for a human contact-center worker fits Agent Assist.', '''A contact center wants suggested answers for its human agents during customer conversations. Which offering fits?
A support representative needs relevant guidance while handling a live case. Which product fits?
A company wants to augment human contact-center workers rather than replace the conversation with a bot. Which offering fits?
A leader needs AI assistance for staff while they speak with customers. Which capability fits?
A service organization wants supported recommendations shown to a live human agent. Which product fits?
A call-center team wants AI to help employees respond during their work. Which offering fits?''','2.3')
item(2,'insights assist conversational ccaas','Analyzing patterns across customer conversations is an insights task, not only a live assistance task.', '''A company wants to identify recurring complaint themes across completed support conversations. Which offering fits?
A contact-center manager needs analytics on customer interactions to improve operations. Which product fits?
A team wants to understand why customers repeatedly contact support using conversation analysis. Which capability fits?
A service leader needs trends and patterns from a large set of call transcripts. Which offering fits?
An organization wants to analyze historical conversations for improvement opportunities. Which product fits?
A business needs insight into common issues across customer communications rather than suggestions during one call. Which offering fits?''','2.3')
item(2,'ccaas assist insights translation','An overall cloud contact-center capability is broader than an AI helper or a conversation analytics component.', '''A company wants a cloud-based contact-center platform as the foundation for customer service. Which offering fits?
A service organization needs contact-center capabilities, not merely sentiment analysis of transcripts. Which product category fits?
A leader is selecting cloud contact-center infrastructure that can integrate AI support features. Which offering fits?
A business needs the operational foundation for its cloud contact center. Which product fits?
A company wants a contact-center service rather than only a customer-conversation analysis tool. Which offering fits?
A support organization evaluates a cloud-native contact-center solution for its service operation. Which offering fits?''','2.3')
item(2,'garden search automl workspace','A model catalog helps compare eligible models; search over business documents serves a different purpose.', '''A developer wants to discover supported Google, third-party, and open models for evaluation. Which capability fits?
A team needs a catalog of eligible model options rather than an internal document search service. Which offering fits?
A business wants to compare available models before building its application. Which Agent Platform capability fits?
A solution team needs to explore model choices and their terms. Which capability fits?
A leader asks where developers can discover supported foundation-model options on the platform. Which offering fits?
A project needs model discovery rather than automated training of a new task model. Which capability fits?''','2.4')
item(2,'automl garden search workspace','A reduced-code model-training workflow is different from simply browsing existing models.', '''A team has a suitable labeled-data task and wants reduced manual model-development effort. Which capability should it evaluate?
A business needs to train a supported predictive model with less custom modeling code. Which Agent Platform feature fits?
A company wants automated assistance for a suitable model-training task rather than only a model catalog. Which offering fits?
A department has an appropriate dataset and wants a lower-effort supported ML training approach. Which capability fits?
A solution team needs automated model development for an eligible task. Which Agent Platform feature fits?
A leader distinguishes selecting a pretrained model from training a suitable model with reduced technical effort. Which capability serves the latter?''','2.4')
item(2,'customagents gems workspace garden','A purpose-specific business agent needs integrated models, tools, knowledge, and controls rather than only reusable personal instructions.', '''A business needs an agent that consults approved knowledge and invokes authorized business tools. Which development approach fits?
A company wants a custom task-oriented assistant integrated with its systems and controls. Which platform approach fits?
A team needs a production business agent with approved actions rather than only a personal chat preset. Which approach fits?
An enterprise plans a goal-directed workflow combining model reasoning and controlled external operations. Which approach fits?
A department needs a custom agent tied to its knowledge and permitted processes. Which development approach fits?
A business wants a specialized tool-using agent governed by its application policies. Which platform approach fits?''','2.4')
item(2,'ragapi train automl gems','RAG APIs support custom retrieval integration without implying that facts are permanently trained into the model.', '''A developer needs application-specific retrieval and evidence injection rather than a complete prebuilt search experience. Which capability fits?
A team wants API building blocks for a custom RAG workflow. Which approach fits?
An application needs to integrate approved external evidence through a retrieval API. Which platform capability fits?
A business has custom retrieval requirements that go beyond adopting a standard search interface. Which approach fits?
A developer wants controlled retrieval integration while keeping the same underlying model weights. Which capability fits?
A solution team needs programmatic RAG components for its own application design. Which approach fits?''','2.4')
item(2,'agentstudio aistudio gems notebook','The retrieved guide positions Agent Studio for cloud production-oriented application development; prototyping alone does not prove production readiness.', '''A team is moving beyond a quick model experiment toward production-oriented cloud AI application development. Which studio does the retrieved exam material position for that purpose?
A business needs the platform-oriented studio rather than a rapid Gemini API playground for its production application work. Which option fits?
A leader distinguishes a quick experiment from production-oriented AI application development at scale. Which studio serves the latter in the guide?
A team wants the cloud platform development environment described for production AI applications. Which studio fits?
An organization plans production-oriented AI application work rather than only testing prompts in a prototype tool. Which studio fits?
A solution team needs the production-oriented studio identified by the retrieved guide. Which option fits?''','2.5')
item(2,'aistudio agentstudio automl ccaas','Google AI Studio is positioned for rapid prototyping with supported Gemini capabilities, not a guarantee of deployment readiness.', '''A developer wants to quickly try Gemini prompts and supported API capabilities before planning production. Which studio fits?
A team needs a rapid experimentation environment for a Gemini proof of concept. Which option fits?
A business wants to test model interactions quickly before committing to its enterprise application design. Which studio fits?
A developer needs a simple starting point for experimenting with supported Gemini API behavior. Which tool fits?
A prototype project wants to explore prompts and model responses rather than operate a complete contact center. Which tool fits?
A leader asks which studio is positioned for quick AI prototyping in the retrieved guide. Which option fits?''','2.5')
item(2,'storage database search automl','Files and datasets are objects; object storage is not automatically a business-search index or transactional database.', '''An agent workflow needs an object store for approved source documents and media files. Which service fits?
A company wants to store large collections of files used by an AI application. Which Google Cloud service fits?
A data team needs object storage rather than a conversational product. Which service fits?
A business must retain approved source files before processing them with AI. Which storage service fits?
An application needs durable object storage for datasets and artifacts. Which service fits?
A team wants a place to store files, not a model-training feature or a complete search solution. Which service fits?''','2.5')
item(2,'run storage garden automl','Managed hosting for compatible containerized services fits Cloud Run rather than object storage or a model catalog.', '''A team needs to host a compatible containerized service used by an AI application. Which Google Cloud service fits?
A custom agent backend is packaged as a supported container and needs managed hosting. Which service fits?
A business wants a managed runtime for its compatible container-based tool API. Which service fits?
A developer needs to deploy a supported containerized application around model calls. Which service fits?
An AI workflow includes a containerized business service that needs managed operation. Which Google Cloud service fits?
A project wants managed application hosting for a compatible container rather than model discovery. Which service fits?''','2.5')
item(2,'functions storage garden automl','A suitable bounded event-driven tool can be implemented with a function service rather than a model catalog.', '''An agent needs a suitable event-driven function that performs one approved integration task. Which capability fits?
A team wants a small supported function triggered by an event in its AI workflow. Which service category fits?
An application needs an event-driven tool implementation rather than a complete ML training platform. Which capability fits?
A developer packages a bounded supported operation as a cloud function. Which offering fits?
A business wants to trigger a suitable function when a new source object arrives. Which capability fits?
An AI workflow needs a small event-driven action under the service's execution limits. Which offering fits?''','2.5')
item(2,'stt tts translation nlp','The input is spoken audio and the required output is text.', '''A contact center needs transcripts of recorded customer calls. Which API fits?
A business wants written text from spoken interview audio. Which service fits?
A training team needs transcripts of approved lecture recordings. Which API fits?
An assistant needs speech converted into text before analysis. Which capability fits?
A media company wants to transcribe supported spoken content. Which API fits?
A workflow starts with audio and needs a textual transcript. Which service fits?''','2.5')
item(2,'tts stt translation nlp','The input is text and the required output is synthesized speech.', '''A learning app needs spoken narration from approved written lessons. Which API fits?
A customer experience should read a text response aloud using synthesized speech. Which capability fits?
A business wants to create supported spoken output from written content. Which API fits?
An accessibility feature converts a written explanation into audio. Which service fits?
A voice interface needs generated speech from text. Which API fits?
A team wants to narrate existing instructions without recording a human speaker. Which capability fits?''','2.5')
item(2,'translation nlp stt vision','Language conversion of text is translation rather than sentiment analysis or audio transcription.', '''A retailer needs product text translated into supported customer languages. Which API fits?
A business wants written messages converted between supported languages. Which service fits?
An application must translate text rather than classify its sentiment. Which capability fits?
A company needs multilingual versions of short written notices. Which API fits?
A support workflow needs text language conversion. Which service fits?
A team wants to translate existing written content for an international audience. Which API fits?''','2.5')
item(2,'doctranslation translation docai vision','The requirement includes translating a supported formatted document while preserving its layout as appropriate.', '''A company needs a supported formatted report translated while keeping its layout. Which capability fits most directly?
A legal operations team needs language conversion of a supported document with layout preservation. Which offering fits?
A business wants translated versions of supported formatted files rather than plain text snippets alone. Which capability fits?
A workflow must translate a supported document and preserve its formatting where possible. Which service capability fits?
A publisher needs a supported formatted document translated with layout retained. Which option fits?
A team needs document-level translation that considers supported file structure and layout. Which capability fits?''','2.5')
item(2,'docai vision translation nlp','Structured extraction from documents fits Document AI; general image analysis and language conversion are different tasks.', '''A finance team needs structured fields from supported invoices. Which service fits?
An insurer wants to extract form data from supported claim documents. Which capability fits?
A company needs document-processing automation to capture supported fields. Which offering fits?
A procurement workflow must turn invoice content into structured business data. Which service fits?
A team wants specialized document extraction rather than only general image labels. Which capability fits?
A business needs to process supported forms and extract useful structured information. Which service fits?''','2.5')
item(2,'vision imagen video nlp','The task analyzes existing image content rather than creating a new image or analyzing a video sequence.', '''An archive needs labels for objects and landmarks in existing photos. Which API fits?
A business wants supported image analysis rather than generation of new pictures. Which capability fits?
A media team needs annotations describing content in photographs. Which API fits?
An application must analyze supported visual features in uploaded images. Which service fits?
A company wants to identify supported objects or text in existing image files. Which API fits?
A workflow needs general image-content analysis instead of a specialist document form processor. Which capability fits?''','2.5')
item(2,'video veo vision nlp','Analyzing existing video differs from generating a new video sequence.', '''A media company wants annotations from existing supported video clips. Which API fits?
A business needs to analyze video content rather than generate new clips. Which service fits?
A library wants searchable information derived from supported recorded video. Which capability fits?
A team needs video-content analysis for its existing media collection. Which API fits?
An application must extract supported annotations from uploaded videos. Which offering fits?
A company needs to understand existing video content rather than create a new sequence. Which API fits?''','2.5')
item(2,'nlp translation stt tts','Sentiment and entity analysis operate on existing text rather than translating or synthesizing it.', '''A business wants sentiment and entity information from written reviews. Which API fits?
A support team needs to identify entities in existing text transcripts. Which service fits?
An analyst wants supported sentiment analysis of customer comments. Which API fits?
A company needs insights from unstructured text rather than conversion to another language. Which service fits?
A workflow classifies existing text and extracts supported entities. Which capability fits?
A team wants to analyze the meaning and sentiment of written feedback. Which API fits?''','2.5')
item(2,'database gemini garden imagen','Live structured business facts should come from an authorized authoritative source rather than model recollection.', '''An assistant needs the current balance of a customer's account. Which information approach fits?
A service agent must confirm an order's latest status from approved records. Which tool source fits?
A business requires the exact current inventory count rather than a plausible answer. Which approach fits?
A customer asks for a live reservation detail that must respect access permissions. Which source approach fits?
An agent needs authoritative current structured records for a permitted account. Which tool approach fits?
A workflow must retrieve a verified live business value instead of guessing from pretrained knowledge. Which approach fits?''','2.5')
item(2,'tool prompt geminiapp garden','A real-world operation must be performed and verified by authorized application tooling; generating a claim does not execute it.', '''An assistant must actually create an approved support ticket, not merely say it did. Which capability is required?
A customer agent needs to perform an authorized booking operation through an external API. Which approach fits?
A workflow needs an approved action executed in a business system. Which capability fits?
A chatbot generates a cancellation confirmation but no system record changes. Which missing capability should perform the action?
A business agent must interact with an external service to complete a permitted task. Which mechanism fits?
A model can draft a request, but the application must perform the approved external operation. Which capability fits?''','2.5')
term('hallucination','Hallucination','Is generated content that appears plausible but is factually wrong or unsupported by the available evidence.')
term('cutoff','Pretraining knowledge cutoff','Limits what facts could be learned during training; the model does not inherently know later events without additional evidence or tools.')
term('rag','Retrieval-augmented generation (RAG)','Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights.')
term('tune','Fine-tuning','Updates model parameters using suitable task-specific training data; it is not automatically the best way to supply frequently changing facts.')
term('human','Human-in-the-loop review','Uses qualified people to verify, approve, correct, or escalate outputs, especially where consequences are significant.')
term('zero','Zero-shot prompting','Gives task instructions without a worked example in the prompt.')
term('one','One-shot prompting','Provides one worked demonstration of the desired task behavior in the prompt.')
term('few','Few-shot prompting','Provides several worked demonstrations of the desired input-output behavior in the prompt.')
term('role','Role prompting','Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority.')
term('chaining','Prompt chaining','Uses linked prompt steps or exchanges so one stage informs later stages of a larger task.')
term('cot','Chain-of-thought-style prompting','Uses intermediate-step demonstrations or structured problem-solving guidance; it is not a guarantee of correctness or access to private internal reasoning.')
term('react','ReAct-style reasoning and action','Combines deciding a next step with permitted external actions and observations in a controlled loop.')
term('firstparty','Ground with authorized first-party enterprise data','Uses approved organizational evidence for private business facts, with appropriate access controls.')
term('thirdparty','Ground with a licensed or approved third-party source','Uses permitted information from an external provider when that source is authoritative for the requirement.')
term('world','Ground with relevant public world information','Uses appropriate public evidence, such as supported Search grounding, rather than assuming private records are publicly available.')
term('temperature','Adjust temperature to control sampling variability','Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness.')
term('topp','Adjust top-p nucleus sampling','Restricts the candidate token set using cumulative probability mass rather than a fixed response length.')
term('length','Set an appropriate maximum output length','Caps generated output tokens within supported limits; too low a cap can truncate an answer.')
term('context','Context window','Bounds the information a model can consider within a request according to model-specific limits.')
term('token','Token','Is a model-dependent input or output unit that may represent a word fragment; token count is not always word count.')
term('monitor','Continuously evaluate, version, and monitor the solution','Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance.')
term('softprompt','Prompt tuning','Learns task-specific prompt representations while keeping base model weights frozen in supported approaches; it differs from manually rewriting prompt text.')
term('safety','Configure and test appropriate safety controls','Can reduce supported harmful content but does not guarantee factual accuracy, authorization, or complete risk elimination.')
term('priority','Prioritize measurable business value with feasible data and manageable risk','Selects use cases using value, readiness, constraints, and consequences rather than novelty alone.')
term('pilot','Start with a bounded pilot and defined success criteria','Tests value and risk on a controlled scope before broad expansion.')
term('roi','Evaluate total benefits against total implementation and operating costs','Accounts for integration, model use, review, training, and maintenance rather than relying only on the price of a token.')
term('kpi','Define outcome-focused baseline and success metrics','Measures the business goal, such as verified resolution or handling time, alongside quality and safety measures.')
term('adoption','Plan training, workflow change, feedback, and ongoing support','Addresses the people and process changes required for useful adoption rather than treating deployment as automatic acceptance.')
term('stakeholders','Align business, technical, security, and affected-user stakeholders','Connects goals, feasibility, controls, and user needs before decisions become difficult to reverse.')
term('saif','Google Secure AI Framework (SAIF)','Provides a framework for securing AI systems and addressing AI-specific risks across their lifecycle; it is not a guarantee or an automatic certification.')
term('iam','Identity and Access Management (IAM)','Controls which principals may perform supported actions on resources through roles and policies.')
term('scc','Security Command Center','Helps identify and manage supported security findings and posture information; it is not a source-document quality evaluator.')
term('securelife','Apply security controls throughout the AI lifecycle','Addresses source data, development, deployment, access, monitoring, and updates rather than only the launch endpoint.')
term('transparent','Disclose AI use, relevant limits, and review pathways','Helps stakeholders understand the role of the system and limitations rather than treating generated answers as unquestionable authority.')
term('privacy','Minimize and protect personal data for the approved purpose','Limits unnecessary collection, use, retention, and disclosure according to applicable obligations.')
term('pseudonym','Pseudonymization','Replaces direct identifiers with aliases while a linkage or re-identification route may remain; it is not the same as irreversible anonymity.')
term('anonym','Anonymization','Aims to prevent identification under the relevant standard; simply removing names does not automatically achieve it.')
term('fair','Evaluate relevant subgroups and address inappropriate disparities','Checks uneven outcomes and representation with appropriate data and review; overall accuracy can conceal harmful differences.')
term('accountable','Assign decision ownership, explanations, and escalation responsibilities','Makes people or teams answerable for AI impacts and supports review of consequential outcomes.')

item(3,'hallucination cutoff context token','Fluency and confidence do not prove support or truth; unsupported generated facts are hallucinations.', '''An assistant confidently invents a policy clause absent from approved sources. Which limitation is this?
A model gives a convincing citation to a report that does not exist. Which failure is illustrated?
A generated answer adds a false product feature not supported by the catalog. Which limitation fits?
A summary includes an event that never occurred in the supplied record. Which failure is this?
A chatbot fabricates an accurate-looking price that has no source. Which limitation is this?
A model presents an invented statistic as established fact. Which failure does this illustrate?''','3.1')
item(3,'cutoff hallucination context token','A model cannot inherently know facts that occurred after its training knowledge without additional information.', '''An ungrounded model cannot reliably answer about a product launched after its training data ended. Which limitation explains this?
A team assumes pretrained knowledge includes yesterday's announcement. Which model limitation should it consider?
An assistant lacks facts about a recent event absent from its training and supplied context. Which limitation matters?
A leader expects a static pretrained model to automatically know every new regulation. Which constraint should be explained?
A model's built-in knowledge does not include a newly published policy. Which limitation is relevant?
An application relies only on pretrained weights for facts created after training. Which limitation should the team address?''','3.1')
item(3,'rag tune softprompt largest','Frequently changing evidence can be supplied through retrieval rather than repeatedly training facts into model weights.', '''An assistant needs current internal policy facts without retraining the base model. Which approach fits?
A retailer wants answers grounded in its frequently changing approved catalog. Which architecture fits?
A business needs a model to consult documents supplied as evidence at query time. Which approach fits?
A help assistant should use updated manuals while leaving learned weights unchanged. Which technique fits?
An application must retrieve approved information and add it to the prompt before answering. Which method is this?
A company wants grounded answers from external source content without inherently updating model parameters. Which approach fits?''','3.3')
item(3,'tune rag prompt temperature','Changing learned task behavior with an additional supported training job is fine-tuning, not only adding retrieval context.', '''A team updates a supported model's weights using curated task examples to change persistent behavior. Which approach is this?
A business adapts a base model through additional training on approved task demonstrations. Which method fits?
An existing model needs learned specialized output behavior and parameters are updated. Which customization approach is this?
A supported training process modifies model parameters for a narrow task. Which method fits?
A project changes the base model's learned behavior using quality task-specific data. Which approach is this?
A company runs additional training on a pretrained model rather than only rewriting instructions. Which adaptation method fits?''','3.1')
item(3,'human temperature largest length','Consequential or uncertain outputs require suitable qualified review; generation settings cannot provide accountability alone.', '''A generated recommendation could significantly affect a customer's access to a service. Which oversight control is appropriate?
An assistant is uncertain about a high-impact policy decision. Which process should handle the case?
A legal draft needs expert verification before use. Which output-improvement practice fits?
A healthcare information workflow produces an ambiguous consequential answer. Which oversight approach fits?
A business wants qualified approval before acting on a risky generated recommendation. Which process fits?
A model output is outside the application's approved scope and may cause harm. Which escalation approach fits?''','3.1')
item(3,'zero one few tune','Instructions without demonstrations are zero-shot prompting; no model-weight change is implied.', '''A prompt asks for a three-bullet summary but gives no worked example. Which prompting technique is this?
A user requests sentiment classification using instructions alone. Which technique fits?
A translation prompt contains the task and input but no sample translation. Which prompting approach is this?
An assistant receives extraction instructions with no demonstrations. Which technique fits?
A model is asked to rewrite text without an example of the desired result. Which prompting style is this?
A prompt specifies the task and format without showing any completed cases. Which technique fits?''','3.2')
item(3,'one zero few tune','One worked input-output example in the request is one-shot prompting, not training.', '''A prompt shows exactly one sample support reply before asking for a new reply. Which technique is this?
A user provides one worked extraction example with the task instructions. Which prompting approach fits?
An assistant is shown one correct classification before processing the actual input. Which technique is this?
A formatting prompt contains one completed conversion as a demonstration. Which technique fits?
A model receives a single example of the desired output style inside the prompt. Which prompting approach is this?
A team adds one input-output demonstration without updating weights. Which prompting technique fits?''','3.2')
item(3,'few one zero tune','Several demonstrations provided in the prompt constitute few-shot prompting rather than weight training.', '''A prompt includes four sample reviews and their correct sentiment labels. Which technique is this?
An assistant receives several worked input-output cases before a new task. Which prompting approach fits?
A model is shown three approved answers as demonstrations inside its request. Which technique is this?
A user includes a handful of examples to illustrate a desired format. Which prompting approach fits?
A classification prompt demonstrates several boundary cases before asking for a result. Which technique is this?
A team adds multiple demonstrations to the prompt while keeping model weights unchanged. Which approach fits?''','3.2')
item(3,'role few tune rag','A requested role guides perspective and style but is not an authorization mechanism or proof of competence.', '''A prompt says act as a concise technical editor. Which prompting technique is this?
A user asks a model to respond as a patient tutor for beginners. Which technique fits?
An assistant is instructed to take the perspective of a careful customer-service representative. Which approach fits?
A prompt sets a formal reviewer persona to shape the response. Which technique is this?
A model is assigned the function of a briefing writer with a specific tone. Which prompting approach fits?
A team specifies an assistant's role and communication perspective in instructions. Which technique fits?''','3.2')
item(3,'chaining few tune length','Linked prompt stages use one result to inform the next without inherently changing weights.', '''A workflow first extracts facts, then uses them in another prompt to draft a summary. Which technique fits?
A user builds an answer through linked requests where each stage informs the next. Which approach is this?
An assistant completes a multi-part task using connected prompts rather than one overloaded request. Which technique fits?
A team separates outlining, drafting, and reviewing into linked model interactions. Which prompting approach fits?
A workflow passes one prompt's output into a later prompt for refinement. Which technique is this?
A business develops a result through a sequence of contextual follow-up prompts. Which approach fits?''','3.2')
item(3,'cot react role temperature','Intermediate-step guidance can structure problem solving, but a plausible rationale is not proof that the answer is correct.', '''A prompt demonstrates intermediate problem-solving steps before the final answer. Which prompting approach fits?
A team provides worked examples that show a structured reasoning sequence. Which technique fits?
A model receives examples with intermediate calculations to guide a similar task. Which approach is this?
A prompt encourages a structured problem-solving process rather than only a final response format. Which technique fits?
An educator supplies intermediate-step demonstrations for a multi-stage reasoning task. Which prompting approach fits?
A team uses stepwise worked examples to improve a complex response. Which technique is relevant?''','3.2')
item(3,'react cot role temperature','Alternating decision steps with permitted external actions and observations is characteristic of ReAct-style behavior.', '''An assistant decides what information is missing, calls a permitted tool, observes the result, and continues. Which approach fits?
A model-guided workflow alternates reasoning about next steps with authorized external actions. Which technique fits?
An agent inspects tool feedback before choosing its next permitted operation. Which approach is this?
A task loop combines decision making, action, and observation rather than text-only elaboration. Which technique fits?
An assistant uses an external lookup, reviews the returned evidence, and decides whether another action is needed. Which approach fits?
A workflow integrates reasoning with controlled tool use toward a task goal. Which prompting or agent approach fits?''','3.2')
item(3,'firstparty thirdparty world temperature','Private company facts need authorized enterprise evidence, not merely public web content or sampling changes.', '''An assistant must answer from the company's confidential approved policies. Which grounding source category fits?
A business needs answers about its internal operating procedures. Which grounding approach fits?
A user asks for permitted private project facts unavailable on the public web. Which evidence source fits?
A company wants grounded answers from its own controlled knowledge repository. Which source category fits?
A support assistant should cite approved internal manuals. Which grounding source fits?
An application needs private enterprise facts while preserving source access controls. Which grounding approach fits?''','3.3')
item(3,'thirdparty firstparty world tune','An approved external authoritative provider is a third-party evidence source, with licensing and freshness obligations.', '''A business needs licensed market data from an approved external provider. Which grounding source category fits?
An assistant must use a contracted industry research feed rather than internal records or unverified public posts. Which source fits?
A company relies on an approved specialist data vendor for its answer evidence. Which grounding category fits?
A workflow needs authoritative external benchmark information under a data license. Which source category fits?
A leader distinguishes company-owned knowledge from a permitted commercial information feed. Which grounding category is the feed?
An application must ground answers using an approved third-party financial dataset. Which source approach fits?''','3.3')
item(3,'world firstparty thirdparty tune','Public-world grounding fits public evidence requirements, but freshness and source support still need checking.', '''An assistant needs relevant public sources for a current general-information question. Which grounding category fits?
A user asks about a public announcement rather than company-private documents. Which evidence category fits?
A business wants supported Search grounding for broadly available public facts. Which source category fits?
An answer should use relevant public world information, not a confidential database. Which grounding approach fits?
A model needs public evidence about recent widely reported events. Which source category fits?
A company distinguishes its private knowledge base from general public web evidence. Which grounding category describes the latter?''','3.3')
item(3,'temperature length context token','Temperature adjusts sampling variation; lower variability is not a guarantee of truth.', '''A creative team wants more varied wording across generated drafts. Which sampling setting is most directly relevant?
A support assistant needs more focused token sampling rather than highly variable phrasing. Which setting can be lowered?
A leader asks which parameter commonly affects the randomness of generated continuations. Which setting fits?
A team experiments with how diverse repeated model responses are. Which sampling setting fits?
An application wants to tune response variation without retraining the model. Which setting is relevant?
A model's wording is too unpredictable and the team wants to adjust sampling randomness. Which parameter fits?''','3.3')
item(3,'topp temperature length context','Top-p changes a cumulative-probability candidate set rather than capping how long the response can be.', '''A sampler keeps candidate tokens until a chosen cumulative probability is reached. Which setting is this?
A model uses nucleus sampling rather than a fixed output-length cap. Which parameter fits?
A developer adjusts the probability mass of the next-token candidate pool. Which setting is this?
A generation configuration sets a cumulative token-probability threshold. Which sampling approach fits?
A team wants to control the nucleus of likely next tokens used during sampling. Which parameter fits?
A model dynamically chooses a candidate token set using total probability mass. Which setting is this?''','3.3')
item(3,'length temperature topp context','An output token cap controls generated length, not the total capacity of the request context or factual correctness.', '''An application needs an upper bound on the size of each generated answer. Which setting directly fits?
A model response is cut off at its configured generation limit. Which output control should be checked?
A team wants to cap generated token use without changing sampling randomness. Which setting fits?
A business assistant returns overly long responses and needs an output ceiling. Which control fits?
A developer needs a maximum generated response size subject to model limits. Which setting fits?
A cost policy requires a limit on output token count per call. Which control is most direct?''','3.3')
item(3,'monitor largest cheapest biggerdata','Quality and risk can change after launch, so updates and version transitions require continued observation and evaluation.', '''A team assumes an AI model needs no review after deployment. Which lifecycle practice should replace this assumption?
A provider model update changes response behavior unexpectedly. Which ongoing management practice fits?
An assistant's quality declines as business inputs change. Which operational approach fits?
A project needs to track model versions, security updates, and quality over time. Which practice fits?
A business wants to detect regressions rather than rely solely on its original pilot result. Which practice fits?
A team must preserve reliable AI behavior as services and data evolve. Which ongoing approach fits?''','3.1')
item(3,'softprompt prompt tune rag','Learned prompt representations with frozen base weights distinguish prompt tuning from manual prompt engineering and full parameter adaptation.', '''A supported method learns task-specific prompt representations while keeping base model weights frozen. Which approach is this?
A team distinguishes learned soft prompts from manually rewritten instructions. Which customization method refers to the learned prompts?
A model adaptation process optimizes prompt representations without changing the base model parameters. Which method fits?
A training technique learns prompt-side vectors for a supported task while freezing the base model. Which approach is this?
A leader asks how prompt tuning differs from ordinary prompt wording changes. Which option names the learned-representation method?
A supported customization uses learned prompt parameters rather than updating the full model. Which approach fits?''','3.1')

item(4,'priority largest cheapest biggerdata','A useful first use case must connect value with feasibility, data readiness, and manageable consequences.', '''A company has many AI ideas and limited resources. Which principle should guide its first use-case selection?
A leader is drawn to the most impressive demo but has no evidence of business need. Which prioritization approach fits?
An organization must compare a low-risk drafting pilot with a high-risk autonomous decision project. Which selection principle fits?
A business wants to avoid adopting generative AI solely because competitors do. Which use-case strategy fits?
A department must choose among opportunities with different data readiness and impact. Which principle fits?
A company wants a practical AI initiative rather than novelty without outcomes. Which prioritization approach fits?''','4.1')
item(4,'pilot deploy largest biggerdata','A controlled pilot tests assumptions and outcomes before broad rollout; deployment alone is not validation.', '''A business has an uncertain AI opportunity and wants evidence before organization-wide rollout. Which approach fits?
A leader wants to test a use case with a small group and explicit success measures. Which implementation strategy fits?
A company needs to validate data readiness and value on a limited scope first. Which approach fits?
An AI initiative has untested risks and assumptions. Which first implementation strategy is most appropriate?
A department wants evidence of usefulness before scaling a new assistant. Which rollout approach fits?
A business wants to learn from a controlled trial rather than commit every team immediately. Which strategy fits?''','4.1')
item(4,'roi cheapest token temperature','Financial value depends on total benefits and full lifecycle costs, not token price alone.', '''An AI assistant saves staff time but requires integration, review, and model fees. Which financial assessment fits?
A leader compares two solutions with different operating and implementation costs. Which value assessment fits?
A cheap model needs so much correction that the solution becomes expensive. Which financial approach captures this?
A business must justify AI spending against measurable savings and ongoing costs. Which assessment fits?
A project has licensing, training, maintenance, and inference costs. Which assessment should include them?
A company wants to measure whether the benefits of AI exceed all relevant expenses. Which financial approach fits?''','4.1')
item(4,'kpi token largest cheapest','Outcome baselines and quality constraints determine whether an initiative helps the business rather than merely generating more text.', '''A support pilot must prove that it improves verified resolution rather than just producing more responses. Which measurement approach fits?
A leader wants evidence of time saved without unacceptable quality loss. Which metric-planning practice fits?
A business launches an AI pilot without a baseline for its goal. Which measurement step is missing?
A team proposes counting generated words as its only success measure. Which alternative measurement practice fits?
A company needs to know whether its AI application improves an actual workflow. Which measurement approach fits?
A leader wants defined success criteria and comparison with pre-AI performance. Which practice fits?''','4.1')
item(4,'adoption deploy largest biggerdata','Useful adoption requires user capability and process change, not merely making software available.', '''An AI assistant is technically available but employees do not use it effectively. Which adoption action should be prioritized?
A team deploys an AI tool without training or workflow guidance and sees little value. Which strategy fits?
A company needs employees to understand when to use AI and when to verify its output. Which adoption practice fits?
A leader wants sustained use rather than a one-week launch announcement. Which organizational approach fits?
An enterprise must integrate AI into everyday work with support and feedback. Which strategy fits?
A business has resistance and confusion around a new AI process. Which adoption approach should address this?''','4.1')
item(4,'stakeholders largest cheapest train','Cross-functional alignment joins business goals, feasibility, controls, and the needs of affected users.', '''An AI project meets technical goals but fails the business and security review. Which planning practice was missing?
A leader wants early agreement between operations, engineers, compliance, and end users. Which collaboration approach fits?
A pilot creates workflow problems because affected employees were never consulted. Which planning practice fits?
A company needs to connect business value with technical and governance requirements. Which approach fits?
A project selects a model before discussing data restrictions with security and legal teams. Which process improvement fits?
A business wants shared ownership of an AI initiative across relevant functions. Which planning practice fits?''','4.1')
item(4,'saif iam scc safety','SAIF is a security framework for AI lifecycle risks; individual tools implement parts of a security program.', '''A leader needs Google's framework for addressing AI-specific security risks across the lifecycle. Which option fits?
A business wants a structured approach to securing AI systems rather than relying on one filter. Which Google framework fits?
An organization is planning an AI security program and needs the relevant Google framework. Which option fits?
A team asks which Google initiative guides protection of AI systems from attacks and misuse. Which framework fits?
A security leader wants an AI-focused framework, not just a role-assignment tool. Which option fits?
A company evaluates Google's structured guidance for secure AI development and operation. Which framework fits?''','4.2')
item(4,'iam scc safety quality','Authorization policies control permitted resource actions; content filtering and model quality do not replace access enforcement.', '''An AI application should access only the approved resources required by its role. Which Google Cloud capability controls this?
A company wants to restrict who can call supported services and read project data. Which control fits?
A service account has more resource permissions than its task requires. Which capability should narrow them?
A platform needs identity-based authorization for its AI resources. Which service fits?
A leader wants enforced permissions rather than merely telling the model to behave. Which Google Cloud control fits?
An organization must define which principals may perform supported resource operations. Which capability fits?''','4.2')
item(4,'scc iam quality prompt','Security findings and posture visibility are distinct from resource-role assignment or prompt improvement.', '''A security team wants visibility into supported cloud security findings affecting its AI environment. Which service fits?
A leader needs a central view of supported security posture issues rather than a model evaluation score. Which offering fits?
An organization wants to identify and manage relevant cloud security findings. Which Google Cloud service fits?
A security operation needs supported risk and posture information for its environment. Which capability fits?
A company needs security-finding visibility across its cloud environment used by AI. Which service fits?
A platform team wants to review supported security findings rather than manually infer them from model answers. Which offering fits?''','4.2')
item(4,'securelife safety deploy largest','AI security spans data, development, access, serving, monitoring, and updates instead of appearing only at launch.', '''A team secures only its public endpoint but ignores training-data access and maintenance. Which lifecycle strategy fits?
A leader wants controls for source data, development, production, and ongoing monitoring. Which security approach fits?
An AI project treats security as a final review after implementation. Which strategy should replace that approach?
A company needs protection from misuse throughout the model and application lifecycle. Which approach fits?
A business considers security patches and data governance beyond deployment day. Which strategy fits?
An organization wants continuous AI security rather than one launch-time filter. Which lifecycle approach fits?''','4.2')
item(4,'transparent accountable safety temperature','Transparency helps people understand AI involvement and limits; it does not itself guarantee correctness.', '''Users cannot tell that recommendations are generated or how to request review. Which responsible AI practice should be improved?
A company presents AI output as unquestionable expert advice without communicating limits. Which practice fits?
An assistant should tell users when AI is involved and what needs verification. Which principle fits?
A business wants clear disclosure of AI use and relevant limitations. Which responsible practice fits?
A service needs understandable communication about the role and boundaries of its AI. Which principle fits?
A team should explain that generated responses can be wrong and offer review pathways. Which practice fits?''','4.3')
item(4,'privacy biggerdata largest prompt','Personal information should be necessary, authorized, protected, and retained only as appropriate for its purpose.', '''A pilot collects every customer detail even though only a few fields are needed. Which responsible data practice fits?
An AI workflow stores personal prompts indefinitely without a defined need. Which privacy approach should guide redesign?
A business wants to reduce unnecessary exposure of employee information in AI processing. Which practice fits?
A team plans to send identifiable customer data to an AI tool without checking necessity or permissions. Which principle fits?
A company needs an approved purpose and protections for personal data used in an AI application. Which practice fits?
An assistant uses more personal records than required for its task. Which responsible approach should be applied?''','4.3')
item(4,'pseudonym anonym structured unlabeled','A retained linkage can allow re-identification, so replacing names with codes does not establish anonymization.', '''A dataset replaces names with codes but keeps a separate lookup table. Which privacy technique is this?
A company can reconnect coded customer records to identities through a retained key. Which technique fits?
An AI dataset uses aliases while a mapping still identifies the original people. Which technique is this?
A leader claims coded IDs make a dataset anonymous even though linkage remains. Which more accurate term fits?
A data team removes direct names but stores a re-identification mapping securely. Which process is this?
A project substitutes identifiers with tokens that can be linked back using another file. Which privacy technique fits?''','4.3')
item(4,'fair quality largest cheapest','Aggregate performance can hide inappropriate disparities; subgroup analysis and representation review are needed.', '''An assistant works well overall but performs much worse for one relevant user group. Which responsible AI evaluation fits?
A model's errors disproportionately affect an underrepresented population. Which review should the team prioritize?
A voice experience has uneven performance across accents. Which responsible AI assessment fits?
A hiring-related assistant has different harmful error rates across relevant groups. Which practice fits?
A leader sees a strong average score but receives reports of systematic exclusion. Which review is appropriate?
An AI service's benefits and mistakes are unevenly distributed across intended users. Which responsible practice fits?''','4.3')
item(4,'accountable transparent temperature largest','Consequential AI decisions need named owners, meaningful review, and appropriate explanations rather than responsibility assigned to the model itself.', '''A company cannot identify who must investigate a harmful AI recommendation. Which governance practice is missing?
A consequential AI workflow needs clear ownership and escalation when users challenge outcomes. Which practice fits?
A leader wants people to remain answerable for AI impacts rather than blame the model. Which governance approach fits?
An organization needs a responsible team to explain and review disputed AI decisions. Which practice fits?
A business deploys an AI process without naming who approves risk and handles incidents. Which governance control fits?
A service needs clear responsibility for correcting harmful AI outcomes and providing review. Which practice fits?''','4.3')
# Additional multi-constraint cases replace selected base scenarios; totals remain 600.
def case(number,objective,question,choices,reason):
    base=ITEMS[objective-1]
    assert len(choices)==4
    keys=[]
    for n,(label,explanation) in enumerate(choices):
        key=f'case_{number}_{objective}_{n}'
        term(key,label,explanation)
        keys.append(key)
    OVERRIDES[(number,objective)]={**base,'keys':keys,'reason':reason,'prompts':[question]*6}

case(1,21,'A retailer compares two models for product descriptions. Model A has the lowest token price but requires extensive corrections; Model B costs more per call but meets the quality target with little editing. What should the leader compare before choosing?',[
 ('Total cost per acceptable business output, including review and integration','A useful comparison includes quality-adjusted effort and full operating cost, not just the API unit price.'),
 ('Only the advertised input-token price','This omits output pricing, correction work, failed attempts, and solution costs.'),
 ('Only the model parameter count','Capacity is not an independent measure of suitability for the actual task.'),
 ('Only the number of generated words','Text volume does not establish useful quality or economic value.')],
 'Choose against the real task and business outcome. A higher unit price can still result in a lower total cost per usable output.')
case(2,10,'A policy assistant retrieves conflicting documents: one is current and approved, another is an obsolete draft. The team proposes upgrading to a larger model. What should it prioritize first?',[
 ('Curate authoritative source versions and remove or clearly govern obsolete evidence','The immediate issue is contradictory source quality and status, not demonstrated lack of model capacity.'),
 ('Increase model size without changing the documents','More capacity does not establish which contradictory policy is authoritative.'),
 ('Raise temperature to make the response more decisive','Sampling variation cannot resolve source authority.'),
 ('Expand the output limit to include both contradictory instructions','More text can reproduce the conflict rather than resolve it.')],
 'Improve the source of truth and approval metadata before assuming model scale is the fix. Retrieval and final answers should reflect authoritative, permitted evidence.')
case(3,30,'A company wants an AI assistant to explain invoices conversationally, but the invoice totals must exactly follow approved arithmetic rules. Which design is MOST appropriate?',[
 ('Calculate totals in a validated deterministic component and let AI explain the verified result','This separates exact computation from open-ended explanation.'),
 ('Let an unconstrained model invent both totals and explanations','A plausible explanation does not make arithmetic authoritative.'),
 ('Generate totals repeatedly and pick the most fluent answer','Fluency is unrelated to exact calculation correctness.'),
 ('Use a higher temperature to ensure the total is unbiased','Sampling diversity does not enforce a financial formula.')],
 'Use generative AI where language flexibility adds value and deterministic code where the business requires an exact reproducible calculation.')
case(4,19,'An insurance team needs to ask questions about photographs together with claim descriptions. A text-only model meets the budget but cannot process images. What is the best next selection criterion?',[
 ('Evaluate models supporting the required modalities, then check quality and operating constraints','The required input capability is a prerequisite before optimizing among eligible models.'),
 ('Select the cheapest text-only model and assume it can infer unseen image details','A model cannot reliably interpret image content it cannot receive.'),
 ('Increase the response length of the text-only model','An output limit does not add an input modality.'),
 ('Choose solely by how many text examples were used in training','Training volume alone does not establish supported visual inputs.')],
 'Match modality to the business task, then evaluate security, quality, availability, cost, and other requirements for the eligible models.')
case(5,27,'A manufacturer needs a compatible model deployment in an environment it controls, with limited connectivity. It is willing to operate the runtime and review license terms. Which Google model family is most relevant to evaluate?',[
 ('Gemma, with a compatibility, license, and quality assessment','Open-weight deployment options are relevant to local or controlled hosting requirements.'),
 ('Veo solely because it generates videos','Video generation does not address the stated deployment and task needs.'),
 ('Imagen solely because it creates high-quality still images','Image generation is not evidence of suitability for the required local language workload.'),
 ('Any personal chatbot account, assuming it runs entirely on the factory device','A user-facing hosted account does not establish a local model deployment.')],
 'Open-weight options can provide deployment flexibility, but local operation still requires suitable hardware, license compliance, security, and measured task quality.')
case(6,11,'A company owns clean, relevant documents, but its assistant cannot access the approved repository. A sponsor suggests making all documents public. What is the best response?',[
 ('Create an authorized data connection with usable formats and appropriate access controls','The problem is controlled accessibility, not a need for public disclosure.'),
 ('Publish every document publicly so the model can find it','Public access removes confidentiality boundaries and is unnecessary for authorized enterprise retrieval.'),
 ('Buy a larger model without connecting the data','Additional capacity does not grant access to missing private evidence.'),
 ('Ask the model to reconstruct the documents from memory','The model cannot be assumed to know private source records.')],
 'Accessible data means available and usable for the authorized workflow. It does not mean available to everyone.')

case(1,39,'Employees need an AI entry point spanning several authorized internal systems, with organizational search and custom agent experiences. Their primary need is not editing emails. Which offering is the closest fit?',[
 ('Gemini Enterprise','The need is cross-source enterprise discovery and agent experiences over permitted organizational knowledge.'),
 ('Gemini for Google Workspace alone as an email-writing feature','Productivity assistance is useful but does not by itself describe the requested cross-system enterprise experience.'),
 ('Google Search without any enterprise connectors','Public search does not automatically access protected internal sources.'),
 ('Imagen','An image-generation family does not provide an enterprise knowledge and agent experience.')],
 'Distinguish organizational knowledge discovery from productivity assistance inside an individual application, and verify connectors, permissions, and actual offering capabilities.')
case(2,44,'A contact center wants humans to continue handling complex customer conversations while AI supplies relevant guidance during the interaction. Which capability should the leader prioritize?',[
 ('Agent Assist','It supports the human representative rather than replacing the interaction with automated self-service.'),
 ('Conversational Insights as the only live assistance tool','Historical conversation analysis is not the same requirement as guidance during a live case.'),
 ('Veo','Generating video is unrelated to live contact-center guidance.'),
 ('Cloud Storage alone','Storing files does not provide live response suggestions to staff.')],
 'Identify who the AI is helping and when. In this scenario it augments a human agent during work, rather than analyzing conversations afterward or automating the entire customer conversation.')
case(3,46,'A company needs a cloud contact-center operating foundation and plans to add conversational AI and agent assistance. It does not yet have the underlying contact-center service. Which offering category best addresses that foundation?',[
 ('Google Cloud Contact Center as a Service','The requirement is a contact-center platform rather than one AI feature layered onto it.'),
 ('Natural Language API alone','Text analysis is only one component and does not establish a contact-center operation.'),
 ('Agent Assist alone','Helping a representative does not by itself describe the full contact-center platform.'),
 ('Model Garden alone','Model discovery does not supply the operational contact-center foundation.')],
 'Separate the contact-center foundation from the AI capabilities that enhance it. Selection should follow the complete operating requirement.')
case(4,40,'An analyst has a bounded set of approved source files and wants summaries and source-oriented questions for personal research. There is no requirement to train a new model or run an organization-wide search deployment. Which capability is the best fit?',[
 ('Gemini Notebook source-grounded research capabilities','The need is exploration of selected source materials rather than model development or infrastructure hosting.'),
 ('Agent Platform AutoML','The scenario does not call for training a supported predictive model.'),
 ('Cloud Run alone','A runtime is not itself a research assistant over selected files.'),
 ('Model Garden alone','Discovering models is a different task from working with the supplied source collection.')],
 'Choose the simplest offering that matches the research workflow, then verify the available account features and data handling terms.')
case(5,42,'An assistant must discuss recent public news. The internal knowledge base contains no relevant source. Which addition most directly addresses the evidence gap without claiming that the base model has automatically learned the news?',[
 ('Supported grounding with relevant Google Search results','This can supply public evidence at inference time rather than assuming the facts exist in pretrained weights.'),
 ('Higher temperature without any new evidence','More sampling variety does not add current facts.'),
 ('A longer answer limit','Output size does not supply missing information.'),
 ('A private database lookup unrelated to the news','An irrelevant source does not close the evidence gap.')],
 'Use the source category appropriate to the question. Search grounding can help with public facts, but claims and source support still need evaluation.')
case(6,49,'A company wants an assistant to check authorized order records and initiate permitted support actions. A saved chat persona produces convincing text but never changes the business system. What should the team implement?',[
 ('A controlled custom agent with validated tools and business-system integration','Actual permitted actions require trusted application tooling, access checks, and verified results.'),
 ('More detailed persona wording with no external integration','Instructions alone do not execute operations in another system.'),
 ('A larger response token limit','Longer responses cannot substitute for a real tool call.'),
 ('A video-generation model','The requirement concerns business operations rather than media creation.')],
 'Distinguish a conversational preset from an integrated tool-using system. The model can propose an action; trusted application code must authorize and perform it.')

case(1,68,'A benefits assistant must use policies updated weekly. Its output format is already acceptable, but its built-in facts become stale. Which first improvement is the most appropriate?',[
 ('Retrieve approved current policies and ground answers in them','The need is fresh evidence, not necessarily a change in learned response style.'),
 ('Fine-tune only once and assume all future policy changes are covered','A one-time training job does not add facts created afterward.'),
 ('Increase temperature to discover new policies','Sampling cannot create reliable evidence of an unpublished-to-model fact.'),
 ('Remove source references to avoid conflicting information','Hiding evidence weakens traceability and does not correct stale facts.')],
 'Match the remedy to the limitation. Retrieval addresses changing knowledge; fine-tuning may address persistent behavior when supported and justified.')
case(2,81,'A team lowers temperature and observes more consistent wording. It now proposes eliminating factual review because the answers repeat reliably. What is the best response?',[
 ('Retain grounding and appropriate verification because consistency does not prove truth','Focused sampling can repeatedly produce the same incorrect answer.'),
 ('Accept the proposal because low temperature guarantees factual correctness','No sampling setting establishes truth.'),
 ('Remove the data source because repeated text is sufficient evidence','Consistency is not an authoritative source.'),
 ('Raise temperature to convert repeated facts into verified ones','More variation also does not verify a claim.')],
 'Sampling controls affect generated behavior, not the truth of the underlying evidence. Grounding and risk-appropriate review remain relevant.')
case(3,73,'A support assistant repeatedly misformats a small set of complex request types. The team has several approved input-output demonstrations and wants a fast experiment without a training job. Which change is the best starting point?',[
 ('Add the approved demonstrations as few-shot examples in the prompt','Examples can demonstrate the desired behavior immediately while keeping learned weights unchanged.'),
 ('Run a new pretraining project before any prompt experiment','This is far more effort than the stated first experiment requires.'),
 ('Use a longer context window without adding instructions or examples','Capacity alone does not explain the required formatting behavior.'),
 ('Remove all task guidance to avoid biasing the response','Removing guidance does not demonstrate the approved behavior.')],
 'Try a proportionate low-effort intervention before undertaking model training. Evaluate the prompt change on held-out realistic cases rather than only the demonstrations.')
case(4,84,'A provider releases a new model version and a pilot reports better average answers. Some sensitive workflow cases have not been retested. What should the leader do before broad adoption?',[
 ('Run representative quality and safety regression checks and retain a controlled version plan','An average improvement does not establish that critical behaviors remain acceptable.'),
 ('Upgrade every production workflow immediately because newer always means safer','Version recency is not evidence of preserved task-specific behavior.'),
 ('Keep only positive pilot examples as evaluation evidence','Selective examples can conceal important regressions.'),
 ('Disable monitoring so users are not distracted by changes','Removing monitoring hides problems rather than preventing them.')],
 'Use continuous evaluation and controlled version transitions. Security updates matter, but application behavior and sensitive cases still need review.')
case(5,70,'An assistant drafts guidance that could materially affect the eligibility of a person for a service. Reviewers identify uncertain edge cases. Which control best fits the consequential decisions?',[
 ('Qualified human review with clear escalation and approval responsibility','People can assess uncertain cases before a consequential action is taken.'),
 ('A more confident persona as the sole safeguard','Tone does not establish correctness or decision authority.'),
 ('A higher maximum output length as the sole safeguard','More text does not ensure sound judgment.'),
 ('Unreviewed automation because the average pilot score was high','An aggregate score does not resolve consequential edge cases.')],
 'Use oversight proportionate to impact. The model can assist, but uncertain high-impact decisions need defined human responsibility and review.')
case(6,85,'A team proposes prompt tuning and another proposes rewriting the prompt manually. Which distinction is most accurate for supported prompt-tuning approaches?',[
 ('Prompt tuning learns prompt representations while base weights remain frozen; manual prompt engineering changes written instructions','This distinguishes learned prompt-side adaptation from direct input wording changes.'),
 ('Both methods necessarily retrain every model parameter','That is not required by either manual prompting or the stated prompt-tuning approach.'),
 ('Both methods are simply retrieval from a search engine','Retrieval is a separate evidence-supply mechanism.'),
 ('Prompt tuning always makes private data publicly accessible','Access and data handling depend on the system design, not this definition.')],
 'Choose the customization method based on the behavior needed, data availability, support, cost, and evaluation. Prompt tuning, fine-tuning, RAG, and manual prompting are not interchangeable.')

case(1,88,'An illustrative pilot saves $12,000 per month in verified staff effort and costs $4,000 per month to operate, plus a $24,000 one-time implementation cost. Ignoring tax and financing, what is the simple payback period?',[
 ('3 months','Net monthly savings are $12,000-$4,000=$8,000; $24,000/$8,000=3 months.'),
 ('2 months','This divides implementation cost by gross benefits while ignoring operating cost.'),
 ('6 months','This divides implementation cost by operating cost, which is not the net benefit.'),
 ('There is no payback because any operating cost prevents it','Positive net savings can recover the initial implementation cost.')],
 'Use net benefit for a simple payback calculation. These figures are hypothetical business inputs, not Google Cloud prices.')
case(2,88,'An illustrative AI workflow delivers $100,000 in verified first-year benefits. Total first-year implementation and operation cost is $80,000. Using ROI=(benefits-cost)/cost, what is first-year ROI?',[
 ('25%','($100,000-$80,000)/$80,000=0.25, or 25%.'),
 ('125%','This is benefits divided by cost, not the defined net-return formula.'),
 ('20%','This divides net benefit by gross benefit rather than cost.'),
 ('80%','The cost-to-benefit ratio is not the defined ROI.')],
 'Use the explicitly stated financial definition and include total relevant costs. A positive ROI does not remove the need for quality and risk checks.')
case(3,88,'A model option costs $0.02 per attempt and 50% of attempts meet the acceptance target. Another costs $0.03 per attempt and 90% meet it. Ignoring all other costs, which has the lower expected model cost per accepted output?',[
 ('The $0.03 option, at about $0.033 per accepted output','Cost divided by acceptance probability is about $0.033 versus $0.04 for the cheaper attempt.'),
 ('The $0.02 option, because the unit price alone determines usable output cost','The acceptance rate changes the number of attempts needed per accepted output.'),
 ('Both are equal at $0.05 per accepted output','Adding the prices is not a cost-per-accepted-output calculation.'),
 ('The comparison is impossible even with the stated simplifying assumptions','The specified costs and acceptance rates are enough for this simplified expected-cost calculation.')],
 'Quality affects economics. This is a hypothetical comparison under simplified assumptions, not real service pricing; review, integration, and risk costs matter in a full decision.')
case(4,88,'A pilot reduces average task time from 20 minutes to 15 minutes while keeping the required quality. What is the percentage reduction relative to the original task time?',[
 ('25%','The reduction is 5 minutes divided by the 20-minute baseline.'),
 ('33.3%','This divides the reduction by the new time instead of the original baseline.'),
 ('5%','Five is the number of minutes saved, not the percentage reduction.'),
 ('75%','The new time is 75% of the original, not the amount of the reduction.')],
 'Specify the baseline when reporting percentage improvement and verify that quality and risk constraints remain acceptable.')
case(5,88,'An illustrative project saves $60,000 annually before $20,000 of annual operating costs. Initial implementation costs $100,000. Ignoring tax and financing, how long is the simple payback period?',[
 ('2.5 years','Net annual savings are $40,000; $100,000/$40,000=2.5 years.'),
 ('About 1.67 years','This ignores the annual operating costs and uses gross savings.'),
 ('5 years','This divides initial cost by operating cost rather than net savings.'),
 ('0.4 years','This reverses the payback ratio.')],
 'Simple payback uses initial cost divided by recurring net savings. More complete investment analysis may also account for timing, uncertainty, and other effects.')
case(6,88,'A business expects 10,000 monthly requests at an illustrative model cost of $0.01 each. It also budgets $300 for review and $500 for platform operations each month. What is the total stated monthly cost?',[
 ('$900','Model usage is $100, plus $300 review and $500 operations, totaling $900.'),
 ('$100','This counts only model usage and omits the other stated expenses.'),
 ('$800','This omits model usage from the stated total.'),
 ('$10,800','This treats the number of requests as a monetary cost.')],
 'Budget the whole workflow, not just tokens or requests. These are illustrative figures rather than current Google service prices.')
