import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from ingestion.pdf_loader import PDFLoader
from ingestion.text_chunker import TextChunker

from vectorstore.chroma_store import ChromaVectorStore

from workflows.graph_flow import build_graph


st.set_page_config(
    page_title="Smart Support RAG Assistant",
    layout="wide"
)

st.title("📄 Smart Support RAG Assistant")


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with open(
        f"data/{uploaded_file.name}",
        "wb"
    ) as f:

        f.write(uploaded_file.read())

    loader = PDFLoader()

    text = loader.load_pdf(
        f"data/{uploaded_file.name}"
    )

    chunker = TextChunker()

    chunks = chunker.split_text(text)

    vector_store = ChromaVectorStore()

    vector_store.add_documents(chunks)

    st.success(
        "PDF processed successfully."
    )


query = st.text_input(
    "Ask your question"
)

if st.button("Generate Answer"):

    graph = build_graph()

    result = graph.invoke({
        "query": query
    })

    st.subheader("Response")

    st.write(result["response"])