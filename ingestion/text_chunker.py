from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.config import settings

class TextChunker:

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

    def split_text(self, text):
        return self.splitter.split_text(text)