from typing import List, Dict
import chromadb
from chromadb.config import Settings
from vector_store.embeddings import EmbeddingGenerator


class ChromaVectorStore:
    """
    ChromaDB wrapper for medical RAG.
    """

    def __init__(self, collection_name: str = "medical_reports"):
        self.embedding_generator = EmbeddingGenerator()

        self.client = chromadb.Client(
            Settings(
                persist_directory="./chroma_db",
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=None  # we supply embeddings manually
        )

    # --------------------------------------------------
    # INGEST DOCUMENTS
    # --------------------------------------------------

    def add_documents(self, documents: List[Dict[str, str]]):
        """
        documents: [
            {
                "id": str,
                "text": str,
                "source": str
            }
        ]
        """

        texts = [doc["text"] for doc in documents]
        embeddings = self.embedding_generator.embed_documents(texts)

        ids = [doc["id"] for doc in documents]
        metadatas = [{"source": doc["source"]} for doc in documents]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        self.client.persist()

    # --------------------------------------------------
    # QUERY
    # --------------------------------------------------

    def query(self, query: str, top_k: int = 3) -> List[Dict[str, str]]:
        """
        Retrieve top-k relevant document chunks.
        """

        query_embedding = self.embedding_generator.embed_query(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        retrieved = []
        for doc, meta in zip(documents, metadatas):
            retrieved.append({
                "text": doc,
                "source": meta.get("source", "unknown")
            })

        return retrieved
