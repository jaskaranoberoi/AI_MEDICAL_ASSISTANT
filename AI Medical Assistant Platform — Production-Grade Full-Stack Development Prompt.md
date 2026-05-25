# **AI Medical Assistant Platform — Production-Grade Full-Stack Development Prompt**

## **Context and Role**

Being an experienced Senior Full-Stack AI Engineer and Healthcare Systems Architect focused on Agentic AI, multimodal medical systems, secure healthcare workflows, and modern AI product experiences, you have the role of developing an AI Medical Assistant Platform that is a production-grade full-stack AI system.

The platform must combine:

* agentic AI orchestration,  
* multimodal medical intelligence,  
* RAG-driven clinical report understanding,  
* local/private AI inference,  
* secure healthcare workflows,  
* modern storytelling UI/UX,  
* real-time conversational experiences,  
* safety-constrained medical knowledge,  
* enterprise-grade scalability and observability.

At the same time, this AI system should be able to deliver:

* strict safety controls,  
* privacy-focused architecture,  
* hallucination-proofing,  
* engineering with compliance in mind,  
* high-performing front-end experience

This project can be thought of as one that would fit right into-:

* modern AI copilot solutions  
* advanced healthcare software-as-a-service   
*  other enterprise AI products.

The architecture must support:

* LLM inference locally,  
* modular AI agents,  
* multimodal capabilities,  
* contextual memory,  
* secured APIs,  
* interaction pipeline.


# **Objective**

Build an entire production-ready AI Medical Assistant Platform that will:

* Employ Agentic AI framework to manage medical agents.  
* Have a capability to analyze multimodal inputs (text and medical imagery).  
* Implement Retrieval Augmented Generation (RAG) to analyze medical reports.  
* Have persistent patient context memory.  
* Do private/local LLM inference using Ollama.  
* Contain impressive frontend storytelling animations.  
* Securely handle patients' personal information.  
* Be immune to generating hallucinations and incorrect medical advice.  
* Have an easily-accessible web-based frontend.  
* Contain scalable backend infrastructure.  
* Include observability, logging, and monitoring.  
* Be thoroughly safety-checked before presenting the answer to the patient.

# **Core System Requirements**

The platform must include:

## **1\. Agentic AI Orchestration Layer**

The orchestration layer should be implemented as an entity that is tasked with the following:

* agent routing,  
* execution sequence,  
* memory management,  
* context management,   
* response composition.

The orchestrator should make the decision regarding which agents to run depending on:

* report uploads,  
* images of illnesses,  
* user-reported symptoms,  
* patient intake, and  
* user questions.

The orchestrator should facilitate:

* sequential execution,  
* conditional execution,  
* fallback execution, and  
* future multi-agent parallel execution.

The architecture should be modular and extensible.

# **Required AI Agents**

Implement the following specialized agents:

## **Intake Agent**

Duties:

* Patient intake data handling.  
* Symptoms and patient history normalization.  
* Demographic and clinical info structuring.  
* Medical entity extraction in a safe way.  
* Uncertainty maintenance.


Key Features:

* Parsing in a structured format  
* Symptom extraction  
* Risk factor tagging  
* Context enhancement

## **Vision Agent**

Duties:

* Examination of uploaded medical images.  
* Making non-diagnostic visual observations.  
* Image quality analysis.  
* Provision of uncertainty-aware outputs.


Accepted formats:

* X-rays  
* MRIs  
* Computed tomography (CT)  
* Ultrasounds  
* Laboratory test results (screenshots)


Requirements:

* Implementation based on multimodal local models via Ollama.  
* No definitive diagnoses allowed.  
* Confidence warnings included.


Vision processing has to provide:

* Asynchronous inference support  
* Efficient image preprocessing  
* UI blocking prevention

## **RAG Report Agent**

Tasks:

* Upload and process medical reports.  
* Extract and chunk PDFs.  
* Generate embeddings.  
* Store vectors in ChromaDB/PostgreSQL vector store.  
* Find grounded medical context.  
* Avoid generating answers from thin air.


Features:

* Semantic search  
* Contextual search  
* Support for source citations  
* Rank chunks  
* Index metadata


The system must:

* handle more than one report upload at a time,  
* keep retrieval history intact, and  
* ensure grounding consistency.

## **Planner Agent**

Tasks:

* Identify which agents need to be run.  
* Formulate an execution plan.  
* Optimize the inferencing process.

Illustrations:

* Bypass vision pipeline when there is no image.  
* Bypass RAG if no report is uploaded.  
* Prioritize safety if any emergency symptoms are observed.


The planner must allow:

* rule-based planning,  
* planning driven by future LLMs,  
* and conditional execution graphs

## **Guidance Agent**

Tasks:

* Combine the outputs of all agents.  
* Output guidance that is intelligible to patients.  
* Ensure medical safety in output.  
* Offer educational information.


The guidance agent needs to:

* understand multimodal context,  
* retain uncertainty, and  
* avoid unsafe claims.


The outputs need to:

* be empathic,  
* professional, and  
* non-fear inducing.


## **Safety Agent (Critical)**

Responsibilities:

* Validate ALL outputs produced.  
* Determine if output makes any unsafe medical claim.  
* Avoid:  
1.  Diagnosis,  
2. Prescription,  
3. Unsafe conclusions,  
4. Hallucination, and  
5. Overconfidence.

The safety system must:

* Enforce medical disclaimers,  
* Detect emergencies,  
* Escalate when needed, and  
* Block unsafe outputs.

Safety validations must include:

* Rule-based filtering,  
* Confidence thresholds,  
* Restricted vocabulary check,  
* Hallucination detection, and  
* Fallback actions.

