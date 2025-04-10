from fastapi import FastAPI, UploadFile, File, Query
from PIL import Image
from image_processing import extract_image_embedding
from text_processing import extract_text_embedding
from faiss_index import search_similar_images
import numpy as np

app = FastAPI()

image_paths = np.load("image_paths.npy", allow_pickle=True)

@app.post("/search/image/")
async def search_by_image(file: UploadFile = File(...)):
    """Searches for similar images using an uploaded image."""
    image = Image.open(file.file)
    query_embedding = extract_image_embedding(image)
    indices, distances = search_similar_images(query_embedding)

    # Convert NumPy types to Python native types
    results = [{"index": int(idx), "image_path": int(idx), "similarity": float(1 - dist)} for idx, dist in zip(indices, distances)]
    
    return {"results": results}

@app.post("/search/text/")
async def search_by_text(query: str = Query(..., description="Text search query")):
    """Searches for similar images using a text query."""
    query_embedding = extract_text_embedding(query)
    if query_embedding is None:
        return {"error": "Query contains restricted words"}
    indices, distances = search_similar_images(query_embedding)

    # Convert NumPy types to Python native types
    results = [{"index": int(idx), "image_path": int(idx), "similarity": float(1 - dist)} for idx, dist in zip(indices, distances)]
    
    return {"results": results}
