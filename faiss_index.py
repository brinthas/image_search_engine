import faiss
import numpy as np

# Load FAISS index and metadata
index = faiss.read_index("search.index")
image_paths = np.load("image_paths.npy")
class_names = np.load("classes.npy")

def search_similar_images(query_embedding, k=5):
    """Searches FAISS index for similar images."""
    if query_embedding is None:
        return [], []
    faiss.normalize_L2(query_embedding)
    distances, indices = index.search(query_embedding, k)
    return indices[0], distances[0]
