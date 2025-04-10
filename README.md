## Amazon Image-Based Search Engine

This project is a scalable image search engine powered by CLIP embeddings, FAISS for efficient similarity search, FastAPI as a high-performance backend framework, and Streamlit for an intuitive and interactive frontend interface.

It enables users to:

•	Upload an image and retrieve visually similar products from a dataset.

•	Input a text query and receive product images matching the description.

•	Upload PDF or DOCX documents and extract keywords to perform a semantic image search.

With its modular client-server architecture, this solution is easy to deploy, extend, and integrate into broader e-commerce workflows. This project is designed for datasets of approximately 10,000 product images, making it suitable for mid-sized retail catalogs or prototypes.
Architecture Overview 

 `Streamlit (Frontend)   ⇄   FastAPI (Backend)   ⇄   FAISS + Embedding Models (CLIP, Sentence Transformers)` 

The system is split into two independent components:

•	A frontend client where users upload inputs and view results.

•	A backend server that handles preprocessing, embedding generation, similarity search, and filtering.

CLIP is used to generate feature embeddings for both images and text, while FAISS allows for fast approximate nearest-neighbor search. The backend also applies a simple text filtering system to block inappropriate queries using a configurable banned word list.
Project Directory Structure

`repo/`

`├── backend/`

`│   ├── api1.py               # FastAPI application`

`│   ├── image_processing.py   # Functions to preprocess image files`

`│   ├── text_processing.py    # Functions for processing text inputs`

`│   ├── faiss_index.py        # FAISS indexing and search logic`

`│   ├── banned_words.py       # List of filtered/offensive terms`

`│   ├── requirements.txt      # Backend Python dependencies`

`├── frontend/`

`│   ├── app1.py               # Streamlit client interface`

`│   ├── requirements.txt      # Frontend Python dependencies`

`├── data/`

`│   ├── image_paths.npy       # Numpy array of image paths`

`│   ├── classes.npy           # Labels or categories for images`

`│   ├── search.index          # Serialized FAISS index`

`├── README.md`

To generate these .npy and .index files, ensure your dataset is preprocessed and embeddings are extracted. A generate_index.py script is recommended (not included here).
________________________________________

## Getting Started
### 1. Clone the Repository

git clone https://github.com/your-username/image-search-engine.git
cd image-search-engine

### 2. Set Up the Backend (FastAPI API Server)

cd backend

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn api1:app --host 0.0.0.0 --port 8002

This will launch the API on http://127.0.0.1:8002.

### 3. Set Up the Frontend (Streamlit App)

Open a separate terminal window:

cd frontend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

streamlit run app1.py

The Streamlit interface will automatically connect to the backend server and be accessible in your web browser.
Python 3.8+ is recommended. Make sure the required .npy and .index files are present in the data/ directory.
________________________________________
### Key Notes

•	Backend uses CLIP (via sentence-transformers) to compute embeddings.

•	PDF/DOCX documents are parsed and passed through the same text embedding pipeline.

•	Streamlit displays the top-K similar images along with similarity scores.

•	Backend responses are JSON-based, and frontend dynamically renders the results.
________________________________________
### Example Use Case

Upload or drag an image (e.g., a shoe, bag, or watch) or describe it using a short phrase like:

"stationery"

The system will return the top 5 most visually or semantically similar product images from the dataset.

![image](https://github.com/user-attachments/assets/e5244894-508d-4689-9ac8-0dce426c1b16)

 
This system can be adapted for retail, visual search engines, fashion tech platforms, and educational tools involving content-based retrieval.
________________________________________
### License

This project is released under the MIT License. You are free to use, modify, and distribute it.
For more details, see the LICENSE file.

