# 🔍 AI Reverse Image Search

This **Streamlit-powered web app** uses **Google Gemini AI** and **CLIP model** to generate captions and find visually similar images from the web via the **Unsplash API**.

---

## 🚀 Features
- 🖼️ Upload an image (JPG, PNG)
- 📝 Generate a short caption using **Gemini Flash**
- 🔍 Search Unsplash for related images using the caption
- 🎯 Use **CLIP-based embeddings** to compare visual similarity
- 📊 Display and rank top similar images by cosine similarity

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-reverse-image-search.git
cd ai-reverse-image-search
```

### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set API Keys
Create a `.streamlit/secrets.toml` file with:
```toml
GEMINI_API_KEY = "your_gemini_api_key"
UNSPLASH_API_KEY = "your_unsplash_api_key"
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

---

## 📂 File Structure
```
📦 ai-reverse-image-search
│
├── app.py                      # Main Streamlit app
├── requirements.txt           # Python dependencies
├── .streamlit/secrets.toml    # API keys (not committed)
├── backend/
│   ├── caption_generator.py   # Gemini-powered caption generation
│   ├── feature_extractor.py   # CLIP-based image embeddings
│   ├── image_search.py        # Unsplash image search and download
│   └── similarity.py          # Cosine similarity computation
└── temp/
    └── downloaded/            # Temporary images
```

---

## 🧠 How It Works
1. **Upload** an image from the sidebar.
2. **Gemini** generates a caption describing the image.
3. The caption is used to **search Unsplash** for similar content.
4. Images are downloaded and **encoded using CLIP**.
5. Each image is compared with the input using **cosine similarity**.
6. Top 10 visually similar images are **displayed with scores**.

---

## 📌 Dependencies
- `streamlit`
- `transformers`
- `torch`
- `Pillow`
- `requests`
- `numpy`

Install with:
```bash
pip install -r requirements.txt
```

---

## 🎓 Use Cases
- Creative inspiration & mood boarding
- Art or photo style reference finding
- Reverse search when no text clue is available

---
## 🔗 Contact
For any questions or collaborations, feel free to reach out:
- **GitHub**: [Jd1430](https://github.com/Jd1430)
- **Email**: jayanthdevarajgowda@gmail.com

---
💡 **Contributions are welcome!** Feel free to fork this repository and submit pull requests. 🚀
