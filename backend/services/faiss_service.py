import faiss
import numpy as np

class FaissService:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.text_store = []

    def add_vectors(self, vectors, texts):
        self.index.add(vectors)
        self.text_store.extend(texts)

    def search(self, query_vector, top_k=3):
        if self.index.ntotal == 0:
            return []

        distances, indices = self.index.search(query_vector, top_k)
        results = [self.text_store[i] for i in indices[0] if i != -1]
        return results
  
