from typing import Dict, Any
from llm.ollama_client import OllamaClient
from llm.prompts import GUIDANCE_PROMPT
from memory.context_store import MedicalContextStore


class GuidanceAgent:
    """
    Medical Guidance Agent

    - Provides educational, non-diagnostic guidance
    - Explains findings in plain language
    - Encourages professional consultation
    """

    def __init__(self, context_store: MedicalContextStore):
        self.context_store = context_store
        self.llm = OllamaClient()

    def execute(self) -> Dict[str, Any]:
        """
        Generate medical guidance from structured context.
        """

        context = self.context_store.get_context()

        prompt = f"""
{GUIDANCE_PROMPT}

PATIENT CONTEXT:
{context}

Generate clear, cautious medical guidance.
"""

        guidance_text = self.llm.generate_text(prompt)

        return {
            "status": "success",
            "guidance": guidance_text
        }
