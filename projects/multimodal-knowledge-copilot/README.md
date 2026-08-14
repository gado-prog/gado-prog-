# 📚 Multimodal Knowledge Copilot

Search and question-answering system for mixed knowledge bases containing PDFs, images and text.

## Pipeline

`Documents → OCR/Parsing → Chunks → Embeddings → Hybrid Retrieval → Reranking → Answer + Sources`

## Highlights

- Multimodal ingestion architecture
- OCR for scanned documents
- Semantic + keyword retrieval
- Source citations and confidence metadata
- Evaluation hooks for retrieval quality

## Stack

Python · FastAPI · OCR · embeddings · vector search · PostgreSQL
