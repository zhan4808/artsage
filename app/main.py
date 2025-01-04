#cohere trial PcSM5p7jmIf4Ck0S42BY7bHvnKGYuEREaiVVqfZb
#serpapi 6fb59283e98f42c2aa3db6c998ad2e196a567e01728548a286f56a5831e8b748
#pinecone pcsk_4uEBmr_UcuxaQHFK83vhwvq8oTjyDgHFaEjvbkeoj26EgwjqSCC4qjrzHHgwHpnsfnhM8q

from pinecone import Pinecone, ServerlessSpec
from fastapi import FastAPI, File, UploadFile
from app.capture.camera import capture_frame
from app.recognition.detectron import load_model, recognize_painting
from app.retrieval.pinecone_client import query_embedding
from app.nlp.query_processor import process_query


app = FastAPI()
model = load_model()

@app.post("/query")
async def handle_query(user_query: str):
    # 1. Capture frame
    image_path = capture_frame()

    # 2. Recognize painting
    outputs = recognize_painting(image_path, model)

    # 3. Retrieve data (mock example)
    context = "Retrieved painting metadata..."

    # 4. Process user query
    response = process_query(user_query, context)

    return {"response": response}