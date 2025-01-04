import cohere

def get_text_embedding(text, api_key="your-cohere-api-key"):
    co = cohere.Client(api_key)
    response = co.embed(model="embed-english-v3.0", texts=[text])
    return response.embeddings[0]