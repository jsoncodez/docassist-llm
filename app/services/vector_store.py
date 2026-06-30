import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):

        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    # stores embeddings and the associated text chunk
    def add(self, embeddings, chunks):


        # normalize embeddings - cosine similarity
            # - meaning FAISS natively uses Euclidean distance.
            # - converts python list of vectors into numpy array, casts them float 32 data type
        embeddings = np.array(embeddings).astype("float32")
        faiss.normalize_L2(embeddings)  # modifies vectors in place (normalizes- modifies them in place resuilting in a mgnitude of 1)
            # reason for this is to make calculating cosine similiarity easier process; similar to calculating for dot product
                    #dot product - takes 2 equal length vectors and multiplies them together to produce single, regular number (aka a scalar)
                        # - used to create Weighted Sums of inputs.
        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):


        query_embedding = np.array([query_embedding]).astype("float32")
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            if idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results