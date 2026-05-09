from sentence_transformers import SentenceTransformer
from core.config import settings

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def encode(self, texts):
        return self.model.encode(texts).tolist()