import streamlit as st
import base64
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import google.generativeai as genai

# --------- Configure Gemini API ---------
genai.configure(api_key="AIzaSyDGPcIpxKsPFk1Nil-47XkLn6VGQB_rvrI")  # <<-- Your Gemini key

# --------- IMAGE UTILS ---------
def img_to_base64_str(path):
    with open(path, "rb") as img_file:
        b64_bytes = base64.b64encode(img_file.read())
        return f"data:image/jpeg;base64,{b64_bytes.decode()}"

doctor_img_base64 = img_to_base64_str("doctor.jpeg")
brain_img_base64  = img_to_base64_str("brain.jpeg")


# --------- PAGE STYLE (paste your CSS here) ---------
page_style = f"""
<style>
/* Your custom CSS from before goes here! */
.corner-image {{
  position: fixed; bottom: 20px; right: 20px; width: 120px; border-radius: 14px; opacity: 0.88; z-index: 9999;
}}
.corner-image-top-left {{
  position: fixed; top: 20px; left: 20px; width: 110px; border-radius: 13px; opacity: 0.88; z-index: 9999;
}}
.app-name-bg {{
  position: fixed; top: 42vh; left: 50%; transform: translateX(-50%);
  font-size: 8vw; font-weight: 900; color: #0078AA22; user-select: none; white-space: nowrap; z-index: 0; pointer-events: none;
  font-family: "Poppins", Arial, sans-serif; letter-spacing: 10px;
}}
/* ... rest of your CSS ... */
</style>
<img src="{doctor_img_base64}" class="corner-image">
<img src="{brain_img_base64}" class="corner-image-top-left">
<div class="app-name-bg">CareSync</div>
"""
st.markdown(page_style, unsafe_allow_html=True)

# --------- TOP NAV ---------
st.markdown("""
    <div style="width:100%;display:flex;align-items:center;gap:18px;margin-top:12px;">
      <span style="font-family:'Poppins',sans-serif;font-weight:600;font-size:2.1em;color:#0078AA;">CareSync</span>
      <img src="https://img.icons8.com/ios/50/0078AA/hearts.png" width="32" style="margin-bottom:6px;" />
    </div>
    <div style='font-size:18px;font-family:Poppins,Arial,sans-serif;font-weight:500;color:#22577a;'>Welcome to your AI-powered health dashboard!</div>
    <div class='devaq'>[translate:स्वस्थ शरीर में ही स्वस्थ मन वास करता है।]</div>
""", unsafe_allow_html=True)

# --------- LAYOUT ---------
col1, col2 = st.columns([4,5])
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Brain Tumor MRI Classification")
    st.write("Upload MRI Image…")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, width=300)
        if st.button('Start Diagnosis'):
            with st.spinner("Predicting..."):
                model = load_model(r"C:\Users\abhin\brain tumour\brain_tumor_model(1).h5")
                img = image.resize((224, 224))
                img = np.array(img) / 255.0
                img = np.expand_dims(img, axis=0)
                pred = model.predict(img)
                pred_idx = int(np.round(pred[0][0]))
                labels = ['Healthy', 'Tumor']
                st.success(f"Prediction: {labels[pred_idx]} (prob={pred[0][0]:.3f})")
    else:
        st.info("Limit 200MB per file • JPG, PNG, JPEG")
    st.markdown("**Consult confidentially and securely with Us.**")
    st.markdown('<span style="display:inline-block;background:#00f5cc;padding:6px 18px;border-radius:24px;font-weight:700;color:#004d40;margin-top:9px;font-family:Poppins;">Gemini Flash 2.5</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    tab = st.radio("", ["Diagnosis", "ChatBot", "Image Captioning", "Ask Anything"], label_visibility='collapsed')

    if tab == "Diagnosis":
        st.write("Upload MRI image and start diagnosis on the left.")

    elif tab == "ChatBot":
        prompt = st.text_input("Ask anything about your MRI results...")
        if prompt:
            with st.spinner(" please wait ..."):
                try:
                    model = genai.GenerativeModel("models/gemini-2.5-flash")
                    rsp = model.generate_content(prompt)
                    st.markdown(rsp.text)
                except Exception as e:
                    st.warning(f"Error: {e}")

    elif tab == "Image Captioning":
        img_up = st.file_uploader("Upload image for captioning", type=["jpg", "jpeg", "png"], key="cap")
        if img_up:
            st.image(Image.open(img_up))
            with st.spinner("Gemini is generating a caption..."):
                try:
                    caption_prompt = "Describe this medical image (e.g., MRI brain scan) in clinical detail."
                    model = genai.GenerativeModel("models/gemini-2.5-flash")
                    result = model.generate_content(caption_prompt)
                    st.success(result.text)
                except Exception as e:
                    st.warning(f"Error: {e}")

    elif tab == "Ask Anything":
        question = st.text_input("Your question")
        if question:
            with st.spinner("Gemini is replying..."):
                try:
                    model = genai.GenerativeModel("models/gemini-2.5-flash")
                    rsp = model.generate_content(question)
                    st.markdown(rsp.text)
                except Exception as e:
                    st.warning(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# --------- ARTICLE GRID ---------
st.markdown("""
<div class="article-grid">
  <div class="article-card">
    <span class="article-icon">🧠</span>
    <a class="article-title" href="https://www.mayoclinic.org/diseases-conditions/brain-tumor/symptoms-causes/syc-20350084" target="_blank">Brain Tumor Signs</a>
    <div class="article-desc">Learn key symptoms and indicators of brain tumors.</div>
  </div>
  <div class="article-card">
    <span class="article-icon">⚠️</span>
    <a class="article-title" href="https://www.webmd.com/brain/brain-tumors-causes-types-symptoms-treatments" target="_blank">Tumor Symptoms & Treatment</a>
    <div class="article-desc">Overview of tumor types and available treatment options.</div>
  </div>
  <div class="article-card">
    <span class="article-icon">💙</span>
    <a class="article-title" href="https://www.healthline.com/health/brain-tumor" target="_blank">Healthline: Brain Health</a>
    <div class="article-desc">Insights into maintaining and improving brain health.</div>
  </div>
  <div class="article-card">
    <span class="article-icon">🔬</span>
    <a class="article-title" href="https://www.medicalnewstoday.com/categories/neuroscience" target="_blank">Neuroscience News</a>
    <div class="article-desc">Latest scientific research in brain and neuroscience.</div>
  </div>
  <div class="article-card">
    <span class="article-icon">📊</span>
    <a class="article-title" href="https://www.cdc.gov/cancer/brain/statistics/" target="_blank">CDC Brain Cancer Stats</a>
    <div class="article-desc">Current statistics and trends in brain cancer incidence.</div>
  </div>
</div>
""", unsafe_allow_html=True)

# --------- FOOTER ---------
st.markdown("""
<div style="width:100%;background:linear-gradient(90deg,#0078AA,#00BFA6);padding:12px 0 8px 0;border-radius:0 0 12px 12px;color:white;text-align:center;margin-top:26px;">
  <b>Contact 📞</b> — Hospital: 1800-100-1000 | Ambulance: 102, 108 | Neuro: +91-9876543210<br>
  <small>24x7 emergency support | &copy; 2025 CareSync | <a href="https://www.who.int/health-topics" target="_blank" style="color:#a2e6d3;text-decoration:underline;">WHO Health Topics</a></small>
</div>
""", unsafe_allow_html=True)


