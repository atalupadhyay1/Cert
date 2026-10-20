"""Original AIF-C01 teaching bank. Six independently worded prompts per objective.
No exam dumps. Shared objectives deliberately recur for spaced practice.
Edit this source, then run build.py and validate.py.
"""
TERMS = {}
ITEMS = []
def term(key, label, why):
    TERMS[key] = (label, why)
def item(domain, keys, reason, prompts, ref=None):
    questions = [q.strip() for q in prompts.strip().split('\n') if q.strip()]
    assert len(questions) == 6, (keys, len(questions))
    ITEMS.append(dict(domain=domain, keys=keys.split(), reason=reason, prompts=questions, ref=ref))

# Definitions supply substantive feedback for correct answers and distractors.
term('supervised','Supervised learning','Learns a mapping from input examples to known target labels.')
term('unsupervised','Unsupervised learning','Discovers structure in data without supplied target labels.')
term('reinforcement','Reinforcement learning','Learns actions through interaction and reward signals.')
term('rules','Deterministic rule-based processing','Executes explicit rules; it does not learn patterns from training examples.')
term('classification','Classification','Predicts a discrete category, such as fraud or legitimate.')
term('regression','Regression','Predicts a continuous numeric quantity, such as a sale price.')
term('clustering','Clustering','Groups similar examples without requiring predefined category labels.')
term('generation','Generative modeling','Creates new content based on patterns learned from training data.')
term('training','Training','Adjusts model parameters using training examples and an optimization objective.')
term('inference','Inference','Uses a trained model to produce outputs for new inputs.')
term('validation','Validation','Uses a held-out development dataset to select models or hyperparameters.')
term('test','Final test evaluation','Estimates generalization using held-out data not used for training or model selection.')
term('overfit','Overfitting','Fits training-specific noise and patterns, producing weak generalization.')
term('underfit','Underfitting','Fails to capture important patterns, often performing poorly on both training and unseen data.')
term('leakage','Data leakage','Allows information unavailable at prediction time to influence training or evaluation.')
term('drift','Data distribution drift','Occurs when production input distributions change relative to the reference data.')
term('precision','Precision','Measures the fraction of predicted positives that are actually positive.')
term('recall','Recall','Measures the fraction of actual positives that the model identifies.')
term('accuracy','Accuracy','Measures the fraction of all predictions that are correct; imbalance can make it misleading.')
term('f1','F1 score','Combines precision and recall using their harmonic mean.')
term('mae','Mean absolute error','Measures average absolute numeric prediction error in the target variable units.')
term('latency','Inference latency','Measures the time required to return a prediction or response.')
term('textract','Amazon Textract','Extracts text, form fields, and tables from document images.')
term('rekognition','Amazon Rekognition','Analyzes images and video for objects, scenes, and other supported visual features.')
term('transcribe','Amazon Transcribe','Converts speech audio into text.')
term('polly','Amazon Polly','Converts text into synthesized speech.')
term('comprehend','Amazon Comprehend','Uses natural language processing for tasks such as entity extraction and sentiment analysis.')
term('translate','Amazon Translate','Translates text between supported languages.')
term('sagemaker','Amazon SageMaker AI','Provides managed tools for developing, training, and deploying ML models.')
term('bedrock','Amazon Bedrock','Provides managed access to foundation models and features for building generative AI applications.')
term('groundtruth','Amazon SageMaker Ground Truth','Supports workflows for labeling training data with human workers and automation.')
term('s3','Amazon S3','Provides object storage for datasets, artifacts, and other objects.')
term('batch','Batch inference','Processes a collection of inputs asynchronously when immediate individual responses are unnecessary.')
term('realtime','Real-time inference','Serves individual prediction requests with interactive response requirements.')
term('features','Input features','Are measurable input attributes used by a model to make predictions.')
term('labels','Target labels','Are known outcomes provided to a supervised learning algorithm.')
term('parameters','Model parameters','Are internal values learned during training, such as weights.')
term('hyperparameters','Hyperparameters','Are configuration choices such as learning rate, selected outside the parameter-learning process.')
term('clean','Clean and representative training data','Reduces avoidable data errors and improves coverage of the intended operating population.')
term('moreepochs','More training epochs alone','Repeats passes over training data but does not inherently fix label errors, bias, or leakage.')
term('larger','A larger model alone','Adds capacity but does not automatically improve data quality or suitability for a business problem.')
term('business','Business outcome metrics','Measure operational value, such as handling time, revenue, or resolved customer issues.')

