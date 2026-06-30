# Document Assistant

An AI-powered document assistant that allows users to upload PDFs and ask natural language questions about their contents.

## Features

- Extract text from PDF documents
- FastAPI backend
- Retrieval-Augmented Generation (RAG) *(coming soon)*
- Local LLM support with Ollama *(coming soon)*

## Tech Stack

- Python
- FastAPI
- PyPDF
- Git

## Current Progress

- [x] Project setup
- [x] PDF text extraction
- [x] File upload API
- [x] Embeddings
- [x] FAISS vector search
- [x] LLM integration
- [ ] Refactor allowing new data to be parsed. 
  - (need to connect /upload and /ask; document rebuilt every time app starts; remove temp file being written)
- [ ] Front End
- [ ] Docker implementation
- [ ] Deploy