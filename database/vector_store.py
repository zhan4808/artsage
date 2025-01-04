from retrieval.retriever import Retriever

class VectorStore:
    def __init__(self, embedding_dim):
        self.retriever = Retriever(embedding_dim)

    def add_documents(self, embeddings, docs):
        self.retriever.add_documents(embeddings, docs)

    def query(self, query_embedding, top_k=5):
        return self.retriever.retrieve(query_embedding, top_k)