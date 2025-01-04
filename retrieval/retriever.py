import faiss
import numpy as np

class Retriever:
    def __init__(self, embedding_dim, index_path=None):
        self.embedding_dim = embedding_dim
        if index_path:
            self.index = faiss.read_index(index_path)
        else:
            self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = []

    def add_documents(self, embeddings, docs):
        self.index.add(embeddings)
        self.documents.extend(docs)

    def retrieve(self, query_embedding, top_k=5):
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        results = [self.documents[i] for i in indices[0] if i < len(self.documents)]
        return results, distances[0]

    def save_index(self, path):
        faiss.write_index(self.index, path)