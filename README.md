# CortexRAG

Production-style Retrieval-Augmented Generation (RAG) system for research papers featuring semantic search, query expansion, persistent vector storage, contextual retrieval, and local LLM-powered response generation using FastAPI, ChromaDB, and HuggingFace embeddings.

---
## Demo

### API Response Example

![CortexRAG Demo](assets/image.png)

# Features

- Research paper ingestion pipeline
- Semantic vector search using ChromaDB
- HuggingFace embedding models
- Multi-query retrieval system
- Query expansion using local LLMs
- Retrieval metadata with source tracking
- FastAPI backend for API serving
- Local LLM inference using Ollama
- Persistent vector database storage

---

# Architecture

User Query
↓
Query Expansion
↓
Semantic Retrieval
↓
Context Aggregation
↓
LLM Response Generation
↓
FastAPI API Response

---

# Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- HuggingFace Embeddings
- Ollama
- Llama3
- Semantic Search
- Vector Databases

---

# Project Structure

```bash
backend/
    app.py

source/
    dataloader.py
    splitter.py
    vectordb.py
    retriever.py
    query_expansion.py
    rag_chain.py

data/
    research papers

vector_store/
    persisted embeddings

ingest.py
```
# Retrieval Engineering Learnings

During development, multiple retrieval-quality issues emerged that required iterative experimentation and debugging.

Key observations and improvements included:

- Query expansion occasionally caused semantic drift and hallucinated technical terminology
- Multi-query retrieval introduced duplicate and low-relevance chunks
- Retrieval quality varied significantly with chunk size and overlap tuning
- Short technical queries (e.g., “What is LoRA?”) required different handling compared to descriptive queries
- Anchor-based query expansion was explored to stabilize abbreviation-heavy retrieval
- Context filtering and deduplication logic were refined to improve grounding quality
- Grounded generation prompts were added to reduce hallucinations from the local LLM
- Retrieval scores and chunk previews were exposed through the API for debugging and observability

These experiments helped improve understanding of:
- semantic vector search behavior
- embedding similarity limitations
- retrieval ranking instability
- query expansion tradeoffs
- grounding vs hallucination dynamics in RAG systems
# Setup

## Clone Repository

```bash
git clone https://github.com/ritugupta8898-cloud/CortexRAG.git
cd CortexRAG
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Ingestion

```bash
python3 ingest.py
```

## Start Backend

```bash
uvicorn backend.app:app --reload
```

---

# API Endpoint

## Chat Endpoint

```bash
GET /chat?query=your_query
```

Example:

```bash
http://127.0.0.1:8000/chat?query=(your question)
```

---

# Future Improvements

- Hybrid Retrieval
- Reranking
- Metadata Filtering
- Conversational Memory
- Frontend UI
- Streaming Responses
- Evaluation Metrics

---

# Example Use Cases

- Research paper semantic search
- AI research assistant
- Knowledge retrieval systems
- Context-aware QA systems
- NLP experimentation
