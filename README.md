# CareSync – AI Brain Tumor MRI App (Streamlit + Gemini)

An AI-powered health dashboard for easy Brain Tumor MRI prediction, interactive Gemini chatbot, and smart image captioning, all in a beautiful Streamlit UI.
  
---

## Features

- **Brain Tumor MRI Diagnosis:** Upload MRI images, get instant predictions using a TensorFlow/Keras model (`.h5`).
- **Gemini Flash 2.5 ChatBot:** Ask health, pharmacy, or MRI questions with answers powered by Google Gemini.
- **AI Ask Anything:** Natural-language Q&A using Gemini.
- **Medical Image Captioning (Demo):** Automatic report/caption generated from MRI images (Gemini Flash 2.5).
- **Responsive Glassmorphism UI:** Modern cards, fixed images, dashboards, contact info, and more.

---

## Quick Start

**1. Clone or fork this repo, or deploy directly using Streamlit Cloud ([share.streamlit.io](https://share.streamlit.io/)).**

**2. Install requirements:**

pip install -r requirements.txt


**3. Set your Gemini API Key (do NOT hardcode in code):**
- In terminal (Linux/Mac):
export GEMINI_API_KEY=your-google-gemini-key
- In Windows CMD:
set GEMINI_API_KEY=your-google-gemini-key

**4. Run:**
streamlit run app.py


**5. For cloud deployment:**
- Push all files (including model & images) to your own GitHub repo
- In Streamlit Cloud, set GEMINI_API_KEY as a secret environment variable in the advanced settings  
- Deploy

---

## File Structure

app.py # Main Streamlit app
requirements.txt # All required Python libraries
brain_tumor_model(1).h5 # Pre-trained Keras/TensorFlow model (<100MB)
doctor.jpeg, brain.jpeg # UI/branding images
HD-wallpaper-medical-hospital.jpg # UI header imag


---

## Credits
- ML/AI: TensorFlow/Keras, Google Gemini API
- UI: Streamlit, CSS-Glassmorphism
- Icons: Icons8, Emojis

---

**© 2025 Abhinov | AI Health | GATE-2026 Project**
