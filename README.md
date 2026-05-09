# Smart Support RAG Assistant

## Project Overview
Smart Support RAG Assistant is an AI-powered customer support system built using Retrieval-Augmented Generation (RAG), LangGraph, and ChromaDB.

The system processes PDF documents, stores embeddings in a vector database, retrieves relevant context, and generates intelligent responses for user queries.

It also supports Human-in-the-Loop (HITL) escalation for unresolved or complex queries.

---

## Features

- PDF Knowledge Base Processing
- Text Chunking
- Embedding Generation
- ChromaDB Vector Storage
- Context Retrieval
- AI-based Response Generation
- LangGraph Workflow Routing
- Human Escalation System
- Streamlit Web Interface

---

## Technologies Used

- Python
- Streamlit
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformers
- PyPDF
- OpenAI
- HuggingFace Embeddings

---

## Project Structure

```bash
smart-support-rag-assistant/
│
├── app
├── data
├── docs
├── ui
├── core
├── workflows
├── vectorstore
├── ingestion
├── prompts
├── escalations
├── tests
└── assets