item(1,'supervised unsupervised reinforcement rules','Known historical outcomes make learning an input-to-target mapping possible.', '''A lender has applications labeled repaid or defaulted. Which learning approach fits prediction of future defaults?
An email team has messages tagged spam or legitimate. Which learning approach can use these examples directly?
A factory has sensor readings paired with confirmed failure outcomes. Which approach learns from those pairs?
An insurer supplies past claims and their verified fraud labels. Which learning paradigm fits this dataset?
A retailer provides product reviews with human-assigned sentiment classes. Which approach uses these targets?
A hospital has approved training records with known readmission outcomes. Which learning approach fits this setup?''')
item(1,'unsupervised supervised reinforcement rules','No target labels are available; discovering inherent groups is an unsupervised task.', '''A retailer wants to discover shopper segments from purchase behavior without labeled segments. Which approach fits?
A publisher wants to find natural groups of articles without predefined topic labels. Which approach fits?
A telecom company explores patterns in unlabeled usage records. Which learning paradigm is appropriate?
A researcher wants to identify structure in unlabeled gene measurements. Which learning approach fits?
A wholesaler wants to discover similar store profiles with no known store categories. Which approach fits?
A travel company wants to explore unlabeled booking patterns before defining customer segments. Which approach fits?''')
item(1,'reinforcement supervised unsupervised rules','Sequential actions with feedback rewards indicate reinforcement learning, rather than fixed labeled examples.', '''A simulated warehouse robot receives rewards for safe, efficient deliveries. Which learning approach fits?
A game-playing agent improves by receiving a score after its actions. Which paradigm is being used?
A simulator rewards a traffic controller for reducing queues after signal changes. Which learning approach fits?
A navigation agent explores routes and receives penalties for collisions. Which paradigm fits this feedback?
A resource-allocation agent learns a policy from rewards for meeting service objectives. Which approach fits?
A simulated robot arm receives positive feedback for successful grasps after trying actions. Which approach fits?''')
item(1,'classification regression clustering generation','The required output is a discrete class rather than a continuous value or unlabeled group.', '''A bank must mark a transaction as suspicious or normal. What type of prediction is this?
A support tool assigns each ticket to billing, technical, or account access. What ML task is this?
A medical research model assigns an image to one of several known disease categories. What task is this?
A manufacturer labels a finished item as pass or fail. What type of ML problem is this?
A moderation model predicts whether a comment violates a defined policy. What prediction task fits?
A document router assigns each file to an existing department category. Which ML task fits?''')
item(1,'regression classification clustering generation','The target is a continuous numeric measurement; regression predicts its magnitude.', '''A real estate model predicts a house sale price. Which ML task fits?
A logistics model predicts delivery duration in minutes. Which task fits this numeric target?
A factory predicts energy consumption in kilowatt-hours. Which ML task is this?
An insurer predicts the monetary cost of a claim. Which modeling task fits?
A weather model predicts tomorrow's maximum temperature. Which task fits?
A retailer predicts next month's sales revenue as a continuous value. Which ML task fits?''')
item(1,'training inference validation test','Learning weights from examples is training; serving an already learned model is inference.', '''An engineer runs optimization over labeled examples to update neural network weights. Which lifecycle stage is this?
A model's parameters change as it processes repeated passes through historical data. Which stage is occurring?
A team fits a predictor to historical prices before deploying it. Which ML lifecycle activity is this?
A learning algorithm minimizes its objective by updating internal values. Which stage is this?
A fraud model learns relationships from confirmed historical transactions. What lifecycle activity is being performed?
A development job adjusts a model's weights using approved examples. Which lifecycle stage is this?''')
item(1,'inference training validation test','Using a model to predict a new operational example is inference; weights need not be updated.', '''A deployed endpoint scores a newly received payment for fraud risk. Which activity is this?
A mobile application sends a new photo to a trained classifier and receives a category. Which stage is this?
An existing model predicts a delivery estimate for a new order. What ML activity is occurring?
A production service uses saved weights to classify an incoming support ticket. Which activity is this?
A trained speech model converts a customer's newly uploaded recording to text. Which stage is this?
A loan application is passed to an already deployed risk model for a score. Which activity is this?''')
item(1,'overfit underfit drift leakage','A large training-versus-held-out performance gap is characteristic of overfitting.', '''A classifier performs almost perfectly on training data but poorly on untouched examples. What is the likely issue?
A complex model memorizes rare training records and fails on new records from the same distribution. What is this?
Training error keeps falling while validation error rises. Which problem does this pattern suggest?
A model recognizes its training images but struggles with new images drawn from the same population. What is likely?
A predictor captures noise in the training sample rather than stable relationships. Which issue is this?
Adding model complexity improves training accuracy but worsens held-out accuracy. What problem is emerging?''')
item(1,'underfit overfit leakage drift','Poor performance even on the training set can indicate insufficient model capacity or inadequate learning.', '''A very simple predictor performs poorly on both training and validation examples. Which issue is most likely?
A linear model cannot capture a strongly nonlinear relationship even in training data. Which problem is this?
A model is too constrained to learn basic patterns in its training examples. What is this called?
Training and validation errors are both high because the model misses important relationships. What is likely?
A sentiment model cannot fit even the clear patterns present in its training sample. Which issue does this suggest?
An overly simplistic forecasting model misses seasonal patterns in both seen and unseen data. What is likely?''')
item(1,'leakage drift overfit underfit','Using future outcomes or overlapping evaluation records gives an unrealistically favorable estimate.', '''A default predictor uses a field recorded only after the borrower defaults. What evaluation risk is present?
An analyst normalizes data using statistics from the final test set before model selection. What issue can this introduce?
A dataset contains duplicate customers in training and test partitions, inflating evaluation results. What is the concern?
A ticket model uses the final resolution text to predict the initial routing decision. What problem exists?
A sales predictor includes actual end-of-month totals when predicting at the start of the month. What is this?
A model predicts hospital discharge outcomes using fields populated after discharge. What risk should be addressed?''')
item(1,'precision recall accuracy mae','When false positive alerts are costly, precision directly describes how trustworthy positive predictions are.', '''Investigators want to know what fraction of fraud alerts are genuinely fraudulent. Which metric answers this?
A moderation team asks how often flagged posts truly violate policy. Which metric should it inspect?
A medical team asks what fraction of positive model predictions are confirmed cases. Which metric fits?
A lead-scoring team wants the proportion of predicted qualified leads that actually qualify. Which metric is this?
A factory wants to measure how many defect alerts correspond to real defects. Which metric fits?
A spam team wants the proportion of messages marked spam that really are spam. Which metric measures this?''')
item(1,'recall precision accuracy mae','Recall measures coverage of actual positives and is useful when missing positives is costly.', '''A screening team wants to measure the fraction of all true disease cases detected. Which metric fits?
A fraud team prioritizes finding as many actual fraudulent payments as possible. Which coverage metric fits?
A safety team asks how many of all dangerous events its detector identified. Which metric answers this?
A security team wants the fraction of actual attacks successfully flagged by its classifier. Which metric fits?
A manufacturer measures the fraction of truly defective products detected. Which metric is this?
A document team wants to know how many of all relevant records were found. Which metric measures this?''')
item(1,'mae accuracy precision recall','Absolute numeric prediction errors are meaningful for a continuous target; classification metrics are not the direct fit.', '''A price predictor must be evaluated by average absolute error in dollars. Which metric fits?
A delivery model's errors should be reported in minutes without allowing positive and negative errors to cancel. Which metric fits?
A temperature predictor needs an average error measure in degrees. Which listed metric is suitable?
A demand model should report the average magnitude of its numeric prediction mistakes. Which metric fits?
A claim-cost model needs an interpretable average absolute deviation in currency units. Which metric fits?
An energy forecast must report average absolute prediction error in kilowatt-hours. Which metric fits?''')
item(1,'textract rekognition transcribe comprehend','Document structure, forms, and tables call for document extraction rather than speech or general image analysis.', '''A finance team needs key-value fields and tables from scanned invoices. Which AWS service best fits?
A bank needs to extract form entries from images of application documents. Which service fits?
An insurer must turn scanned claim tables into structured data. Which AWS AI service fits?
A logistics firm needs text and layout-aware table extraction from delivery forms. Which service fits?
An archive wants to extract printed form fields from scanned documents. Which AWS service fits?
A procurement team needs line-item tables from invoice images. Which service is designed for this?''')
item(1,'transcribe polly translate textract','The input is speech audio and the required output is text.', '''A contact center needs text transcripts of recorded calls. Which service fits?
A university wants written transcripts of lecture audio. Which AWS service fits?
A podcast team needs speech-to-text output for episode recordings. Which service fits?
A medical training platform needs transcripts of consented educational recordings. Which service fits?
A media company wants to convert interview audio into written text. Which AWS service fits?
A meeting application needs a transcription service for spoken discussion. Which service fits?''')
item(1,'comprehend translate transcribe rekognition','The requested task analyzes the meaning or entities of existing text, not language conversion or audio recognition.', '''A retailer needs sentiment detection in customer reviews. Which AWS service fits?
A company wants named entities identified in business articles. Which managed NLP service fits?
A support team needs sentiment analysis of written feedback. Which AWS service fits?
A publisher needs to identify organizations and locations in text documents. Which service fits?
An analyst wants key phrases from a large set of written comments. Which service fits?
A service desk wants to analyze sentiment in its existing text transcripts. Which AWS service fits?''')
item(1,'groundtruth s3 bedrock polly','Human annotation of training examples is a data-labeling workflow.', '''A vision team needs human workers to label bounding boxes for training images. Which service supports this workflow?
A company needs a managed process for workers to annotate text training examples. Which SageMaker capability fits?
A manufacturer wants reviewers to label defects in a training image collection. Which AWS capability fits?
A researcher needs a workforce workflow to assign labels to an ML dataset. Which service fits?
A team has unlabeled photos and needs human-verified category annotations. Which managed capability fits?
An ML team wants human annotators and automation to help create its labeled dataset. Which service fits?''')
item(1,'batch realtime training validation','The workload has no interactive response requirement and can process a collection asynchronously.', '''A retailer scores five million historical records overnight with no immediate response requirement. Which inference mode fits?
A publisher generates predictions for its entire archive once each weekend. Which inference mode fits?
An insurer scores a daily file of claims before the next morning. Which inference mode is suitable?
A bank performs a monthly offline portfolio scoring job. Which inference approach fits?
A utility processes yesterday's meter readings together after collection. Which inference mode fits?
A research team runs predictions on a fixed dataset and retrieves results when the job completes. Which mode fits?''')
item(1,'features labels parameters hyperparameters','Inputs supplied to the model are features; the known outcome is the label.', '''In a house-price model, floor area and number of bedrooms are what type of information?
For a churn predictor, monthly usage and tenure are provided as model inputs. What are they called?
A fraud model uses transaction amount and merchant category as inputs. What are these attributes?
A delivery model receives route distance and package weight. What role do these values play?
A defect classifier receives measurements of item width and surface texture. What are these inputs called?
A risk model uses approved applicant income and debt information as predictors. What are these variables called?''')
item(1,'clean business moreepochs larger skip','Select TWO. Data quality and measurable business value are prerequisites; extra capacity or training alone does not establish suitability.', '''Before launching a customer-service ML pilot, which TWO foundations should a team prioritize? (Select TWO.)
A retailer is evaluating whether an ML initiative is worthwhile. Which TWO foundations should guide the decision? (Select TWO.)
A bank wants an ML pilot to deliver trustworthy operational value. Which TWO foundations matter first? (Select TWO.)
A manufacturer plans its first predictive quality project. Which TWO foundations best support a useful pilot? (Select TWO.)
A logistics manager must justify an ML investment before scaling. Which TWO foundations should be established? (Select TWO.)
A healthcare operations team wants a useful and reliable ML feasibility study. Which TWO foundations should it prioritize? (Select TWO.)''')
term('fm','Foundation model','Is pretrained on broad data and can be adapted to a range of downstream tasks.')
term('llm','Large language model','Models language token sequences and can perform tasks such as text generation and summarization.')
term('token','Token','Is a model-dependent unit of text or other input representation used in processing and billing.')
term('embedding','Embedding','Is a numeric vector representation used to capture relationships such as semantic similarity.')
term('context','Context window','Limits the amount of input and generated content a model can consider within a request, according to model-specific rules.')
term('hallucination','Hallucination','Is plausible-looking generated content that is factually incorrect or unsupported.')
term('multimodal','Multimodal model','Processes or generates more than one modality, such as text and images.')
term('diffusion','Diffusion model','Learns to reverse a noise-adding process and is commonly used for image generation.')
term('pretrain','Pretraining','Learns broad patterns from a large corpus before adaptation to a narrower task.')
term('finetune','Fine-tuning','Updates an existing model using task-specific examples to adapt its behavior.')
term('rag','Retrieval-Augmented Generation (RAG)','Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.')
term('prompt','Prompt engineering','Shapes instructions, context, and examples supplied at inference time without changing model weights.')
term('temperature','Temperature','Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.')
term('topk','Top-k sampling','Restricts sampling candidates to the k highest-probability tokens at each step.')
term('topp','Top-p sampling','Restricts sampling to a set of tokens whose cumulative probability reaches a chosen threshold.')
term('maxtokens','Maximum output tokens','Caps generated response length, subject to model-specific limits.')
term('ondemand','On-demand inference','Supports usage-based access without reserving dedicated model throughput in advance.')
term('provisioned','Provisioned Throughput','Reserves model capacity for supported models under the applicable pricing and commitment terms.')
term('cost','Token and request cost measurement','Tracks input/output usage and actual prices to compare the economics of candidate models.')
term('qualityeval','Task-specific quality evaluation','Tests representative prompts against defined acceptance criteria rather than assuming all models perform equally.')
term('qbusiness','Amazon Q Business','Is a generative AI assistant for enterprise information with supported data connectors and access-aware retrieval.')
term('qdeveloper','Amazon Q Developer','Provides generative AI assistance for software development and AWS-related technical tasks.')
term('canvas','Amazon SageMaker Canvas','Offers a visual, no-code experience for building and using supported ML models.')
term('distill','Model distillation','Trains a smaller student model to reproduce useful behavior of a larger teacher model.')
term('quantize','Model quantization','Uses lower-precision numeric representations to reduce model memory and potentially improve inference efficiency.')
term('skip','Deploy without evaluation','Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.')
term('fresh','Retrieve current approved sources','Provides up-to-date evidence at inference time; model pretraining alone does not supply newly changed facts.')
term('verify','Verify factual claims against trusted sources','Checks generated claims instead of treating confident language as proof of accuracy.')

