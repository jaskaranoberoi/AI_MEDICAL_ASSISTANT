from typing import Dict, Any, List
from llm.ollama_client import OllamaClient
from llm.prompts import RAG_REPORT_PROMPT
from vector_store.chroma_store import ChromaVectorStore
from memory.context_store import MedicalContextStore


class RAGReportAgent:
    """
    Retrieval-Augmented Generation agent for medical reports.

    - Answers ONLY from retrieved documents
    - Refuses if evidence is insufficient
    - No hallucination by design
    """

    def __init__(self, context_store: MedicalContextStore):
        self.context_store = context_store
        self.vector_store = ChromaVectorStore()
        self.llm = OllamaClient()

    def ingest_reports(self, documents: List[Dict[str, str]]):
        """
        documents: [
            {"id": str, "text": str, "source": str}
        ]
        """
        self.vector_store.add_documents(documents)

    def execute(self, query: str) -> Dict[str, Any]:
        """
        query: user question about uploaded reports
        """

        retrieved_docs = self.vector_store.query(query)

        if not retrieved_docs:
            return {
                "answer": (
                    "The provided documents do not contain sufficient "
                    "information to answer this question safely."
                ),
                "sources": []
            }

        # Build grounded context
        context_text = "\n\n".join(
            f"[Source: {doc['source']}]\n{doc['text']}"
            for doc in retrieved_docs
        )

        prompt = f"""
{RAG_REPORT_PROMPT}

DOCUMENTS:
{context_text}

QUESTION:
{query}
"""

        answer = self.llm.generate_text(prompt)

        # Store summary in medical context
        self.context_store.add_report_summary({
            "question": query,
            "answer": answer,
            "sources": list(set(doc["source"] for doc in retrieved_docs))
        })

        return {
            "answer": answer,
            "sources": list(set(doc["source"] for doc in retrieved_docs))
        }
