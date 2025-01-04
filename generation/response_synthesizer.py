class ResponseSynthesizer:
    def __init__(self, generator):
        self.generator = generator

    def synthesize(self, query, retrieved_docs):
        context = "\n".join(retrieved_docs)
        prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"
        return self.generator.generate(prompt)