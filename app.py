app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Crop Recommendation", layout="centered")

st.title("🌾 Smart Crop Recommendation")

temperature = st.slider("Temperature (°C)", 10, 45, 30)
rainfall = st.slider("Rainfall (mm)", 200, 3000, 1500)
season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid"])

if st.button("Recommend"):
    st.success("Top 3 Recommended Crops")
    st.write("1. 🌱 Rice — Score: 0.8")
    st.write("2. 🌱 Sugarcane — Score: 0.8")
    st.write("3. 🌱 Maize — Score: 0.4")
