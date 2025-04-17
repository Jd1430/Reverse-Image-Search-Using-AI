# backend/feature_extractor.py

from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
import numpy as np

class FeatureExtractor:
    def __init__(self, model_name="CLIP", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = model_name

        if model_name == "CLIP":
            self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
            self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        else:
            raise NotImplementedError("Only CLIP is currently supported")

    def extract_features(self, image: Image.Image) -> np.ndarray:
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.get_image_features(**inputs)
        embedding = outputs.cpu().numpy().flatten()
        embedding /= np.linalg.norm(embedding)  # Normalize
        return embedding
