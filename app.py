import streamlit as st
import joblib
import numpy as np

# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="Cellphone Price Prediction app", page_icon="📱")

# -------------------------
# Title with image
# -------------------------
st.image(
    "https://cdn-icons-png.flaticon.com/512/747/747376.png",
    width=120
)

st.title("📱 Cellphone Prediction App")
st.write("Enter all feature values to get prediction")

# -------------------------
# Load trained model
# -------------------------
model = joblib.load("cellphone.pkl")

# -------------------------
# Input fields (EXACT order)
# -------------------------
sale = st.number_input("Sale", value=0.0)
weight = st.number_input("Weight", value=0.0)
resolution = st.number_input("Resolution", value=0.0)
ppi = st.number_input("PPI", value=0.0)
cpu_core = st.number_input("CPU Cores", value=0)
cpu_freq = st.number_input("CPU Frequency", value=0.0)
internal_mem = st.number_input("Internal Memory", value=0.0)
ram = st.number_input("RAM", value=0.0)
rear_cam = st.number_input("Rear Camera", value=0.0)
front_cam = st.number_input("Front Camera", value=0.0)
battery = st.number_input("Battery", value=0.0)
thickness = st.number_input("Thickness", value=0.0)

# -------------------------
# Prediction
# -------------------------
if st.button("Predict"):
    input_data = np.array([[ 
        sale, weight, resolution, ppi, cpu_core,
        cpu_freq, internal_mem, ram,
        rear_cam, front_cam, battery, thickness
    ]])

    prediction = model.predict(input_data)
    st.success(f"Prediction Result: {prediction[0]}")