item(2,'fm rules regression clustering','Broad pretraining and reuse across downstream tasks distinguish a foundation model from a narrow task-specific predictor.', '''A model pretrained on broad data is reused for summarization, question answering, and adaptation. What is it?
A company wants one broadly pretrained starting point for many downstream AI tasks. Which model category fits?
A vendor offers a broadly trained model that can be prompted or adapted for different use cases. What is this category?
An architecture reuses knowledge learned from a large general corpus across several applications. Which model type fits?
A team starts with a reusable pretrained model rather than training a narrow predictor from scratch. What category fits?
A product team selects a broadly pretrained base that supports multiple downstream tasks. What kind of model is this?''')
item(2,'llm rekognition rules regression','Language modeling generates and transforms text; it is not a guarantee that the generated text is factual.', '''A team needs a model primarily designed to generate and summarize natural language. Which category fits?
A legal assistant must draft text from written instructions. Which model category is most directly relevant?
A company needs a model that predicts language tokens to continue a passage. Which category fits?
A writing tool turns a short request into a coherent paragraph. Which model category is a natural fit?
A support tool must summarize a long written conversation. Which model category fits this generative task?
A documentation assistant drafts explanations in natural language from textual prompts. Which category fits?''')
item(2,'generation classification regression clustering','Producing novel content is generative; choosing a label or predicting a numeric quantity is not the same task.', '''An application creates original product descriptions from attributes. Which modeling capability is this?
A design assistant creates a new image from a text description. Which capability is being used?
A support tool drafts a new reply rather than merely assigning a ticket category. Which modeling capability fits?
A marketing tool creates candidate slogans from a campaign brief. Which modeling capability is this?
A training assistant writes new practice scenarios from learning objectives. Which capability is this?
A creative tool produces a new audio sample from a description. Which modeling capability is this?''')
item(2,'token embedding parameters labels','Tokenization units are model-dependent and are not always entire words.', '''A model bills for input and output units that can be word fragments. What are these units called?
A prompt is split into model-specific processing units before an LLM processes it. What are they?
A developer discovers that a long word can consume several billable text units. What are these units?
An LLM response contains many small text units rather than one unit per sentence. What are these units called?
An estimator must count model-dependent text units to forecast inference charges. What should it count?
A multilingual prompt uses a different number of processing units than its word count. Which units are being counted?''')
item(2,'embedding token labels hyperparameters','Semantic vector representations enable similarity comparison without exact keyword overlap.', '''A search system represents sentences as vectors so that similar meanings are close. What representation is this?
A recommender converts item descriptions into numeric vectors for similarity lookup. What are these vectors called?
A team needs a machine-readable numeric representation of text meaning. Which representation fits?
A semantic index stores vector representations of document passages. What does each vector represent?
A search engine matches a paraphrased query to conceptually related content using numeric vectors. What enables this?
A clustering pipeline uses vectors that encode semantic relationships between articles. What are these representations?''')
item(2,'context maxtokens temperature topk','The total information considered per request is bounded; a larger context does not inherently eliminate errors.', '''An LLM cannot accept an entire manual plus a desired response in one request. Which limit is being reached?
A team measures the maximum amount of conversation a model can consider at once. Which concept is this?
A chatbot loses earlier details after its request exceeds the model's supported token capacity. Which constraint matters?
A document assistant must split source material because the prompt is too large. Which model characteristic limits it?
An architect compares models by how much input and response content each can handle in a request. Which characteristic is this?
A user wants a model to consider more reference passages simultaneously. Which model limit should be examined?''')
item(2,'hallucination drift leakage underfit','Fluent output can contain fabricated facts; confidence in wording is not evidence of factual grounding.', '''A chatbot invents a nonexistent product policy and states it confidently. What failure is this?
An assistant supplies a convincing but nonexistent journal citation. Which GenAI limitation is illustrated?
A generated summary introduces a fact absent from the source and contrary to the record. What is this issue?
An LLM fabricates an API method that does not exist in the documentation. What is this called?
A model gives a plausible historical date that is factually wrong. Which limitation is this?
A travel bot invents a flight route that the airline does not operate. What type of failure is this?''')
item(2,'multimodal llm regression rules','The defining requirement is handling distinct input or output modalities, rather than text alone.', '''A model must interpret an uploaded photo alongside a written question. Which capability is needed?
An assistant processes both an audio clip and a text instruction in one workflow. Which model capability fits?
A designer wants a model to relate visual content to a textual request. Which model category fits?
A product inspection assistant reasons over images and accompanying text. What capability is required?
A learning assistant accepts diagrams as well as typed questions. Which capability should its model support?
A media tool must connect information from video frames and text descriptions. Which model capability fits?''')
item(2,'diffusion regression clustering rules','Iterative denoising is a characteristic mechanism of diffusion-based generation.', '''An image generator starts with noise and repeatedly denoises it into an image. Which model family fits?
A system learns how to reverse gradual corruption of training images. Which generative approach is this?
A designer uses a generator that refines random noise into a coherent picture. Which model family fits?
A visual model synthesizes an image through successive denoising steps. Which approach is being used?
A training demonstration describes reversing a forward noise process to create samples. Which model family fits?
An image synthesis pipeline iteratively removes noise under text conditioning. Which generative approach fits?''')
item(2,'pretrain inference prompt rag','Broad initial learning from a corpus is pretraining, not retrieving context or sending instructions during inference.', '''A vendor first trains a model on a vast general corpus before task adaptation. Which stage is this?
A new foundation model learns broad language patterns from large datasets. What process is occurring?
A team compares the expensive initial broad training stage with later task adaptation. What is the initial stage called?
A model learns reusable representations from general data before any customer-specific work. Which stage is this?
An organization builds the initial broadly capable model rather than customizing an existing one. Which process is this?
A base model acquires general patterns from a large text collection before deployment. Which activity is this?''')
item(2,'finetune prompt rag inference',"Changing an existing model's weights with task examples is fine-tuning, unlike prompt-only or retrieval-only adaptation.", '''A company updates a pretrained model's weights using approved domain examples. Which approach is this?
A team adapts an existing language model through additional task-specific training. What is this called?
A model learns a specialized output style by updating parameters on curated demonstrations. Which method is used?
An organization trains an existing base model further on its labeled task examples. Which adaptation method is this?
A customization job adjusts pretrained weights to improve a narrow task. What is this process?
A product team supplies examples to an additional training run on an existing model. Which adaptation approach fits?''')
item(2,'prompt finetune pretrain distill','Instructions and examples provided at request time change the input, not the learned weights.', '''A team improves an assistant by rewriting its instructions without training. Which technique is this?
A product manager adds examples to a prompt while leaving the model unchanged. Which approach is being used?
An analyst specifies output format and constraints in the request rather than changing weights. Which method fits?
A company improves model responses by restructuring the supplied context and instructions. What approach is this?
An application asks the same model to behave as a concise editor through explicit instructions. Which technique is used?
A developer iterates on prompt wording and examples without running a training job. What approach is this?''')
item(2,'temperature maxtokens context labels','Temperature changes sampling behavior; it neither expands the context window nor guarantees factual correctness.', '''A writer wants more varied outputs from a sampling-based model. Which inference setting is most directly relevant?
A support bot needs more focused token sampling rather than highly varied wording. Which setting can be lowered?
A team compares the effect of sampling randomness on repeated responses. Which setting is it adjusting?
A creative tool needs to tune how adventurous generated continuations are. Which listed setting fits?
A testing team wants to reduce output variability without altering model weights. Which sampling setting is relevant?
A model produces overly unpredictable wording during drafting. Which setting most directly controls this randomness?''')
item(2,'topk topp temperature maxtokens','Top-k is a fixed candidate-count restriction, not a cumulative probability threshold.', '''A sampler considers only the 20 most likely next tokens. Which decoding control is this?
A team limits each sampling step to a fixed number of highest-probability candidates. Which setting is this?
An engineer caps the candidate token set by count rather than probability mass. Which sampling method fits?
A generation configuration retains exactly the highest-ranked k candidates before sampling. Which setting is this?
A model's decoder excludes all tokens outside a specified top-ranked candidate count. Which control is this?
A tuning guide describes selecting from only the N most probable next tokens. What is this method called?''')
item(2,'topp topk maxtokens context','Nucleus sampling uses cumulative probability mass; its candidate count can vary by step.', '''A sampler keeps the smallest token set whose cumulative probability reaches 0.9. Which method is this?
A team changes a probability-mass threshold rather than a fixed candidate count. Which decoding setting fits?
A decoder dynamically sizes its candidate set using cumulative token probability. Which method is this?
A model samples from a probability nucleus instead of always retaining a fixed number of tokens. What is this called?
A generation setting retains likely tokens until a chosen total probability is reached. Which setting is this?
A developer uses a 0.95 cumulative-probability threshold for next-token candidates. Which sampling control fits?''')
item(2,'maxtokens temperature topp embedding','An output-length cap can constrain response size and cost but may truncate a response.', '''An application needs to cap the length of generated responses. Which setting is most directly relevant?
A team wants a hard upper bound on generated token count for each request. Which control fits?
A chatbot returns overly long answers; the team wants an output token ceiling. Which setting should it inspect?
An architect wants to limit response size without changing sampling randomness. Which setting fits?
A response is cut off because it reaches its configured generation-length limit. Which setting caused this?
A cost-control policy needs a maximum generated length per call. Which inference setting supports this?''')
item(2,'bedrock sagemaker textract translate','Managed access to a choice of foundation models is a core Amazon Bedrock use case.', '''A startup wants managed API access to foundation models from multiple providers without managing model servers. Which service fits?
A business wants to compare supported foundation models through a managed generative AI platform. Which AWS service fits?
A team needs a managed platform for foundation-model applications, retrieval, and guardrails. Which service fits?
An application needs foundation-model inference without deploying its own model-serving cluster. Which AWS service fits?
A company wants to build GenAI applications using a choice of supported model providers. Which service fits?
An architect seeks managed foundation-model APIs rather than training a custom ML model from scratch. Which AWS service fits?''')
item(2,'qbusiness qdeveloper groundtruth polly','Enterprise question answering over connected organizational information fits Amazon Q Business.', '''Employees need an enterprise assistant that answers questions over supported connected company content. Which service fits?
A business wants a managed assistant for finding information across its organizational data sources. Which AWS service fits?
A company wants employee-facing natural-language answers grounded in connected enterprise information. Which service fits?
A team seeks an enterprise knowledge assistant with access-aware retrieval from supported repositories. Which service fits?
A firm wants employees to query internal documentation through a managed business assistant. Which service fits?
An organization needs a general enterprise information assistant rather than a coding assistant. Which AWS service fits?''')
item(2,'qdeveloper qbusiness textract transcribe','Developer-oriented coding and AWS technical assistance fits Amazon Q Developer.', '''A developer wants AI help explaining code and suggesting improvements in a development workflow. Which service fits?
A software team seeks an AWS generative AI assistant aimed at coding tasks. Which service fits?
An engineer wants assistance with application code and AWS technical questions. Which Amazon Q offering fits?
A team needs AI suggestions while developing software rather than enterprise document search. Which service fits?
A programmer wants an assistant for understanding an unfamiliar codebase. Which AWS offering is designed for this role?
A development team wants generative AI support for building and troubleshooting software. Which service fits?''')
item(2,'ondemand provisioned pretrain finetune','Variable, exploratory traffic can use consumption-based access without a reserved throughput commitment.', '''A prototype has unpredictable, low inference traffic and wants no reserved capacity commitment. Which Bedrock access option fits?
A team is comparing supported models with sporadic requests before knowing demand. Which inference pricing approach fits?
A small pilot wants usage-based foundation-model access instead of purchasing reserved model capacity. Which option fits?
A development environment sends occasional requests and does not need dedicated model throughput. Which access option fits?
An experiment has irregular usage and should avoid an upfront throughput reservation. Which inference mode fits?
A startup is validating demand with a few model calls per day. Which access model is a reasonable starting point?''')
item(2,'provisioned ondemand prompt rag','Reserved throughput may suit predictable sustained demand, but support, commitments, and economics must be checked.', '''A team has stable high demand and wants to evaluate reserved model capacity for a supported Bedrock model. Which option should it assess?
An architect needs a throughput reservation rather than purely per-request access. Which supported Bedrock option fits?
A company can commit to sustained model use and wants reserved throughput. Which option should it evaluate?
A supported model powers a predictable production workload that may benefit from capacity reservation. Which option fits?
A team compares consumption-based access with an explicit model-throughput commitment. What is the committed option called?
A business seeks provisioned capacity for a supported foundation model after analyzing steady demand. Which feature fits?''')
item(2,'distill quantize prompt rag','A smaller model learning from a larger teacher is distillation, not merely lowering numerical precision.', '''A smaller student model is trained using outputs from a larger teacher. What technique is this?
A team transfers useful behavior from a large model into a compact model through training. Which technique fits?
An engineer wants a smaller model to imitate a larger model's response behavior. Which approach is this?
A model-compression project uses teacher-generated examples to train a student. Which technique fits?
A product team trains a compact predictor to reproduce a powerful model's outputs. What method is being used?
A deployment team reduces model size by training a student on a teacher's behavior. Which approach fits?''')
item(2,'qualityeval cost larger moreepochs skip','Select TWO. Model selection should jointly measure task quality and workload economics, not assume bigger is always better.', '''A team compares two foundation models for a production assistant. Which TWO evaluation activities are essential? (Select TWO.)
A startup must choose a model for its expected workload. Which TWO measurements best support a defensible choice? (Select TWO.)
A company wants to avoid selecting a model purely by parameter count. Which TWO evaluation practices should it use? (Select TWO.)
A team is deciding whether a cheaper model is adequate for its task. Which TWO evaluation activities should guide it? (Select TWO.)
A procurement group compares generative AI model options for a pilot. Which TWO evidence sources should guide selection? (Select TWO.)
A product manager needs to justify model choice using usefulness and economics. Which TWO activities fit? (Select TWO.)''')
item(2,'fresh verify temperature larger moreepochs','Select TWO. Current retrieved evidence and independent claim checking address stale or unsupported facts; neither guarantees perfect output.', '''An assistant answers questions about frequently changing company policies. Which TWO actions reduce unsupported factual answers? (Select TWO.)
A chatbot cites obsolete product terms and sometimes invents details. Which TWO actions address these limitations? (Select TWO.)
A company needs more reliable answers about its current catalog. Which TWO practices are most appropriate? (Select TWO.)
A support assistant must answer using newly approved procedures and avoid fabricated claims. Which TWO actions fit? (Select TWO.)
A research assistant must handle recent information while limiting unsupported statements. Which TWO practices fit? (Select TWO.)
A business chatbot should not rely solely on its model's pretraining for current facts. Which TWO actions are appropriate? (Select TWO.)''')
term('kb','Amazon Bedrock Knowledge Bases','Manages supported retrieval and generation workflows over connected data sources for grounding model responses.')
term('vector','Vector similarity search','Retrieves nearby embedding vectors to find semantically related content.')
term('keyword','Exact keyword search','Matches lexical terms and can be useful when exact identifiers or wording matter.')
term('chunk','Document chunking','Splits source content into retrievable passages; size and boundaries affect retrieval quality and context use.')
term('rerank','Reranking','Reorders an initially retrieved candidate set by relevance before selecting context.')
term('metadata','Metadata filtering','Restricts retrieval candidates using attributes such as department, date, or document type.')
term('agent','Amazon Bedrock Agents','Orchestrates foundation-model reasoning with supported knowledge retrieval and actions to complete tasks.')
term('tool','Tool or action invocation','Calls an external function or API to perform an operation or obtain information unavailable in model weights.')
term('zeroshot','Zero-shot prompting','Provides task instructions without worked task examples in the prompt.')
term('fewshot','Few-shot prompting','Includes a small number of demonstrations of the desired input-output behavior in the prompt.')
term('role','Role-based prompting','Sets a perspective or function, such as a concise technical editor, in the instructions.')
term('decompose','Task decomposition','Breaks a complex request into smaller explicit subtasks to improve control and reviewability.')
term('template','Reusable prompt template','Defines a consistent instruction structure with placeholders for task-specific inputs.')
term('version','Versioned prompt management','Tracks prompt revisions so changes can be evaluated, reproduced, and rolled back.')
term('schema','Explicit output schema and validation','Requests a structured format and checks generated output against that format before downstream use.')
term('rouge','ROUGE','Measures text overlap, commonly recall-oriented, between generated and reference summaries; it does not prove factual accuracy.')
term('bleu','BLEU','Measures n-gram overlap with reference text and is commonly associated with machine translation evaluation.')
term('human','Human evaluation','Uses qualified reviewers to assess dimensions such as correctness, usefulness, tone, and safety.')
term('autoeval','Automated model evaluation','Applies repeatable metrics or configured model-based judging to test examples, with limitations that require oversight.')
term('groundeval','Groundedness evaluation','Checks whether generated claims are supported by the supplied source context.')
term('relevanceeval','Retrieval relevance evaluation','Checks whether retrieved passages contain information useful for answering the query.')
term('holdout','Representative held-out evaluation prompts','Provide an independent test of quality across realistic users and tasks without reusing adaptation examples.')
term('cache','Cache eligible repeated results','Can reduce repeated computation, latency, and cost when correctness, permissions, and freshness requirements allow reuse.')
term('shortprompt','Remove irrelevant prompt content','Can reduce input token use and improve focus while preserving necessary instructions and evidence.')
term('smallmodel','Evaluate a smaller adequate model','Can reduce cost and latency when measured quality still meets the use case requirements.')
term('maxcontext','Always fill the entire context window','Consumes tokens and can introduce irrelevant information; more context is not inherently better.')
term('cite','Require source citations and inspect support','Improves traceability to retrieved evidence but still requires checking that the citations support the claims.')
term('sync','Refresh the retrieval index when sources change','Keeps indexed evidence aligned with approved source content according to the required freshness schedule.')
term('curate','Curate high-quality task examples','Provides consistent, representative examples for adaptation and reduces conflicting supervision.')
term('freeze','Keep evaluation data separate from adaptation data','Preserves an independent estimate of generalization and reduces evaluation leakage.')
term('compress','Compress or select context carefully','Reduces irrelevant tokens while retaining evidence required for the task.')

