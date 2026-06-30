import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        # FAISS index for cosine similarity (using inner product)
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embeddings, chunks):
        """
        Store embeddings + associated text chunks
        """

        # normalize embeddings for cosine similarity
        embeddings = np.array(embeddings).astype("float32")
        faiss.normalize_L2(embeddings)

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        """
        Find most relevant chunks for a query
        """

        query_embedding = np.array([query_embedding]).astype("float32")
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            if idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results