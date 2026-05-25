AI Medical Assistant (GenAI + Agentic AI)

A privacy-preserving, multimodal AI Medical Assistant built using Generative AI, Agentic AI, RAG pipelines, and local LLM inference.

The system processes:

Patient intake information
Medical reports
Medical images
Clinical queries

to provide safe, non-diagnostic medical guidance with strong hallucination prevention and privacy-first architecture.

Disclaimer

This project is NOT a diagnostic or treatment system.

It does NOT provide:

medical diagnoses
prescriptions
emergency decisions
clinical treatment plans

The platform is intended strictly for:

educational purposes
AI research
healthcare AI experimentation
clinical decision-support assistance

Always consult licensed medical professionals for real medical advice.

Features
Agentic AI Architecture

The platform uses modular AI agents for:

Patient Intake Processing
Medical Image Understanding
Medical Report Analysis
RAG Retrieval
Safety Validation
Guidance Generation
Context Memory
Multimodal AI

Supports:

Text understanding
Medical image analysis
Clinical report analysis

Example image types:

MRI
X-ray
CT scan
Ultrasound screenshots

The system produces:

non-diagnostic observations
uncertainty-aware responses
grounded AI outputs
RAG-Based Medical Report Analysis

Implements Retrieval-Augmented Generation using:

PDF parsing
embeddings
vector search
semantic retrieval

This helps:

reduce hallucinations
ground responses in uploaded reports
preserve medical context
Safety & Compliance First

Built-in safeguards prevent:

diagnoses
prescriptions
unsafe medical claims
overconfident outputs

Includes:

automatic disclaimers
escalation recommendations
uncertainty-aware generation
response validation
Context Memory

Maintains structured patient context across sessions:

intake history
uploaded reports
extracted findings
prior AI interactions
Fully Local & Privacy-Preserving

Runs entirely on-device using:

Ollama
local embeddings
local vector DB

No external AI APIs are required by default.

Tech Stack
Backend
Python
Flask
AI & ML
Ollama
Sentence Transformers
ChromaDB
ONNX Runtime
RAG Pipeline
PDF text extraction
Embeddings
Vector retrieval
Semantic search
Frontend (Planned / Optional)
Streamlit
Next.js
React
Tailwind CSS
Framer Motion
Project Structure
AI-MEDICAL-ASSISTANT/
│
├── agents/
│   ├── intake_agent.py
│   ├── imaging_agent.py
│   ├── rag_report_agent.py
│   ├── safety_agent.py
│   └── guidance_agent.py
│
├── memory/
│   └── context_store.py
│
├── vector_store/
│   └── chroma_store.py
│
├── uploads/
│
├── data/
│   ├── reports/
│   └── images/
│
├── app.py
├── orchestrator.py
├── requirements.txt
└── README.md
Installation
1. Clone Repository
git clone <your-repo-url>
cd AI-MEDICAL-ASSISTANT
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Ollama Setup
Install Ollama

Download:

Ollama Official Website

Pull Local LLM
ollama pull llama3

Optional models:

ollama pull mistral
ollama pull phi3
ollama pull llava
Start Ollama Server
ollama serve
Running the Backend

Start Flask API:

python app.py

Server runs on:

http://127.0.0.1:5000
API Endpoints
Health Check
GET
/health

Response:

{
  "status": "ok"
}
Patient Analysis
POST
/analyze
Example Request
{
  "intake": {
    "age": 45,
    "gender": "Male",
    "symptoms": ["headache", "fatigue"]
  },
  "reports": [
    {
      "id": "r1",
      "text": "Patient shows mild inflammatory changes.",
      "source": "report.pdf"
    }
  ],
  "user_query": "Summarize the findings."
}
Example CURL Request
curl -X POST http://127.0.0.1:5000/analyze \
-H "Content-Type: application/json" \
-d @test_request.json
AI Workflow
Step 1 — Intake Processing

Patient symptoms and metadata are analyzed.

Step 2 — Medical Report Retrieval

Uploaded reports are embedded and retrieved semantically.

Step 3 — Image Understanding

Medical images are analyzed using multimodal AI.

Step 4 — Safety Validation

Responses pass through safety constraints.

Step 5 — Guidance Generation

The final grounded response is generated.

Hallucination Prevention

The system minimizes hallucinations using:

RAG grounding
source-aware retrieval
constrained prompting
safety validation
uncertainty handling
Security & Privacy

Features include:

Local inference
No external API dependency
Minimal data retention
Safe upload handling
Vectorized document retrieval
Privacy-first architecture
Supported File Types
Reports
PDF
Images
PNG
JPG
JPEG
Future Improvements
Next.js frontend dashboard
Real-time streaming responses
WebSocket support
JWT authentication
PostgreSQL integration
Redis caching
OCR support
Docker deployment
Kubernetes scaling
Monitoring dashboards
Advanced multimodal models
Known Limitations
Not medically certified
Non-diagnostic system
Research prototype
Requires local hardware resources
Large models may require GPU acceleration
Troubleshooting
ChromaDB Telemetry Warnings

These warnings are harmless:

Failed to send telemetry event ...
ONNX Runtime DLL Errors

Fix using:

pip install msvc-runtime
pip install onnxruntime==1.17.3
Ollama Not Found

Install Ollama and restart terminal:

Ollama Download

License

MIT License

Author

Developed as a research-focused AI healthcare assistant project using:

GenAI
Agentic AI
RAG
Multimodal AI
Privacy-Preserving AI Systems