item(3,'rag finetune pretrain distill','Changing facts in external documents are best supplied through retrieval rather than embedded by repeatedly updating weights.', '''A chatbot must answer from frequently updated internal manuals without retraining model weights. Which architecture fits?
A retailer needs answers grounded in today's product documentation without modifying the base model. Which approach fits?
A legal assistant should use approved case documents supplied at query time. Which approach fits?
A support bot must consult a changing troubleshooting library while keeping the same model weights. Which method fits?
An enterprise assistant needs current internal policy evidence in each request. Which architecture fits?
A company wants grounded answers from its document repository without training a new model. Which technique fits?''')
item(3,'kb groundtruth polly qdeveloper','A managed Bedrock retrieval workflow fits Knowledge Bases; it is different from human labeling or development assistance.', '''A team wants a managed Bedrock feature to connect approved documents to retrieval-based answers. Which feature fits?
An application needs Bedrock-managed ingestion and retrieval for grounding responses in its content. Which capability fits?
An architect wants to use supported organizational data stores in a managed Bedrock RAG workflow. Which feature fits?
A company prefers a managed knowledge retrieval capability rather than implementing its entire Bedrock RAG pipeline. Which feature fits?
A support bot uses Bedrock and needs managed retrieval over connected reference material. Which capability fits?
A business wants Bedrock to retrieve relevant passages from its configured sources for a generative application. Which feature fits?''')
item(3,'vector keyword classification regression','Semantic retrieval compares embeddings; exact lexical matching is not required for paraphrases.', '''A query uses different wording from a relevant document but should still retrieve it by meaning. Which retrieval technique fits?
A support assistant must match paraphrased questions to conceptually related passages. Which search approach fits?
A search system should find relevant text even without shared keywords. Which technique fits?
An engineer searches a database using proximity between query and document embeddings. Which approach is this?
A help center wants meaning-based search rather than only exact phrase matches. Which technique fits?
A customer asks about ending a plan, while the document says subscription cancellation. Which retrieval technique can bridge the wording?''')
item(3,'chunk finetune temperature pretrain','Splitting documents into coherent passages controls retrieval granularity and the amount of evidence supplied per match.', '''Long source files must be divided into retrievable passages before indexing. Which preparation step is this?
A RAG team adjusts passage boundaries so answers have enough surrounding context. Which design choice is it tuning?
An assistant retrieves overly large document sections; the team wants smaller coherent units. Which preprocessing step should it revisit?
A knowledge pipeline breaks manuals into sections that can be embedded separately. What step is this?
A team balances passage size against context completeness for document retrieval. Which design decision is this?
A source ingestion job splits text into overlapping retrievable segments. What is this operation called?''')
item(3,'rerank chunk finetune temperature','A second relevance scoring stage reorders retrieved candidates; it does not change the source model weights.', '''A retriever returns 30 candidate passages, then another relevance step selects the best five. Which step is this?
A RAG system has relevant content in its candidate set but ranks it too low. Which additional stage could help?
A team wants to improve the order of initial retrieval results before passing context to a model. Which technique fits?
An application applies a more precise relevance scorer to already retrieved documents. What is this stage called?
A search pipeline reorders its initial results using query-document relevance. Which technique is this?
A knowledge assistant narrows an initial candidate set by rescoring relevance. Which retrieval stage fits?''')
item(3,'metadata temperature topk maxtokens','Retrieval attributes can constrain results to the requested subset; sampling controls do not enforce source categories.', '''A document assistant should retrieve only documents marked finance. Which retrieval control fits?
A RAG query should consider only documents with an approved publication date range. Which mechanism fits?
A product assistant must restrict retrieval to a specified product-version attribute. Which technique fits?
A help system needs results from documents tagged with a selected region. Which retrieval mechanism fits?
A researcher wants to retrieve only material marked as an approved document type. Which control fits?
A knowledge query must exclude archived items using a status attribute. Which technique fits?''')
item(3,'agent kb groundtruth textract','Multi-step task completion involving actions calls for orchestration, not retrieval alone.', '''An assistant must retrieve a policy, check an external system, and initiate an approved workflow. Which Bedrock capability fits orchestration?
A travel assistant must gather details and invoke supported booking APIs under application controls. Which Bedrock feature fits?
A service assistant needs to coordinate retrieval and action groups across multiple task steps. Which capability fits?
An operations assistant must use a model to plan and call supported business actions. Which Bedrock capability fits?
A customer assistant must combine knowledge lookup with an approved case-management action. Which feature fits orchestration?
A company wants a Bedrock feature to coordinate model reasoning, retrieval, and configured actions. Which feature fits?''')
item(3,'tool generation finetune embedding','External actions require a controlled integration; generating a statement that an action happened is not performing it.', '''A chatbot must actually check live inventory through an API rather than guess. Which capability is needed?
An assistant must submit a customer-approved service request to an external system. What mechanism performs the action?
A model lacks current shipment status and must query a logistics API. Which mechanism fits?
A financial assistant needs a controlled external calculator for an exact computation. Which mechanism fits?
A support assistant must fetch the latest ticket status from a business service. What mechanism is required?
A workflow must call an authorized function to update a reservation, not merely produce text. Which mechanism fits?''')
item(3,'zeroshot fewshot finetune pretrain','Instructions without demonstrations are zero-shot prompting; no parameter updates are involved.', '''A prompt says classify this review as positive or negative and supplies no examples. Which prompting style is this?
A translation request contains instructions and input text but no worked translations. Which prompting style fits?
A summarization prompt asks for three bullets without demonstrating any examples. Which style is this?
A support prompt specifies a task but includes no sample input-output pairs. What prompting style is this?
An analyst asks an LLM to extract dates using instructions alone. Which prompting approach is this?
A model receives a formatting task with no demonstrations of expected output. Which prompting style fits?''')
item(3,'fewshot zeroshot finetune pretrain','A small set of examples supplied in context demonstrates expected behavior without training weights.', '''A prompt includes three sample reviews and correct sentiment labels before a new review. Which approach is this?
An extraction prompt shows two input-output examples before the actual input. Which prompting style fits?
A team adds a handful of approved answers to demonstrate tone inside each request. Which technique is this?
A classifier prompt demonstrates several correct mappings without training the model. Which style fits?
A support template includes four worked examples for how to respond. Which prompting approach is this?
A formatting prompt supplies sample conversions before requesting a new conversion. Which approach is this?''')
item(3,'role finetune rag distill','A requested role is a prompt instruction, not proof of expertise or a change to the model weights.', '''A prompt begins act as a concise technical editor. Which technique is this?
A model is told to respond as a patient tutor for beginners. Which prompting approach is used?
An assistant is instructed to take the perspective of a careful customer-service representative. Which technique is this?
A writing prompt specifies a formal reviewer persona. Which prompt design approach fits?
A prompt tells the model to behave as a documentation assistant focused on clarity. Which technique is this?
A team sets the assistant's function and communication perspective in its instructions. What technique is this?''')
item(3,'decompose temperature pretrain distill','Explicit smaller subtasks improve control; this does not require exposing private internal reasoning.', '''A complex document request is split into extract facts, compare records, and draft a summary. Which technique is this?
A team turns a large analytical request into separate checkable subtasks. Which prompt design technique fits?
An assistant first identifies requirements, then evaluates alternatives, then produces a recommendation. Which technique fits?
A difficult workflow becomes several bounded tasks whose intermediate outputs can be reviewed. Which approach is this?
A product team improves control by breaking a long generation task into explicit smaller steps. Which technique fits?
An application separates evidence collection from final response generation. Which general task design technique is this?''')
item(3,'template pretrain quantize embedding','Templates keep instructions consistent while substituting user input and retrieved context.', '''A team uses fixed instructions with placeholders for customer text and retrieved evidence. Which artifact is this?
A prompt structure is reused across requests while only the document and question change. What is it?
A company standardizes output instructions using variable fields in a reusable prompt. Which approach fits?
An application fills a common instruction pattern with each user's query. Which artifact is being used?
A team wants consistent request structure without manually rewriting instructions each time. Which artifact fits?
A workflow inserts different records into the same approved prompt layout. What is this reusable artifact?''')
item(3,'version temperature embedding quantize','Tracking prompt versions enables controlled comparisons and rollback after a regression.', '''A team needs to know which prompt revision caused a drop in quality and restore the prior revision. Which practice fits?
An application must reproduce last month's model requests with the exact instruction revision. Which practice matters?
A prompt update improves one task but harms another; the team needs traceable rollback. Which practice fits?
An audit requires a record of prompt changes associated with each deployment. Which management practice fits?
A product team compares new and old instructions before promoting a change. Which practice supports this?
A support bot must link each response to an identifiable prompt revision. Which practice fits?''')
item(3,'schema temperature topk context','A requested format should be validated; prompting alone does not ensure every generated object is valid.', '''An assistant's output feeds software that requires valid JSON with specific fields. Which approach is best?
A workflow fails when generated records omit mandatory fields. Which design control should be added?
An extraction tool needs machine-readable output checked before database insertion. Which approach fits?
A company wants structured model responses accepted only when they satisfy a defined contract. Which control fits?
A downstream API expects a fixed object structure from a model response. Which design choice best supports this?
A report generator must reject responses that violate required field types. Which approach fits?''')
item(3,'finetune rag prompt pretrain','Persistent learned output behavior can be adapted through fine-tuning when suitable data, support, and evaluation justify it.', '''A team has many approved examples and needs persistent task-specific behavior through weight updates. Which method fits?
An existing model must learn a consistent specialized response style through additional training. Which adaptation fits?
A company wants the model itself to learn a domain-specific mapping from curated demonstrations. Which method fits?
A supported base model needs task adaptation by updating parameters rather than adding reference documents. Which approach fits?
A team can train on curated task examples and wants to change learned behavior, not merely retrieve facts. Which method fits?
A model must adapt its output conventions through supervised training on approved examples. Which approach is this?''')
item(3,'rouge bleu precision mae','ROUGE is commonly used for summary overlap, but complementary factual and human evaluation is still needed.', '''A team compares generated summaries with reference summaries using recall-oriented text overlap. Which metric fits?
A summarization benchmark needs a common overlap-based metric from the listed choices. Which fits best?
An evaluator wants to measure how much reference-summary content appears in a generated summary. Which metric family fits?
A team reports an automated reference-overlap score for summarization, alongside human review. Which metric is commonly used?
A document summarizer uses a standard overlap metric that often emphasizes recall. Which metric fits?
A model evaluation report lists summary overlap with human-written references. Which metric family fits?''')
item(3,'bleu rouge recall mae','BLEU is associated with reference-based translation overlap; it is not a complete semantic quality measure.', '''A translation team needs a common n-gram precision-oriented comparison with reference translations. Which metric fits?
A machine translation benchmark reports reference n-gram overlap. Which listed metric is commonly used?
An evaluator compares candidate translations with approved translations using a standard n-gram score. Which metric fits?
A language conversion tool needs a conventional translation overlap metric alongside human assessment. Which fits?
A report evaluates translation candidates using modified n-gram precision against references. Which metric fits?
A team wants the metric traditionally associated with reference-based machine translation evaluation. Which metric is this?''')
item(3,'human rouge bleu latency','Qualified reviewers can assess nuanced usefulness and tone that simple overlap metrics do not capture.', '''A brand assistant must be evaluated for subtle tone and practical usefulness. Which evaluation approach is most direct?
A high-stakes explanation tool needs domain experts to judge correctness and appropriateness. Which approach fits?
A team finds lexical overlap insufficient for judging the helpfulness of open-ended answers. Which approach should complement it?
A creative assistant requires nuanced assessment of whether its output satisfies a brief. Which evaluation fits?
A customer-service model needs reviewers to judge empathy and policy appropriateness. Which approach is suitable?
A team needs contextual expert judgment of a generated recommendation. Which evaluation approach fits?''')
item(3,'groundeval relevanceeval latency cost','Groundedness asks whether the response is supported by context, not just whether retrieval returned relevant passages.', '''A RAG assistant retrieves the right document but adds unsupported claims. Which evaluation dimension targets this failure?
A reviewer checks each generated statement against supplied source passages. Which quality dimension is being measured?
A team wants to know whether answers stay within the evidence in retrieved context. Which evaluation fits?
An assistant's response cites a document but invents an additional policy exception. Which dimension should be evaluated?
A model receives accurate source text yet fabricates a detail in its answer. Which evaluation dimension addresses this?
A quality check verifies that generated claims are entailed by available context. Which evaluation is this?''')
item(3,'relevanceeval groundeval latency maxtokens','Retrieval quality must be checked separately from generation; a generator cannot reliably answer from irrelevant evidence.', '''A RAG system returns passages unrelated to the question. Which evaluation dimension should be inspected first?
A support assistant's context lacks the answer even though the repository contains it. Which retrieval evaluation matters?
A team wants to measure whether selected passages actually help answer the query. Which dimension fits?
A knowledge assistant retrieves the wrong product manual. Which evaluation should identify this failure?
An engineer tests the usefulness of documents returned before generation occurs. Which evaluation is this?
A search stage misses answer-bearing passages and supplies off-topic context. Which dimension should be measured?''')
item(3,'holdout moreepochs maxcontext larger','Independent realistic prompts expose generalization failures that adaptation examples or capacity alone cannot establish.', '''A team needs an independent estimate of how an adapted assistant performs on real user tasks. What should it use?
A model performs well on its demonstration examples; the team needs evidence beyond those examples. What should it use?
An evaluation must test varied realistic users without reusing the adaptation dataset. Which resource fits?
A product team wants to detect regressions on realistic tasks before launch. Which evaluation input fits?
A fine-tuned model must be assessed without simply testing its training demonstrations. Which evaluation resource fits?
A company needs a representative, independent benchmark for a changed prompt or model. What should it maintain?''')
item(3,'quantize distill rag prompt','Lower numeric precision changes model representation and resource needs; it must be checked for quality impacts.', '''A team reduces model weight precision to lower memory requirements. Which optimization is this?
An engineer replaces higher-precision weight representations with lower-precision ones. Which technique fits?
A deployment project compresses numeric representations rather than training a student model. What technique is this?
A model needs less memory after its values are stored with fewer bits. Which optimization was applied?
A team evaluates lower-precision inference for efficiency while checking quality. Which technique is it testing?
A serving optimization reduces the bit width used to represent model values. What is this called?''')
item(3,'latency accuracy precision recall','Interactive wait time is a latency concern; correctness metrics measure different dimensions.', '''An otherwise accurate assistant takes too long to answer users. Which operational metric directly captures this issue?
A team measures elapsed time between submitting a prompt and receiving a completed response. Which metric is this?
A chatbot meets quality goals but violates its response-time objective. Which metric needs improvement?
A product manager compares how quickly two models return answers. Which metric is being compared?
An interactive tool needs a performance measure for user waiting time. Which metric fits?
A support assistant must respond within an operational time target. Which metric measures this target?''')
item(3,'keyword vector temperature maxtokens','Exact product codes and identifiers can benefit from lexical matching; semantic similarity alone may confuse nearby codes.', '''A user searches for a precise SKU and exact identifier matching is essential. Which search technique directly supports that requirement?
An archive search must locate a literal legal clause identifier. Which retrieval approach most directly fits exact matching?
A support system must match an error code exactly rather than retrieve conceptually similar errors. Which technique fits?
A catalog query targets a specific product part number. Which search method directly preserves exact term matching?
A document search must find a quoted phrase exactly as typed. Which technique most directly fits?
An audit lookup requires a literal policy identifier, not merely related policies. Which retrieval approach fits?''')
item(3,'shortprompt smallmodel maxcontext moreepochs skip','Select TWO. Remove unnecessary tokens and test an adequate smaller model; verify quality rather than assuming savings imply suitability.', '''A GenAI assistant is too costly and slow. Which TWO changes are sensible candidates to evaluate while preserving quality? (Select TWO.)
A team wants lower inference cost without abandoning quality checks. Which TWO optimizations should it evaluate? (Select TWO.)
An interactive assistant needs more efficient inference. Which TWO candidate changes address token use or model size directly? (Select TWO.)
A product team wants to reduce waste in foundation-model calls. Which TWO actions are reasonable experiments? (Select TWO.)
A support bot needs lower latency and cost under the same acceptance criteria. Which TWO changes should be tested? (Select TWO.)
A company wants more economical model responses without blindly adding capacity. Which TWO actions fit? (Select TWO.)''')
item(3,'cite sync larger moreepochs skip','Select TWO. Traceable evidence and refreshed sources improve a document-grounded workflow; neither removes the need for checking answers.', '''A RAG assistant answers from a changing policy repository. Which TWO practices improve traceability and freshness? (Select TWO.)
A knowledge bot sometimes cites stale documents and gives answers hard to audit. Which TWO actions fit? (Select TWO.)
A company wants answers linked to evidence from its latest approved documents. Which TWO practices should it adopt? (Select TWO.)
A support assistant needs current retrieved knowledge and inspectable support for its claims. Which TWO actions fit? (Select TWO.)
A document assistant must keep evidence current and make answer sources reviewable. Which TWO practices fit? (Select TWO.)
A RAG workflow needs better source accountability as its manuals change. Which TWO practices should be prioritized? (Select TWO.)''')
item(3,'curate freeze maxcontext larger skip','Select TWO. Consistent adaptation examples and independent evaluation data enable meaningful fine-tuning assessment.', '''A team prepares to fine-tune a model. Which TWO data practices support a trustworthy assessment? (Select TWO.)
An organization wants to adapt an existing model without inflating evaluation results. Which TWO practices fit? (Select TWO.)
A company has task demonstrations and plans a customization job. Which TWO practices improve the quality of the experiment? (Select TWO.)
A fine-tuning pilot must avoid conflicting supervision and evaluation leakage. Which TWO actions fit? (Select TWO.)
A model adaptation project needs reliable examples and an independent quality estimate. Which TWO practices fit? (Select TWO.)
A team wants defensible evidence that fine-tuning helps its task. Which TWO data preparation practices should it follow? (Select TWO.)''')
term('fair','Fairness assessment','Examines whether system performance and outcomes create inappropriate disparities across relevant groups.')
term('explain','Explainability','Helps people understand which factors influenced a model output or decision.')
term('transparent','Transparency','Communicates system purpose, limitations, data practices, and the role of AI to relevant stakeholders.')
term('robust','Robustness','Concerns maintaining acceptable behavior under expected variations, disturbances, or challenging inputs.')
term('privacy','Privacy protection','Limits collection, exposure, and use of personal information according to applicable requirements.')
term('safety','Safety evaluation','Assesses potential harmful outputs or consequences and the controls needed to reduce them.')
term('inclusive','Inclusive design','Considers diverse users, abilities, languages, and usage contexts in system design and evaluation.')
term('accountable','Accountability','Assigns ownership, review responsibilities, and escalation paths for AI decisions and impacts.')
term('clarify','Amazon SageMaker Clarify','Provides capabilities for detecting potential bias and explaining model predictions in supported ML workflows.')
term('modelcard','Amazon SageMaker Model Cards','Documents model purpose, evaluation results, intended uses, and risk considerations for governance.')
term('guardrails','Amazon Bedrock Guardrails','Applies configured controls such as content filters and sensitive-information handling to supported generative AI interactions.')
term('humanreview','Human review and escalation','Routes uncertain or consequential cases to qualified people instead of allowing unchecked automation.')
term('subgroups','Evaluate performance across relevant subgroups','Can reveal disparities hidden by aggregate metrics; grouping choices should be appropriate and lawful.')
term('represent','Improve representative coverage in data','Addresses missing or underrepresented operating populations, while still requiring evaluation of actual outcomes.')
term('redteam','Adversarial testing and red teaming','Probes likely misuse and failure modes with challenging inputs before and after release.')
term('appeal','Provide a review or appeal mechanism','Allows affected people to challenge consequential decisions and obtain appropriate human reconsideration.')
term('license','Check content rights and licensing','Verifies permitted use of training data and generated material instead of assuming AI removes intellectual property obligations.')
term('disclose','Disclose AI use and relevant limitations','Helps users understand that outputs are generated and may require verification.')
term('document','Document intended uses and known limitations','Creates reviewable records of scope, performance, assumptions, and risk controls.')
term('nomonitor','Stop monitoring after launch','Misses changes in risks and performance; responsible AI requires ongoing oversight.')
term('guarantee','Treat a safety filter as a complete guarantee','Overstates control effectiveness; filters can miss harmful content and need layered safeguards.')
term('averages','Use only aggregate accuracy','Can conceal uneven performance across populations and does not establish fairness or safety.')

