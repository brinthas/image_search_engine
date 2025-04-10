import torch
import faiss
import numpy as np
from PIL import Image
from sentence_transformers import SentenceTransformer

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer("sentence-transformers/clip-ViT-B-32").to(device)

def extract_image_embedding(image):
    """Extracts and normalizes image embeddings."""
    if image.mode != "RGB":
        image = image.convert("RGB")
    with torch.no_grad():
        embedding = model.encode([image], convert_to_tensor=True).cpu().numpy().astype(np.float32)
    faiss.normalize_L2(embedding)
    return embedding
