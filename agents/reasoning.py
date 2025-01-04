class ReasoningAgent:
    def __init__(self, retriever, synthesizer):
        self.retriever = retriever
        self.synthesizer = synthesizer

    def answer_query(self, query, query_embedding):
        retrieved_docs, _ = self.retriever.retrieve(query_embedding)
        if not retrieved_docs:
            return "I couldn't find any relevant information."
        return self.synthesizer.synthesize(query, retrieved_docs)