import requests
import base64
from typing import List, Dict, Optional

OLLAMA_URL = "http://localhost:11434"


class OllamaClient:
    """
    Centralized Ollama client.
    All LLM, vision, and embedding calls go through this class.
    """

    def __init__(
        self,
        text_model: str = "llama3",
        vision_model: str = "llava",
        embedding_model: str = "nomic-embed-text"
    ):
        self.text_model = text_model
        self.vision_model = vision_model
        self.embedding_model = embedding_model

    # ------------------------------------------------------------------
    # TEXT GENERATION
    # ------------------------------------------------------------------

    def generate_text(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2
    ) -> str:
        payload = {
            "model": self.text_model,
            "prompt": prompt,
            "temperature": temperature,
            "stream": False
        }

        if system_prompt:
            payload["system"] = system_prompt

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=120
        )

        response.raise_for_status()
        return response.json().get("response", "").strip()

    # ------------------------------------------------------------------
    # VISION (IMAGE + TEXT)
    # ------------------------------------------------------------------

    def analyze_image(
        self,
        image_path: str,
        prompt: str
    ) -> str:
        """
        Sends an image + prompt to a vision-capable model (LLaVA).
        """

        with open(image_path, "rb") as f:
            image_bytes = f.read()

        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        payload = {
            "model": self.vision_model,
            "prompt": prompt,
            "images": [image_base64],
            "stream": False
        }

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=180
        )

        response.raise_for_status()
        return response.json().get("response", "").strip()

    # ------------------------------------------------------------------
    # EMBEDDINGS
    # ------------------------------------------------------------------

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        Used by RAG pipeline.
        """

        embeddings = []

        for text in texts:
            payload = {
                "model": self.embedding_model,
                "prompt": text
            }

            response = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json=payload,
                timeout=60
            )

            response.raise_for_status()
            embedding = response.json().get("embedding")
            embeddings.append(embedding)

        return embeddings
