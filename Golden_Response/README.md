AI Medical Assistant (GenAI + Agentic AI)

A privacy-preserving, multimodal AI medical assistant built using GenAI and Agentic AI principles.
The system processes patient intake data, medical images, and clinical reports to provide safe, non-diagnostic medical guidance with strict hallucination prevention and compliance controls.

 Overview
This is a production-grade AI Medical Copilot architecture built with:
FastAPI backend
Streamlit frontend
Ollama local inference
ChromaDB vector retrieval
Async orchestration
Enterprise safety enforcement
Typed schemas (Pydantic)
Structured RAG pipeline
Modular AI agents
Session memory layer
Medical-safe prompting

Recommended Final Project Structure
medical-ai-platform/
│
├── backend/
│   ├── app.py
│   ├── orchestrator.py
│   ├── dependencies.py
│   ├── middleware/
│   │   ├── logging_middleware.py
│   │   └── error_handler.py
│   │
│   ├── routes/
│   │   ├── health.py
│   │   ├── sessions.py
│   │   ├── upload.py
│   │   └── analyze.py
│   │
│   ├── schemas/
│   │   ├── requests.py
│   │   ├── responses.py
│   │   └── medical.py
│   │
│   └── services/
│       ├── ollama_client.py
│       ├── vector_store.py
│       ├── embedding_service.py
│       ├── audit_logger.py
│       └── emergency_detector.py
│
├── agents/
│   ├── planner_agent.py
│   ├── intake_agent.py
│   ├── vision_agent.py
│   ├── rag_agent.py
│   ├── guidance_agent.py
│   ├── grounding_agent.py
│   └── safety_agent.py
│
├── memory/
│   └── session_memory.py
│
├── prompts/
│   └── prompts.py
│
├── frontend/
│   └── app.py
│
├── uploads/
├── chroma_db/
├── requirements.txt
├── docker-compose.yml
└── README.md

requirements.txt
fastapi
uvicorn
streamlit
requests
chromadb
sentence-transformers
pymupdf
python-multipart
pydantic
pillow
ollama



Running The Project
1. Install Ollama
Install Ollama:
https://ollama.com/download

2. Pull Models
ollama pull llama3
ollama pull llava
ollama pull nomic-embed-text

3. Install Requirements
pip install -r requirements.txt

4. Start Backend
python app.py

5. Start Frontend
streamlit run frontend/ui.py

