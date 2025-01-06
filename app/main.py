from google.cloud import bigquery
import json

def generate_met_categories(output_path="app/recognition/configs/met_categories.json"):
    client = bigquery.Client()
    query = """
    SELECT
        object_number,
        object_id,
        department,
        object_name,
        title,
        culture,
        artist_display_name,
        artist_display_bio,
        object_date,
        link_resource
    FROM
        `bigquery-public-data.the_met.objects`
    GROUP BY
        object_number,
        object_id,
        department,
        object_name,
        title,
        culture,
        artist_display_name,
        artist_display_bio,
        link_resource,
        object_date
    ORDER BY
        object_date ASC
    """
    query_job = client.query(query)
    categories = [{"id": idx + 1, "name": row["category"]} for idx, row in enumerate(query_job)]
    with open(output_path, "w") as f:
        json.dump(categories, f)

if __name__ == "__main__":
    generate_met_categories()
"""
from fastapi import FastAPI
from recognition.detectron import load_model

app = FastAPI()

predictor = load_model()

@app.get("/")
def read_root():
    return {"message": "Detectron2 Met Model Inference API"}

@app.post("/predict")
def predict(image_url: str):
    from PIL import Image
    import requests
    from io import BytesIO

    # Load image from URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Run inference
    outputs = predictor(image)
    return outputs
"""