import pinecone

def insert_embedding(index_name, id, embedding):
    index = pinecone.Index(index_name)
    index.upsert([(id, embedding)])

def query_embedding(index_name, embedding, top_k=5):
    index = pinecone.Index(index_name)
    results = index.query(embedding, top_k=top_k, include_metadata=True)
    return results