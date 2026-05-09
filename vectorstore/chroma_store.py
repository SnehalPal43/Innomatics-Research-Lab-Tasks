import chromadb
from core.config import settings
from core.embeddings import EmbeddingModel

class ChromaVectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)

        self.collection = self.client.get_or_create_collection(
            name="support_docs"
        )

        self.embedding_model = EmbeddingModel()

    def add_documents(self, documents):
        embeddings = self.embedding_model.encode(documents)

        ids = [f"doc_{i}" for i in range(len(documents))]

        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query, top_k=5):
        query_embedding = self.embedding_model.encode([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]