item(4,'fair explain latency cost','The concern is unequal outcomes across relevant populations; overall quality alone does not reveal this.', '''A model has similar overall accuracy to its predecessor but performs much worse for one relevant demographic group. Which principle needs assessment?
A lending assistant makes disproportionate mistakes for a protected population. Which responsible AI dimension is most directly implicated?
A speech tool performs unequally across accents. Which principle should guide analysis of the disparity?
A hiring model has different error rates across relevant groups. Which responsible AI dimension needs attention?
A healthcare operations model systematically underserves an underrepresented population. Which principle should be examined?
An automated service ranks comparable applicants differently across relevant demographic groups. Which responsible AI concern is central?''')
item(4,'explain transparent latency privacy','Understanding factors behind a specific model output is explainability; general disclosure alone is not enough.', '''A reviewer needs to understand which input factors most influenced a model decision. Which capability fits?
A credit risk team wants to explain the drivers of an individual prediction. Which responsible AI concept fits?
A clinician asks why a research model produced a particular risk score. Which concept addresses this request?
A model owner wants feature contributions for an individual output. Which capability is relevant?
An operations manager asks which measurements led to a high failure-risk prediction. Which concept fits?
An auditor wants insight into the factors affecting a particular model result. Which responsible AI dimension fits?''')
item(4,'transparent explain robust privacy','Informing stakeholders about system use and limitations is transparency, distinct from attributing a particular prediction.', '''Users should be told that a service uses AI and what its limitations are. Which principle fits?
A company publishes information about an AI system's purpose and data practices. Which principle is this?
A chatbot interface clearly identifies generated responses and warns about limitations. Which responsible AI principle fits?
An organization explains to customers where AI is used in its workflow. Which principle is being supported?
A product page communicates how a model is intended to be used and where it may fail. Which principle fits?
A service provides clear disclosures about AI involvement and system boundaries. Which responsible AI concept is this?''')
item(4,'robust latency cost accuracy','The focus is dependable behavior under variation and challenging inputs, rather than a single average accuracy number.', '''A vision model should remain reliable when lighting conditions change within its intended setting. Which dimension is this?
A text classifier should handle common typos without major performance collapse. Which quality dimension fits?
A speech system must tolerate expected background noise. Which responsible AI dimension is relevant?
An assistant is tested against unusual but legitimate input phrasings. Which dimension does this evaluate?
An inspection model should perform acceptably under small changes in camera angle. Which quality dimension fits?
A model is assessed for stable behavior under realistic input disturbances. Which principle is this?''')
item(4,'privacy explain latency generation','Protecting personal information concerns privacy; useful model outputs do not justify unnecessary exposure.', '''A team must prevent unnecessary exposure of customer personal details in model inputs and outputs. Which principle fits?
A chatbot should not reveal one user's personal information to another. Which responsible AI dimension is central?
An organization limits collection of personal attributes for an AI pilot. Which principle guides this decision?
A model evaluation process avoids disclosing identifiable patient records to reviewers without authorization. Which principle fits?
A service masks personal information before sending data for analysis. Which principle does this support?
A company restricts how employee personal records may be used in AI applications. Which principle fits?''')
item(4,'clarify modelcard cloudtrail textract','Bias detection and prediction explanations are SageMaker Clarify capabilities; documentation or API logs alone do not perform this analysis.', '''An ML team wants AWS tooling for potential bias analysis and model explanations. Which capability fits?
A model owner needs supported SageMaker tools to investigate bias and explain predictions. Which feature fits?
An auditor requests bias metrics and feature-attribution analysis for a supported ML model. Which AWS capability fits?
A team wants an AWS capability specifically aimed at model bias analysis and explanations. Which one fits?
An organization uses SageMaker and needs tooling to understand model prediction drivers and potential bias. Which capability fits?
A data science team wants to examine potential bias during its supported model development workflow. Which SageMaker feature fits?''')
item(4,'modelcard clarify cloudwatch guardrails','A structured record of model purpose, evaluation, and risk is a model card, not an enforcement filter.', '''A governance team wants a structured record of a model's intended use, evaluation results, and risk rating. Which feature fits?
An organization needs documentation that summarizes a model's purpose and known limitations. Which SageMaker feature fits?
A model owner must maintain reviewable information about training details and evaluation results. Which feature fits?
A company wants an AWS artifact for documenting model governance information. Which capability fits?
An audit needs a centralized model record containing intended use and performance findings. Which feature fits?
A team must document model assumptions, evaluation outcomes, and risk considerations in SageMaker. Which feature fits?''')
item(4,'guardrails modelcard groundtruth s3','Configured response controls can filter supported harmful content categories, but do not guarantee the elimination of all harm.', '''A Bedrock application needs configured filters for inappropriate content and sensitive information. Which capability fits?
A GenAI team wants policy controls for supported harmful content categories in model interactions. Which Bedrock feature fits?
A chatbot should apply configured content and sensitive-data controls around supported model calls. Which feature fits?
A company wants reusable guardrail policies for supported Bedrock interactions. Which capability fits?
A support assistant needs configured filtering of disallowed content categories. Which Bedrock capability is relevant?
An application owner wants supported GenAI input and output safety controls in Bedrock. Which feature fits?''')
item(4,'humanreview moreepochs guarantee nomonitor','Consequential or uncertain outputs need appropriate human oversight and escalation, not blind reliance on automation.', '''An AI recommendation could materially affect a person's access to a service. Which control supports appropriate oversight?
An assistant is uncertain about a high-impact request. Which process is safer than automatic action?
A healthcare support system produces an ambiguous recommendation with potentially serious consequences. Which control fits?
A financial operations assistant proposes an unusual high-value action. Which process should handle the uncertainty?
A benefits assistant cannot confidently apply a policy to a consequential case. Which control is appropriate?
An AI decision support tool encounters an out-of-scope case. Which operational practice fits?''')
item(4,'inclusive cost latency quantize','Designing for varied abilities and contexts is inclusion; efficiency metrics alone do not establish accessibility.', '''A voice assistant is tested with people with different speech patterns and accessibility needs. Which principle does this support?
A product team includes users with varied abilities when designing its AI interface. Which principle fits?
A service evaluates whether its AI interaction works for different languages and assistive technologies. Which design principle fits?
A company considers diverse user needs rather than designing only for its majority customer group. Which principle is this?
A team checks whether an assistant excludes users who cannot interact through a single input mode. Which principle matters?
A public-service AI pilot includes accessibility testing with varied user communities. Which responsible AI principle fits?''')
item(4,'accountable latency precision embedding','Named ownership and escalation paths create accountability; an AI system does not remove organizational responsibility.', '''A company appoints an owner for AI incidents and defines escalation responsibilities. Which principle is this?
An AI workflow has clear decision owners and review duties. Which governance principle fits?
A firm assigns responsibility for investigating harmful AI outputs. Which principle is being operationalized?
A team documents who approves model changes and who handles resulting incidents. Which principle fits?
An organization ensures a person or group is answerable for AI system impacts. Which responsible AI concept is this?
A product has defined ownership for risk acceptance, monitoring, and remediation. Which principle fits?''')
item(4,'license temperature token maxtokens','Generative AI does not erase rights and licensing obligations; permitted uses must be reviewed.', '''A company plans to use third-party images for model adaptation. Which review is needed before assuming reuse is permitted?
A marketer wants to publish generated material that may resemble protected content. Which practice is appropriate?
A team collects external documents for an AI project. Which practice addresses intellectual property obligations?
A business assumes anything available online can be used to customize a model. Which practice should challenge that assumption?
An artist-facing AI product needs a process for reviewing permitted content use. Which practice fits?
A company evaluates whether source content and generated assets may be used commercially. Which practice is required?''')
item(4,'subgroups represent averages larger skip','Select TWO. Measure disparities and address missing coverage; improving data representation alone is not proof that fairness is achieved.', '''A model underperforms for an underrepresented user group. Which TWO actions are appropriate? (Select TWO.)
A voice service performs poorly for some accents. Which TWO actions help investigate and address this disparity? (Select TWO.)
A pilot's aggregate score hides errors for a small relevant population. Which TWO practices fit? (Select TWO.)
A company discovers its training data poorly covers some intended users. Which TWO actions should it take? (Select TWO.)
A service's error rates differ substantially across lawful, relevant population segments. Which TWO practices fit? (Select TWO.)
An AI product was developed mostly with examples from one region and fails for another. Which TWO practices are appropriate? (Select TWO.)''')
item(4,'redteam document guarantee nomonitor skip','Select TWO. Challenging tests and documented scope support risk management; a safety filter alone cannot establish safe deployment.', '''A company prepares a public-facing GenAI release. Which TWO practices strengthen responsible deployment? (Select TWO.)
A team needs evidence of likely misuse risks and clear system boundaries before launch. Which TWO actions fit? (Select TWO.)
An organization wants to understand adversarial failure modes and communicate intended uses. Which TWO practices fit? (Select TWO.)
A support assistant is ready for a risk review. Which TWO activities create useful safety evidence and scope records? (Select TWO.)
A business must assess difficult inputs and keep reviewable records of model limitations. Which TWO practices fit? (Select TWO.)
A GenAI project needs systematic stress testing and documented risk assumptions. Which TWO activities fit? (Select TWO.)''')

