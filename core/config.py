import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "Smart Support RAG Assistant"

    CHROMA_DB_DIR = "vectorstore/db"

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    TOP_K_RESULTS = 5

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()