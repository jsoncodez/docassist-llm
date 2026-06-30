# Driver of loading document, reading, chunks,embeddings and vectorization.
# called on to run services and return back these steps to ask.py

from app.pdf_reader import extract_text
from app.services.chunker import chunk_text
from app.services.embeddings import get_embeddings
from app.services.llm import generate_answer
from app.services.vector_store import VectorStore


# handling document processing: PDF -> text -> chunks -> embeddings -> vector search -> LLM answer
class DocumentService:

    def __init__(self):
        self.vector_store = None
        self.document_loaded = False


    # Read Doc
    def load_document(self, pdf_path: str):


        text = extract_text(pdf_path)

        chunks = chunk_text(text)

        embeddings = get_embeddings(chunks)

        self.vector_store = VectorStore(
            dimension=len(embeddings[0])
        )

        self.vector_store.add(
            embeddings,
            chunks
        )

        self.document_loaded = True

    def search(self, question: str, top_k: int = 3):


        if not self.document_loaded:
            raise RuntimeError("No document has been loaded.")

        query_embedding = get_embeddings([question])[0]

        return self.vector_store.search(
            query_embedding,
            top_k
        )

    def ask(self, question: str):

        relevant_chunks = self.search(question)

        answer = generate_answer(
            question,
            relevant_chunks
        )

        return {
            "question": question,
            "answer": answer,
            "sources": relevant_chunks
        }

