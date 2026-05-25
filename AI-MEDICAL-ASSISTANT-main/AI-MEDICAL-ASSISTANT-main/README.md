AI Medical Assistant (GenAI + Agentic AI)

A privacy-preserving, multimodal AI medical assistant built using GenAI and Agentic AI principles.
The system processes patient intake data, medical images, and clinical reports to provide safe, non-diagnostic medical guidance with strict hallucination prevention and compliance controls.

 Disclaimer:
This system is not a diagnostic or treatment tool. It does not provide medical diagnoses or prescriptions and is intended only for educational and clinical decision-support purposes.

 Key Features

 Agentic AI Architecture
Modular agents for patient intake, imaging analysis, report understanding (RAG), safety validation, and guidance generation.

 Multimodal AI (Text + Vision)
Processes medical images (e.g., MRI/X-ray) to generate non-diagnostic observations with uncertainty awareness.

 RAG-Based Medical Report Analysis
Analyzes uploaded medical PDFs using embeddings and vector search to ensure source-grounded, hallucination-free responses.

 Safety & Compliance First
Explicit safeguards prevent diagnoses, prescriptions, and overconfident claims, with automatic disclaimers and escalation guidance.

 Context Memory Across Sessions
Maintains structured patient context across multi-turn interactions for coherent medical guidance.

 Fully Local & Privacy-Preserving
Runs entirely on-device using Ollama-hosted LLMs with no external APIs or data sharing.

Tech Stack

Language: Python

LLMs: Ollama (local models)

Vision Models: Local multimodal vision-capable models

Backend: Flask

Frontend: Streamlit

RAG Pipeline: Embeddings + Vector Database

Document Parsing: PDF text extraction

Architecture: Agent-based orchestration
