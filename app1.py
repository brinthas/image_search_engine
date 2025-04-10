import streamlit as st
import requests
from PIL import Image
import os
import numpy as np

# Load image paths
image_paths = np.load("image_paths.npy", allow_pickle=True)

API_URL = "http://127.0.0.1:8002"

st.title("Amazon Image-Based Search Engine")
st.caption("Amazon catalog ~10k data")

option = st.selectbox("Select search method", ["Upload Image", "Enter Text", "Upload Document (PDF/DOCX)"])

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        query_image = Image.open(uploaded_file)
        st.image(query_image, caption="Uploaded Image", width=150)
        
        # Send image to API
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{API_URL}/search/image/", files=files)
        
        if response.status_code == 200:
            results = response.json().get("results", [])
            st.write("### Similar Images:")
            cols = st.columns(min(5, len(results)))
            
            for i, result in enumerate(results):
                similarity = result["similarity"] * 100
                image_path = image_paths[result["image_path"]]
                index = result["index"]
                
                if os.path.exists(image_path):
                    retrieved_img = Image.open(image_path)
                    cols[i % len(cols)].image(retrieved_img, caption=f"Index: {index} | Similarity: {similarity:.1f}%", width=128)
                else:
                    cols[i % len(cols)].write(f"Image not found: {image_path}")

elif option == "Enter Text":
    text_query = st.text_area("Enter a text description")
    if text_query:
        response = requests.post(f"{API_URL}/search/text/", params={"query": text_query})
        
        if response.status_code == 200:
            results = response.json().get("results", [])
            st.write("### Images matching your description:")
            cols = st.columns(min(5, len(results)))
            
            for i, result in enumerate(results):
                similarity = result["similarity"] * 100
                image_path = image_paths[result["image_path"]]
                index = result["index"]
                
                if os.path.exists(image_path):
                    retrieved_img = Image.open(image_path)
                    cols[i % len(cols)].image(retrieved_img, caption=f"Index: {index} | Similarity: {similarity:.1f}%", width=128)
                else:
                    cols[i % len(cols)].write(f"Image not found: {image_path}")
