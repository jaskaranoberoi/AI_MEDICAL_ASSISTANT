# AI MEDICAL ASSISTANT
<img width="958" height="446" alt="image" src="https://github.com/user-attachments/assets/fa552628-344a-4320-8984-c947b8677da9" />


A production-style Healthcare AI Copilot platform built using:

- FastAPI
- Streamlit
- Ollama
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- Vision AI
- Async AI orchestration
- Enterprise-grade safety validation

This platform demonstrates how to build a privacy-first local healthcare AI system with modular AI agents, grounded retrieval, medical safety enforcement, and scalable architecture.

---

# Important Disclaimer

This project is intended for:

- Educational purposes
- AI architecture demonstrations
- Research and experimentation

This platform is NOT:

- A medical device
- FDA approved
- Clinically validated
- Intended for diagnosis or treatment

Always consult licensed healthcare professionals.

---

# Features

## Core AI Features

- Multi-agent orchestration
- Medical-safe prompting
- RAG-based report understanding
- Vision AI using LLaVA
- Session memory
- Grounded response generation
- Safety validation layer
- Emergency symptom detection
- Local inference with Ollama
- Docker deployment
- Production-style modular architecture

---

# AI Agents

| Agent | Responsibility |
|---|---|
| PlannerAgent | Determines workflow execution |
| IntakeAgent | Extracts symptoms and urgency |
| RAGAgent | Retrieves contextual report information |
| VisionAgent | Observes uploaded medical images |
| GuidanceAgent | Generates educational guidance |
| GroundingAgent | Prevents hallucinations |
| SafetyAgent | Blocks unsafe medical claims |

---

# Project Structure

```text
medical-ai-platform/
│

│── app.py
│── orchestrator.py
│── middleware/
├── logging_middleware.py
│      └── error_handler.py
│
│── routes/
│── analyze.py
│── upload.py
│── sessions.py
│      └── health.py
│   
│── schemas/
│      ├── requests.py
│      └── responses.py
│   
│── services/
│       ├── ollama_service.py
│       ├── chroma_service.py
│       ├── audit_logger.py
│       └── emergency_detector.py
│
├── agents/
│   ├── planner_agent.py
│   ├── intake_agent.py
│   ├── rag_agent.py
│   ├── vision_agent.py
│   ├── guidance_agent.py
│   ├── grounding_agent.py
│   └── safety_agent.py
│
├── rag/
│   ├── pdf_ingestor.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── memory/
│   └── session_memory.py
│
├── prompts/
│   └── prompts.py
│
├── frontend/
│   └── ui.py
│
├── uploads/
├── chroma_db/
├── requirements.txt
├── docker-compose.yml
└── README.md


Technology Stack
Layer	Technology
Backend API	FastAPI
Frontend	Streamlit
LLM Runtime	Ollama
Vision Model	LLaVA
Text Model	Llama3
Embeddings	all-MiniLM-L6-v2
Vector Database	ChromaDB
PDF Parsing	PyMuPDF
Validation	Pydantic
Deployment	Docker
Safety Architecture

The platform includes multiple healthcare safety layers.

Safety Features
Rule-based filtering
Unsafe output blocking
Confidence disclaimers
No diagnosis enforcement
No prescription enforcement
Emergency symptom detection
Grounding verification
Educational-only guidance
RAG Pipeline

The Retrieval-Augmented Generation pipeline supports:

PDF ingestion
Semantic chunking
Embeddings generation
Vector retrieval
Grounded AI responses
Supported File Types
PDF
PNG
JPG
JPEG
Vision AI

Medical images are analyzed using:

Ollama
LLaVA multimodal model

The system:

Describes observations
Mentions uncertainty
Refuses diagnosis
Avoids medical claims
Session Memory

The memory layer stores:

Conversation history
Uploaded files
Agent outputs
Workflow state
Current Storage
In-memory session storage
Recommended Production Upgrades
Redis
PostgreSQL
Encrypted persistence
Installation
1. Clone Repository
git clone <repo-url>
cd medical-ai-platform
Install Dependencies
pip install -r requirements.txt
Install Ollama

Download Ollama from:

https://ollama.com

Verify installation:

ollama serve
Pull Required Models
ollama pull llama3
ollama pull llava
ollama pull nomic-embed-text
Run Backend
cd backend
python app.py

Backend URL:

http://localhost:8000
Run Frontend
streamlit run frontend/ui.py

Frontend URL:

http://localhost:8501
Docker Deployment
Start Containers
docker-compose up --build
API Endpoints
Endpoint	Method	Purpose
/health	GET	Health check
/session	POST	Create session
/upload	POST	Upload files
/analyze	POST	Run AI analysis
Example Analyze Request
{
  "session_id": "demo-session",
  "query": "Patient has headache and fatigue"
}
Future Production Upgrades
Infrastructure
Redis caching
PostgreSQL persistence
Celery workers
Kubernetes deployment
GPU inference scaling
WebSocket streaming
AI Enhancements
Medical fine-tuned models
Structured JSON outputs
Citation generation
Confidence scoring
Hallucination verification
Multi-agent memory graphs
Security
JWT authentication
OAuth2
HTTPS reverse proxy
Audit logging
PHI redaction
Encryption-at-rest
Privacy Design

This platform is privacy-focused.

Key Principles
Local inference
No cloud AI APIs
Minimal data retention
Session isolation
Secure uploads
