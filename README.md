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