term('iam','AWS Identity and Access Management (IAM)','Controls which principals can perform which actions on AWS resources through policies and roles.')
term('kms','AWS Key Management Service (AWS KMS)','Manages cryptographic keys and supports encryption controls for integrated services.')
term('cloudtrail','AWS CloudTrail','Records supported AWS account activity and API events for auditing and investigation.')
term('cloudwatch','Amazon CloudWatch','Collects operational metrics and logs and supports alarms and monitoring.')
term('macie','Amazon Macie','Discovers and reports sensitive data such as personal information in Amazon S3 using managed analysis.')
term('artifact','AWS Artifact','Provides on-demand access to AWS compliance reports and agreements.')
term('config','AWS Config','Records supported resource configurations and evaluates them against configured rules.')
term('privatelink','AWS PrivateLink','Provides private connectivity to supported services through VPC endpoints without requiring public internet routing for that service traffic.')
term('tls','Encryption in transit using TLS','Protects data while it travels over a network; it is distinct from encrypting stored data.')
term('atrest','Encryption at rest','Protects stored data through encryption; authorized access and key policies still matter.')
term('least','Least-privilege access','Grants only the actions and resources necessary for a role or workload.')
term('shared','Shared responsibility model','Divides security responsibilities between AWS and the customer, depending on the services used.')
term('inject','Prompt injection','Places malicious instructions in user input or retrieved content to redirect a model away from the application intent.')
term('poison','Data poisoning','Contaminates training or adaptation data to influence the learned model behavior.')
term('exfil','Data exfiltration','Is unauthorized transfer or disclosure of data outside its permitted boundary.')
term('secrets','Managed secret storage and workload roles','Avoids embedding long-lived credentials in prompts or source code; controlled retrieval and role-based access reduce exposure.')
term('minimize','Data minimization','Collects and retains only data necessary for the approved purpose.')
term('retention','Defined retention and deletion policies','Specify how long prompts, logs, datasets, and outputs may be kept and when they must be removed.')
term('residency','Data residency and processing-location review','Checks where data is stored and processed, including applicable model and routing configurations.')
term('authz','Enforce authorization before retrieval and actions','Uses trusted application and identity controls to ensure users access only permitted records and operations.')
term('separate','Treat retrieved content as untrusted data','Separates source material from trusted instructions and avoids granting documents authority over tools or security policies.')
term('provenance','Track dataset provenance and approved use','Records source, permissions, lineage, and transformations to support auditability and appropriate data use.')
term('monitor','Monitor and investigate security-relevant activity','Uses controlled logging, alerts, and response processes to identify misuse without unnecessarily exposing sensitive content.')
term('broad','Grant broad administrator access to every caller','Violates least privilege and increases the impact of mistakes or compromise.')
term('public','Make all internal documents publicly accessible','Removes confidentiality protections and is not a safe solution to retrieval or access problems.')

