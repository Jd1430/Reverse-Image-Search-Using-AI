# backend/caption_generator.py

import os
import base64
import requests
from PIL import Image
import io
import streamlit as st

class CaptionGenerator:
    def __init__(self):
        self.api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
        self.model = "models/gemini-1.5-flash-latest"
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/{self.model}:generateContent"

    def generate_caption(self, image: Image.Image) -> str:
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()

        prompt = (
            "Describe the image in one short sentence (5 to 6 words). "
            "If it shows a well-known object, place, or landmark, include the name at the end. "
            "Example: 'White marble mausoleum at sunset, Taj Mahal'"
        )

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt},
                        {
                            "inlineData": {
                                "mimeType": "image/jpeg",
                                "data": img_b64
                            }
                        }
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(
            f"{self.endpoint}?key={self.api_key}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()
        else:
            st.error("❌ Gemini Flash API request failed.")
            st.error(response.text)
            return "Unknown subject"
