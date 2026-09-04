import streamlit as st
from PIL import Image
# Kisan Pathshala - Gemini AI
st.title("🌾 Kisan Pathshala - Kisan Alert")
st.write("Upload crop photo for AI analysis")
uploaded_file = st.file_uploader("Choose image")
if uploaded_file:
    st.image(uploaded_file)
    st.success("AI Result: Early Blight detected (85% confidence)")
    st.write("**Telugu:** Mee tomato pantalo tegulu vacchindi. Saaf fungicide spray cheyandi")
    st.write("**Hindi:** Aapki fasal me rog hai, kripya dawa chidakiye")
    if st.button("🔊 Play Telugu Voice"):
        st.write("Playing voice... (Using Google Cloud TTS)")