item(5,'iam kms cloudtrail macie','Permission policies and roles determine access to AWS actions and resources; encryption and logs do not grant appropriate permissions.', '''A team must control which workloads can invoke a model and read a specific dataset. Which AWS service provides permission controls?
An application needs role-based permission to access only its approved AWS resources. Which service fits?
A security team wants to allow a workload to call selected AWS APIs and deny unrelated actions. Which service fits?
An AI platform must manage who can perform operations on its AWS resources. Which service provides this foundation?
A developer needs a policy governing access to model invocation actions. Which AWS service fits?
A company must restrict AWS API permissions for its AI application roles. Which service fits?''')
item(5,'kms cloudtrail cloudwatch artifact','Cryptographic key management is separate from auditing, operational monitoring, and compliance reports.', '''A company needs managed cryptographic keys for encryption in supported data services. Which AWS service fits?
An AI project requires centrally controlled encryption keys and key usage policies. Which service fits?
A dataset must use encryption backed by managed customer-controlled keys. Which AWS service is relevant?
A security team needs key management integrated with supported AWS storage services. Which service fits?
An organization wants to control encryption-key access for its supported AI data stores. Which service fits?
A company needs a managed service for creating and controlling cryptographic keys. Which AWS service fits?''')
item(5,'cloudtrail cloudwatch macie artifact','An audit of supported API activity uses CloudTrail; operational latency monitoring is a different purpose.', '''An auditor needs records of supported AWS API calls affecting an AI environment. Which service fits?
A security investigator wants to identify which principal made a supported AWS API request. Which service should be consulted?
A team needs an account activity trail for supported control-plane operations on its AI resources. Which service fits?
An organization must investigate who changed an AWS resource through supported API activity. Which service fits?
An audit requires supported AWS API event records associated with model-platform administration. Which service fits?
A security team needs evidence of supported AWS account actions for incident investigation. Which service fits?''')
item(5,'cloudwatch cloudtrail artifact kms','Metrics, operational logs, and alarms fit CloudWatch; API audit trails have a separate role.', '''A model endpoint needs alarms for elevated latency and error metrics. Which AWS service fits?
An operations team wants dashboards for its AI application's performance metrics. Which service fits?
A production assistant needs centralized operational logs and threshold-based alarms. Which service fits?
A team wants to monitor inference service health and receive alarms for failures. Which service fits?
An AI platform needs a service for collecting application metrics and logs. Which AWS service fits?
An operations engineer wants an alarm when response-time metrics cross an agreed threshold. Which service fits?''')
item(5,'macie artifact cloudwatch kms','Sensitive-data discovery in S3 is Macie; encryption alone does not identify the sensitive fields.', '''A company needs to discover personal information in Amazon S3 datasets before AI use. Which service fits?
A security team wants managed sensitive-data discovery for objects stored in S3. Which service fits?
An AI project needs to identify S3 data that may contain personal identifiers. Which AWS service fits?
A data owner wants findings about sensitive content in its S3 buckets. Which service fits?
An organization wants to assess whether an S3 training-data collection contains personal information. Which service fits?
A company needs automated analysis of supported S3 content for sensitive-data patterns. Which service fits?''')
item(5,'artifact config cloudtrail guardrails','AWS compliance reports support due diligence but do not automatically certify the customer application as compliant.', '''A compliance officer needs AWS third-party audit reports and agreements. Which service fits?
A procurement review requires access to AWS compliance documentation. Which service provides it?
A company needs available AWS audit reports to support its cloud vendor assessment. Which service fits?
An auditor asks where authorized users can obtain AWS compliance reports on demand. Which service fits?
A governance team needs AWS reports and agreements as evidence for its due diligence. Which service fits?
An organization wants to download relevant AWS compliance artifacts for review. Which AWS service fits?''')
item(5,'privatelink tls kms cloudwatch','Private service connectivity controls network paths; encryption and monitoring address separate concerns.', '''An application must access a supported AWS service through a VPC endpoint without public internet routing for that traffic. Which technology fits?
A security design requires private connectivity to a supported service from a VPC. Which AWS capability fits?
A company wants supported service traffic to use private endpoints instead of an internet gateway route. Which capability fits?
An architect needs private network access to a supported model service from a VPC. Which technology fits?
An AI workload requires private service endpoints for supported APIs. Which AWS capability fits?
A network team wants private VPC connectivity to supported AWS services. Which capability fits?''')
item(5,'shared broad public skip','AWS secures the underlying infrastructure, while customers retain duties such as data governance and application permissions, depending on the service.', '''An organization assumes a managed AI service removes all customer security duties. Which concept corrects this assumption?
A team must distinguish AWS infrastructure duties from its own data and access responsibilities. Which model applies?
A managed GenAI project still needs customer-controlled permissions and approved data use. Which concept explains this?
A company asks who is responsible for security when using managed AI services. Which framework should guide the answer?
A platform owner needs to understand which controls belong to AWS and which remain with the customer. Which concept fits?
A customer claims that AWS automatically governs all application prompts and user permissions. Which concept challenges this claim?''')
item(5,'inject poison drift overfit','Malicious instructions delivered during inference are prompt injection; contamination of a training dataset is a separate threat.', '''A retrieved page tells an assistant to ignore its instructions and reveal confidential information. Which threat is this?
A user includes hidden instructions intended to override the assistant's approved behavior. Which attack is this?
A document in a retrieval corpus instructs the model to misuse a tool when read at query time. Which threat is this?
A chatbot input attempts to redirect the model away from the application's trusted instructions. What is this called?
An attacker places operational commands inside content that a model should only summarize. Which threat fits?
A search result tries to instruct an assistant to disregard security restrictions during inference. Which attack is this?''')
item(5,'poison inject drift hallucination','Manipulating training examples to alter learned behavior is data poisoning rather than an inference-time instruction attack.', '''An attacker adds mislabeled examples to a training dataset to create harmful learned behavior. Which threat is this?
A malicious contributor contaminates model adaptation data with targeted false examples. Which attack fits?
A team discovers that an adversary altered labels before a training run. Which threat is this?
A dataset supplier inserts examples designed to make a future model misclassify a chosen target. Which attack fits?
An adversary corrupts fine-tuning data so the model learns an unwanted response pattern. Which threat is this?
A training-data collection has been intentionally manipulated to bias learned outputs. What type of attack is this?''')
item(5,'least broad public skip','Limit privileges to necessary actions and resources; more permission increases potential blast radius.', '''A model application only needs read access to one approved bucket. Which access principle should its policy follow?
A service role should invoke one model without managing unrelated resources. Which principle fits?
A labeling worker needs access only to assigned datasets. Which access principle applies?
An AI workflow should not have administrator permissions merely for convenience. Which principle guides its design?
A retrieval role needs only the minimum actions required for its approved index. Which principle fits?
A company wants to reduce the damage possible from compromised application credentials. Which access principle should it apply?''')
item(5,'residency temperature topk maxtokens','Processing location and routing must be reviewed explicitly; sampling settings do not address geographic requirements.', '''A company must ensure its AI data processing meets geographic restrictions. Which review is needed?
An organization considers cross-region model routing for a regulated dataset. Which assessment is essential?
A governance policy limits where prompts and outputs may be processed. Which review should guide service configuration?
A project must check storage and inference locations against local requirements. Which review fits?
A multinational firm needs to understand whether its selected model configuration processes data in permitted locations. Which assessment fits?
A procurement team evaluates geographic processing requirements for a managed AI service. Which review is needed?''')
item(5,'authz separate public broad skip','Select TWO. Trusted authorization and treating retrieved instructions as untrusted reduce exposure; prompts alone are not security boundaries.', '''An internal RAG assistant may encounter malicious instructions in documents. Which TWO controls should be applied? (Select TWO.)
A document assistant must not reveal restricted records or obey hostile text in retrieved pages. Which TWO controls fit? (Select TWO.)
An enterprise assistant retrieves content from multiple access-controlled repositories. Which TWO controls address unauthorized access and instruction attacks? (Select TWO.)
A support bot has retrieval and action capabilities. Which TWO controls reduce misuse from untrusted content? (Select TWO.)
An AI application must protect records while reading documents that could contain hostile instructions. Which TWO controls fit? (Select TWO.)
A company wants defense in depth against unauthorized retrieval and document-based prompt injection. Which TWO practices fit? (Select TWO.)''')
item(5,'minimize retention public broad nomonitor','Select TWO. Limit data to its approved purpose and set explicit lifecycle rules; collecting everything indefinitely increases exposure.', '''A GenAI application stores prompts that may contain personal information. Which TWO governance practices are appropriate? (Select TWO.)
A company wants to reduce unnecessary retention of sensitive AI interaction data. Which TWO practices fit? (Select TWO.)
An assistant logs customer inputs for quality review. Which TWO practices support controlled data handling? (Select TWO.)
An AI pilot collects more user data than its purpose requires and retains it indefinitely. Which TWO changes are appropriate? (Select TWO.)
A team defines a privacy-conscious lifecycle for prompt and output records. Which TWO practices should be included? (Select TWO.)
A business needs governance rules for datasets and AI interaction logs. Which TWO practices directly limit unnecessary data exposure? (Select TWO.)''')
# Targeted extensions diversify the six sets beyond the shared objective families.
# Coordinates are (set number, one-based objective number). Domain and type stay fixed.
OVERRIDES = {}
def replace(set_number, objective, keys, reason, question):
    base = ITEMS[objective - 1]
    assert not base['reason'].startswith('Select TWO.')
    OVERRIDES[(set_number, objective)] = dict(domain=base['domain'], keys=keys.split(),
        reason=reason, prompts=[question] * 6, ref=None)

