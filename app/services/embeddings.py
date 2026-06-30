from sentence_transformers import SentenceTransformer

# ollama model
model = SentenceTransformer("all-MiniLM-L6-v2")

# converting text chunks to vectors
def get_embeddings(texts: list[str]):

    return model.encode(texts, show_progress_bar=True)