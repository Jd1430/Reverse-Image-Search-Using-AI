# app.py
import streamlit as st
from PIL import Image
import os
import shutil

from backend.caption_generator import CaptionGenerator
from backend.feature_extractor import FeatureExtractor
from backend.image_search import search_and_download_images
from backend.similarity import cosine_similarity

# ----------------------------- CONFIG -----------------------------
st.set_page_config(page_title="AI Reverse Image Search", layout="wide")
st.title("🔍 AI Reverse Image Search")
st.sidebar.markdown("Upload an image to find **visually similar** ones from the internet.")

# ------------------------- API KEY SETUP --------------------------
UNSPLASH_API_KEY = st.secrets.get("UNSPLASH_API_KEY", os.getenv("UNSPLASH_API_KEY"))
os.environ["UNSPLASH_API_KEY"] = UNSPLASH_API_KEY

# ------------------------- APP LOGIC ------------------------------
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    # Create a grid with 3 columns
    cols = st.columns(3)

    # Show the image in the center column
    with cols[1]:  # Middle column
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Generating image caption..."):
        caption_generator = CaptionGenerator()
        caption = caption_generator.generate_caption(image)
    st.success(f"📝 Caption: `{caption}`")

    with st.spinner("Searching Unsplash for related images..."):
        result_paths = search_and_download_images(query=caption, num_images=15)

    with st.spinner("Comparing visual similarity..."):
        extractor = FeatureExtractor()
        input_vector = extractor.extract_features(image)

        results = []
        for path in result_paths:
            candidate = Image.open(path).convert("RGB")
            candidate_vector = extractor.extract_features(candidate)
            score = cosine_similarity(input_vector, candidate_vector)
            results.append((path, score))

        # Sort by similarity score (descending)
        results.sort(key=lambda x: x[1], reverse=True)

    # ------------------- SHOW RESULTS ------------------------
    st.subheader("🖼️ Top Visually Similar Images")
    cols = st.columns(5)

    for i, (path, score) in enumerate(results[:10]):
        with cols[i % 5]:
            st.image(path, caption=f"{score:.2f}", use_container_width=True)

    # Clean up temp files
    shutil.rmtree("temp/downloaded", ignore_errors=True)
