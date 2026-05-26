from typing import Dict, Any
from llm.ollama_client import OllamaClient
from llm.prompts import VISION_PROMPT
from tools.image_loader import load_medical_image
from memory.context_store import MedicalContextStore


class VisionAgent:
    """
    Vision Agent for MRI / X-ray / scan analysis.

    - Uses Ollama vision model (e.g., LLaVA)
    - Produces observations ONLY
    - NO diagnosis
    - NO medical claims
    """

    def __init__(self, context_store: MedicalContextStore):
        self.context_store = context_store
        self.llm = OllamaClient()

    def execute(self, image_path: str) -> Dict[str, Any]:
        """
        image_path: path to uploaded medical image
        """

        # Step 1: Validate & load image (no AI yet)
        image_info = load_medical_image(image_path)

        # Step 2: Vision model prompt
        prompt = f"""
{VISION_PROMPT}

Image metadata:
- Format: {image_info['format']}
- Mode: {image_info['mode']}
- Size: {image_info['size']}

Describe only what is visually observable in this image.
"""

        # Step 3: Call Ollama vision model
        response_text = self.llm.analyze_image(
            image_path=image_path,
            prompt=prompt
        )

        # Step 4: Build safe findings object
        findings = {
            "observations": response_text,
            "confidence": "moderate",
            "note": (
                "These observations are non-diagnostic and require "
                "review by a qualified medical imaging specialist."
            )
        }

        # Step 5: Store in structured medical context
        self.context_store.update_imaging(findings)

        return {
            "status": "success",
            "message": "Image analyzed successfully (non-diagnostic).",
            "findings": findings
        }