Never allow an output to skip Safety Agent validation.

## **Frontend Requirements**

Use:

* Streamlit for the primary frontend interface  
* Optional future migration support for:  
  * React  
  * Next.js  
  * Framer Motion

The frontend should provide:

* a modern AI medical dashboard,  
* responsive layouts,  
* intuitive healthcare workflows,  
* and smooth interaction experiences.

The UI should feel:

* clean,  
* futuristic,  
* privacy-focused,  
* and clinically professional.

# **UI/UX REQUIREMENTS** 

The interface should resemble:

* modern AI healthcare assistants,  
* intelligent medical dashboards,  
* and privacy-first AI systems.

The experience should include:

* smooth transitions  
* responsive layouts  
* animated processing states  
* subtle motion effects  
* AI workflow visualizations  
* modern card-based layouts  
* glassmorphism-inspired panels  
* conversational AI interfaces

Optional future support:

* Framer Motion storytelling animations  
* cinematic AI product experiences

# **DASHBOARD REQUIREMENTS** 

Implement a medical AI dashboard containing:

## **Patient Intake Panel**

Features:

* symptom input  
* demographic information  
* medical history input  
* structured patient intake forms

## **Upload Center**

Support:

* PDF uploads  
* medical image uploads  
* drag-and-drop interaction

Supported formats:

* PDF  
* PNG  
* JPG  
* JPEG

## **AI Processing Workflow**

Visualize:

* planner agent execution  
* active AI agents  
* report analysis stages  
* image analysis stages  
* safety validation pipeline

## **AI Chat Interface**

Features:

* conversational interaction  
* markdown rendering  
* typing indicators  
* streaming AI responses  
* contextual continuity

## **Patient Context Memory**

Display:

* extracted findings  
* uploaded reports  
* imaging observations  
* contextual patient memory

# **BACKEND REQUIREMENTS** 

Use:

* Python  
* Flask  
* Ollama  
* ChromaDB  
* Sentence Transformers

The backend must support:

* agent orchestration  
* multimodal inference  
* report ingestion  
* vector retrieval  
* contextual memory  
* streaming AI responses  
* secure local inference  
* safety validation pipelines

# **API REQUIREMENTS** 

Implement Flask endpoints for:

## **Patient Analysis**

Support:

* intake processing  
* image analysis  
* report ingestion  
* AI response generation

## **Session Management**

Support:

* session creation  
* session retrieval  
* patient context updates

## **Upload Handling**

Implement:

* secure file uploads  
* MIME validation  
* upload size limits  
* PDF extraction  
* image preprocessing

## **Health Monitoring**

Provide:

* Flask health endpoint  
* Ollama availability checks  
* vector database status

# **PRIVACY & COMPLIANCE REQUIREMENTS** 

The system must prioritize:

* local AI inference,  
* privacy-preserving workflows,  
* and secure patient handling.

Requirements:

* fully local Ollama-hosted models  
* no external AI APIs  
* local vector storage  
* secure environment variables  
* minimal data retention  
* safe medical response constraints

The architecture should follow:

* privacy-first AI engineering  
* healthcare-safe AI workflows  
* hallucination prevention principles

# **DATABASE & MEMORY REQUIREMENTS** 

Use:

* ChromaDB for vector retrieval  
* Python memory layers for session context

Store:

* uploaded report embeddings  
* retrieval metadata  
* contextual memory  
* imaging findings  
* agent outputs

Optional future support:

* SQLite  
* PostgreSQL  
* Redis caching

# **RAG PIPELINE REQUIREMENTS** 

Implement:

## **Document Parsing**

* PDF extraction using PyMuPDF  
* report chunking  
* metadata tagging

## **Embeddings**

Use:

* Sentence Transformers  
* local embedding models

## **Retrieval**

Features:

* semantic similarity search  
* top-k retrieval  
* source-grounded responses  
* hallucination prevention

Responses must:

* remain grounded in uploaded reports,  
* preserve uncertainty,  
* and avoid unsupported medical claims.

# **AI MODEL REQUIREMENTS** 

Use local models via Ollama.

Examples:

* llama3  
* mistral  
* phi  
* llava

Support:

* multimodal processing  
* configurable model pipelines  
* local inference  
* streaming generation

# **PERFORMANCE REQUIREMENTS** 

Optimize:

* local inference latency  
* Streamlit responsiveness  
* embedding performance  
* image processing efficiency  
* vector retrieval speed

Implement:

* lazy loading where possible  
* async processing  
* caching  
* efficient memory usage

Ensure:

* responsive UI performance  
* smooth interaction flow  
* scalable local execution

# **DEPLOYMENT REQUIREMENTS** 

Support deployment using:

* local machine execution  
* Docker  
* Docker Compose

Optional future deployment:

* cloud-hosted Flask backend  
* Vercel frontend migration  
* GPU inference deployment

Include:

* environment variable setup  
* Ollama installation guide  
* model download instructions  
* local execution steps

# **EXPECTED FINAL OUTPUT** 

The final system should deliver:

* A privacy-preserving AI medical assistant.  
* Agentic AI orchestration.  
* Multimodal medical understanding.  
* RAG-powered report analysis.  
* Safe non-diagnostic guidance.  
* Local AI inference using Ollama.  
* Context-aware patient memory.  
* Modern AI healthcare dashboard.  
* Hallucination-resistant medical responses.  
* Modular and scalable architecture.

The final product should feel like:

* a next-generation medical AI copilot,  
* a multimodal healthcare assistant,  
* and a privacy-first clinical AI workflow system.

  .

  .

