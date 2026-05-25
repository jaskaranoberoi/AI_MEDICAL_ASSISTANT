from typing import List
from llm.ollama_client import OllamaClient


class EmbeddingGenerator:
    """
    Generates embeddings using a local Ollama embedding model.
    """

    def __init__(self):
        self.client = OllamaClient()

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        """
        Convert a list of documents into embeddings.
        """
        if not documents:
            return []

        return self.client.embed_texts(documents)

    def embed_query(self, query: str) -> List[float]:
        """
        Embed a single query string.
        """
        embeddings = self.client.embed_texts([query])
        return embeddings[0]
