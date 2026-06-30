from sentence_transformers import SentenceTransformer


# lightweight model that runs locally
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(texts: list[str]):
    """
    Convert list of text chunks into vectors.
    """
    return model.encode(texts, show_progress_bar=True)