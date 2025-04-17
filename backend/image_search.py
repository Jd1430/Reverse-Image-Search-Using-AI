# backend/image_search.py

import os
import requests
from PIL import Image
from io import BytesIO

def search_and_download_images(query, download_folder="temp/downloaded", num_images=10):
    os.makedirs(download_folder, exist_ok=True)
    access_key = os.getenv("UNSPLASH_API_KEY")

    headers = {"Authorization": f"Client-ID {access_key}"}
    search_url = "https://api.unsplash.com/search/photos"
    params = {"query": query, "per_page": num_images, "orientation": "landscape"}

    response = requests.get(search_url, headers=headers, params=params)
    results = response.json()

    image_paths = []
    for i, img in enumerate(results.get("results", [])):
        try:
            img_data = requests.get(img["urls"]["regular"], timeout=3)
            image = Image.open(BytesIO(img_data.content)).convert("RGB")
            save_path = os.path.join(download_folder, f"{i}.jpg")
            image.save(save_path)
            image_paths.append(save_path)
        except Exception as e:
            print(f"[ERROR] Could not download image {i}: {e}")

    return image_paths
