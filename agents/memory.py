class Memory:
    def __init__(self, retriever):
        self.retriever = retriever

    def add_memory(self, text, embedding):
        self.retriever.add_documents(np.array([embedding]), [text])

    def recall(self, query_embedding, top_k=3):
        return self.retriever.retrieve(query_embedding, top_k)