term('deeplearning','Deep learning','Is a subset of ML using neural networks with multiple layers to learn representations.')
term('lex','Amazon Lex','Supports building conversational interfaces using voice and text with intent recognition and dialogue management.')
term('timeseries','Time-series data','Contains observations indexed by time; chronological evaluation helps avoid training on future information.')
term('mcp','Model Context Protocol (MCP)','Standardizes how AI applications connect to external tools and data sources; it does not itself grant authorization.')
term('memory','Agent memory management','Controls which information is retained and supplied across interactions, with privacy, relevance, and lifecycle limits.')
term('multiagent','Multi-agent orchestration','Coordinates specialized agents through defined collaboration patterns; complexity and access controls still need evaluation.')
term('contexteng','Context engineering','Selects and organizes instructions, history, retrieved evidence, and tool results available to a model at inference time.')
term('jumpstart','Amazon SageMaker JumpStart','Provides access to pretrained models and solution resources for starting supported ML and foundation-model workflows.')
term('roi','Return on investment (ROI)','Compares business benefits with the total costs of implementation and operation.')
term('opensearch','Amazon OpenSearch Service with vector capabilities','Can index embeddings and perform supported vector similarity queries for semantic retrieval.')
term('abstain','Abstain or escalate when evidence is insufficient','Avoids fabricating an answer when the available context does not support one.')
term('cpt','Continued pretraining','Further trains an existing model on a domain corpus to adapt its learned knowledge or language patterns, subject to model support.')
term('bertscore','BERTScore','Uses contextual embeddings to compare generated text with references, capturing similarities beyond exact lexical overlap.')
term('perplexity','Perplexity','Measures how well a language model predicts a token sequence; lower values on a comparable setup indicate better predictive fit, not guaranteed usefulness.')
term('cacheprompt','Prompt caching','Can reuse supported processing of repeated prompt prefixes to reduce repeated input processing under model-specific conditions.')
term('sustainable','Evaluate environmental efficiency alongside task quality','Considers resource use and whether a smaller adequate model can meet the need without unnecessary computation.')
term('feedback','Collect accessible user feedback and provide review paths','Helps identify real-world limitations and supports human-centered improvement and reconsideration.')
term('tradeoff','Evaluate interpretability and performance together','Recognizes that a more complex model may be harder to explain; deployment choices should reflect risk and user needs.')
term('veracity','Veracity','Concerns truthfulness and factual accuracy of the information an AI system produces.')
term('labelaudit','Audit annotation quality and consistency','Checks whether labels are accurate and applied consistently, rather than assuming more examples fix incorrect supervision.')
term('riskreview','Risk-based release review with documented mitigations','Evaluates likely harm, affected users, evidence, residual risk, and approval responsibilities before release.')
term('inspector','Amazon Inspector','Provides automated vulnerability management for supported workloads such as EC2 instances, container images, and Lambda functions.')
term('advisor','AWS Trusted Advisor','Provides recommendations across areas such as security, cost optimization, performance, and fault tolerance, subject to available checks and support plan.')

replace(1, 19, 'deeplearning rules clustering regression',
    'Layered neural networks characterize deep learning, which is contained within machine learning and the broader field of AI.',
    'A diagram places AI as the broadest field, ML inside AI, and multi-layer neural network methods inside ML. What label belongs on the innermost group?')
replace(2, 15, 'polly transcribe translate textract',
    'The source is written text and the desired output is speech; transcription performs the reverse conversion.',
    'A learning application has written lessons and needs natural-sounding spoken narration. Which AWS service best fits?')
replace(3, 16, 'translate comprehend polly rekognition',
    'The task is language conversion, not sentiment analysis, speech synthesis, or visual recognition.',
    'A retailer needs to convert written product descriptions from English into supported customer languages. Which AWS service fits?')
replace(4, 14, 'rekognition textract transcribe translate',
    'Object and scene analysis in photos is a computer vision task rather than structured document extraction.',
    'A media company needs to detect common objects and scenes in uploaded photographs. Which AWS service fits?')
replace(5, 17, 'lex groundtruth polly comprehend',
    'Intent recognition and managed conversational dialogue fit Amazon Lex; speech synthesis alone does not manage a conversation.',
    'A company wants a voice-and-text bot that recognizes customer intents and manages a booking dialogue. Which AWS service fits?')
replace(6, 10, 'timeseries labels embedding token',
    'Chronological observations are time-series data. A forecast evaluation should avoid allowing future observations to inform earlier predictions.',
    'A demand dataset records sales for each date. The team plans a chronological holdout to evaluate future forecasting. What type of data is central to this task?')
replace(1, 37, 'mcp finetune temperature quantize',
    'MCP is an integration protocol for tools and data. Authentication and authorization remain separate requirements.',
    'An agent platform wants a standardized protocol for connecting compatible AI applications to external tools and data. Which concept fits?')
replace(2, 38, 'memory pretrain topk batch',
    'Keeping selected interaction information across sessions is an agent-memory concern, with privacy and retention controls still required.',
    'An assistant must retain approved preferences across sessions while expiring obsolete personal details. Which agentic AI capability needs design?')
replace(3, 39, 'multiagent regression quantize token',
    'Specialized agents coordinating work constitute a multi-agent system; orchestration does not remove the need for validation.',
    'A research agent gathers evidence, a review agent checks it, and a coordinator combines their results. Which pattern is this?')
replace(4, 40, 'contexteng pretrain finetune distill',
    'Context engineering manages the information available during inference rather than changing model weights.',
    'A team assembles system instructions, relevant history, retrieved passages, and tool results for each model call. Which practice is this?')
replace(5, 41, 'jumpstart textract polly macie',
    'SageMaker JumpStart helps teams start with supported pretrained models and solution resources, not document OCR or data discovery.',
    'A team wants a SageMaker starting point for discovering and using supported pretrained models and ML solution resources. Which capability fits?')
replace(6, 42, 'roi latency perplexity temperature',
    'ROI considers benefits relative to total costs; faster inference or better language prediction alone does not establish business value.',
    'An AI project saves handling costs but also incurs model fees, integration expense, and review labor. Which metric best evaluates financial value relative to these costs?')
replace(1, 69, 'opensearch polly transcribe kms',
    'A supported vector index stores and searches embeddings; speech services and encryption-key management do not provide semantic retrieval.',
    'A team needs a managed search service with vector capabilities to store document embeddings and retrieve nearby vectors. Which listed option fits?')
replace(2, 68, 'abstain maxcontext larger skip',
    'A missing answer in the available evidence should trigger a clear limitation or escalation, not invented facts.',
    'A RAG assistant cannot find any approved source supporting an answer to a consequential policy question. What response behavior is most appropriate?')
replace(3, 60, 'cpt rag prompt inference',
    'Further broad training on domain text is continued pretraining. Labeled input-output task adaptation is a different customization pattern.',
    'A supported existing base model is further trained on a large unlabeled industry corpus to learn domain language patterns. Which adaptation process is this?')
replace(4, 61, 'bertscore bleu mae latency',
    'Contextual embeddings can capture semantic similarity even when references and outputs use different words; this still does not prove factual accuracy.',
    'An evaluator wants a reference-based generated-text metric using contextual embeddings rather than only exact n-gram overlap. Which metric fits?')
replace(5, 62, 'perplexity precision recall latency',
    'Perplexity describes predictive fit for token sequences under a comparable model and evaluation setup; it is not a comprehensive business quality metric.',
    'A language model evaluation measures how well the model predicts held-out token sequences. Which metric is commonly used for this predictive fit?')
replace(6, 67, 'cacheprompt finetune pretrain quantize',
    'Supported prompt caching can reduce processing of repeated prefixes; eligibility, cache lifetime, and pricing depend on the selected model and feature.',
    'Many requests to a supported model repeat the same long instruction prefix. Which feature can reduce repeated prefix processing without changing model weights?')
replace(1, 82, 'sustainable maxcontext larger moreepochs',
    'Environmental efficiency should be considered with quality and safety, rather than using a bigger model or more computation by default.',
    'Two models meet the same task-quality requirements, but one uses substantially fewer computational resources. Which responsible selection practice should guide comparison?')
replace(2, 83, 'feedback nomonitor guarantee averages',
    'Accessible feedback and review pathways expose user-facing failures and support meaningful human involvement.',
    'Users affected by an AI recommendation need a way to report problems and request reconsideration. Which practice supports human-centered design?')
replace(3, 73, 'tradeoff larger skip guarantee',
    'Model selection should assess explainability together with measured performance and the consequences of errors.',
    'A more accurate black-box model is harder to explain than a simpler alternative in a high-impact workflow. Which selection approach is most appropriate?')
replace(4, 75, 'veracity latency throughput privacy',
    'Veracity is about truthfulness, not speed, request volume, or personal-data handling.',
    'A reviewer checks whether the factual statements in an AI-generated report are true. Which responsible AI characteristic is being assessed?')
replace(5, 78, 'labelaudit moreepochs larger averages',
    'Incorrect or inconsistent labels create poor supervision. Inspecting annotation quality addresses the root data issue.',
    'A team discovers that annotators applied different standards to the same training categories. Which responsible data practice should come first?')
replace(6, 81, 'riskreview guarantee nomonitor skip',
    'A documented risk review links evidence, mitigations, residual risk, and approval ownership before users are exposed.',
    'Before a high-impact AI release, a team must decide whether remaining risks are acceptable and who approves deployment. Which process fits?')
replace(1, 92, 'config artifact cloudtrail kms',
    'AWS Config tracks supported resource configurations and evaluates configured rules; compliance reports and activity trails serve different purposes.',
    'A governance team wants a history of supported resource configurations and checks against configured rules. Which AWS service fits?')
replace(2, 90, 'inspector macie artifact polly',
    'Inspector addresses software vulnerabilities in supported workloads, whereas Macie focuses on sensitive data in S3.',
    'An AI application uses supported container workloads and needs automated software vulnerability findings. Which AWS service fits?')
replace(3, 91, 'advisor artifact textract transcribe',
    'Trusted Advisor supplies best-practice recommendations; it does not replace a full customer risk or compliance assessment.',
    'A platform team wants available AWS best-practice checks spanning cost, security, and performance for its environment. Which service fits?')
replace(4, 94, 'tls atrest kms cloudtrail',
    'TLS protects network transmission; encryption of stored objects addresses a different stage of the data lifecycle.',
    'An application must protect prompt data while it travels between services. Which listed control directly addresses that requirement?')
replace(5, 96, 'provenance temperature topk maxtokens',
    'Data origin, permissions, and transformations should be traceable; generation settings do not establish lineage or approved use.',
    'An auditor asks where an AI dataset came from, what permissions apply, and how it was transformed. Which governance practice provides this evidence?')
replace(6, 95, 'secrets public broad skip',
    'Long-lived credentials should not be embedded in prompts or source code. Managed secret handling and scoped workload roles provide controlled access.',
    'A developer proposes pasting API credentials into an assistant prompt so it can call a service. Which alternative is safer?')
# Additional distractor concepts used by the extension questions.
term('throughput','Inference throughput','Measures the volume of requests or tokens processed per unit time, not the truthfulness of outputs.')
