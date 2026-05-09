from vectorstore.chroma_store import ChromaVectorStore

class ContextRetriever:

    def __init__(self):
        self.vector_store = ChromaVectorStore()

    def retrieve(self, query):
        results = self.vector_store.search(query)

        return "\n".join(results)