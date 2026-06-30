from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.ask import router as ask_router

app = FastAPI(title="Document Assistant", version="1.0.0")

@app.get("/")
def root():
    return {"message": "API running"}

app.include_router(upload_router)
app.include_router(ask_router)



    #
    # from fastapi import FastAPI
    # from app.routes.upload import router as upload_router
    #
    # app = FastAPI(
    #     title="Document Assistant",
    #     version="1.0.0"
    # )
    #
    # @app.get("/")
    # def root():
    #     return {"message": "API is running"}
    #
    # app.include_router(upload_router)

    # ## TEST CODE TO SEE IF VECTOR_STORE.PY IS WORKING PROPERLY - AKA FAISS ##
    #   # FAISS VECTOR SEARCH - take user question, convert into embedding, search relevant chunks, return only those to LLM
    # from app.pdf_reader import extract_text
    # from app.services.chunker import chunk_text
    # from app.services.embeddings import get_embeddings
    # from app.services.vector_store import VectorStore
    #
    # # 1. load pdf
    # text = extract_text("data/sample.pdf")
    #
    # # 2. create chunks of text, store in chunks
    # chunks = chunk_text(text)
    #
    # # 3. embed each chunk with number vector
    # embeddings = get_embeddings(chunks)
    #
    # # 4. store those vectors
    # vector_store = VectorStore(dimension=len(embeddings[0]))
    # vector_store.add(embeddings, chunks)
    #
    # # 5. test user query
    # query = "What is the late policy?"
    #
    # query_embedding = get_embeddings([query])[0]
    #
    # results = vector_store.search(query_embedding, top_k=3)
    #
    # print("\nTop results:\n")
    #
    # for r in results:
    #     print("-", r[:200], "\n")

    # ## TEST CODE TO SEE IF EMBEDDINGS.PY IS WORKING PROPERLY ##
    # from app.pdf_reader import extract_text
    # from app.services.chunker import chunk_text
    # from app.services.embeddings import get_embeddings
    #
    # text = extract_text("data/sample.pdf")
    # chunks = chunk_text(text)
    #
    # embeddings = get_embeddings(chunks)
    #
    # print("Chunks:", len(chunks))
    # print("Embedding shape:", len(embeddings), len(embeddings[0]))

    # ## TEST CODE TO SEE IF CHUNKER.PY IS WORKING PROPERLY ##
    # from app.pdf_reader import extract_text
    # from app.services.chunker import chunk_text
    #
    # text = extract_text("data/sample.pdf")
    #
    # chunks = chunk_text(text)
    #
    # print("Total chunks:", len(chunks))
    #
    # for i, chunk in enumerate(chunks):
    #     print(f"\n--- Chunk {i+1} ---\n")
    #     print(chunk[:300])