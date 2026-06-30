from fastapi import APIRouter
from pydantic import BaseModel

from app.pdf_reader import extract_text
from app.services.chunker import chunk_text
from app.services.embeddings import get_embeddings
from app.services.vector_store import VectorStore
from app.services.llm import generate_answer


router = APIRouter()

vector_store = None


class AskRequest(BaseModel):
    question: str


@router.on_event("startup")
def load_document():
    """
    In real systems, this would load a database.
    For now, we load a single PDF.
    """

    global vector_store

    text = extract_text("data/sample.pdf")
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)

    vector_store = VectorStore(dimension=len(embeddings[0]))
    vector_store.add(embeddings, chunks)


@router.post("/ask")
def ask(req: AskRequest):
    global vector_store

    # 1. embed query
    query_embedding = get_embeddings([req.question])[0]

    # 2. retrieve relevant chunks
    relevant_chunks = vector_store.search(query_embedding, top_k=3)

    # 3. generate answer
    answer = generate_answer(req.question, relevant_chunks)

    return {
        "question": req.question,
        "answer": answer,
        "sources": relevant_chunks
    }