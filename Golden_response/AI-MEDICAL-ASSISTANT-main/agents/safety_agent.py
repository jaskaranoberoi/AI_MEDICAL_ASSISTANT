from typing import Dict, Any
from llm.ollama_client import OllamaClient
from llm.prompts import SAFETY_PROMPT


class SafetyAgent:
    """
    Medical Safety & Compliance Agent

    This agent ALWAYS runs last.
    It reviews AI-generated content and enforces:
    - No diagnosis
    - No prescriptions
    - No certainty
    - Mandatory disclaimers
    """

    def __init__(self):
        self.llm = OllamaClient()

        self.blocked_terms = [
            "diagnosis",
            "diagnosed",
            "you have",
            "this means you have",
            "treatment",
            "medication",
            "prescribe",
            "cure",
            "disease",
            "condition",
            "definitive",
            "certainly",
            "confirmed"
        ]

    def execute(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        response: output from GuidanceAgent
        """

        text = response.get("guidance", "")

        # Step 1: Hard safety check (string-based)
        lowered = text.lower()
        for term in self.blocked_terms:
            if term in lowered:
                text = self._rewrite_unsafely_strong_text(text)
                break

        # Step 2: Ensure disclaimer is present
        if "consult" not in text.lower():
            text += self._default_disclaimer()

        return {
            "status": "safe",
            "final_output": text
        }

    # --------------------------------------------------
    # INTERNAL METHODS
    # --------------------------------------------------

    def _rewrite_unsafely_strong_text(self, text: str) -> str:
        """
        Use LLM to soften unsafe medical language.
        """

        prompt = f"""
{SAFETY_PROMPT}

CONTENT TO REVIEW:
{text}

Rewrite this to be medically safe.
"""

        return self.llm.generate_text(prompt)

    def _default_disclaimer(self) -> str:
        return (
            "\n\n⚠️ **Important Medical Disclaimer**:\n"
            "This information is for general educational purposes only "
            "and is not a medical diagnosis or treatment recommendation. "
            "Please consult a qualified healthcare professional for "
            "personalized medical advice."
        )
