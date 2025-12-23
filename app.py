import streamlit as st
import joblib
import pandas as pd

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Phone Price Prediction",
    page_icon="📱",
    layout="centered"
)

# -------------------------
# Title with image
# -------------------------
st.image(
    "https://cdn-icons-png.flaticon.com/512/747/747376.png",
    width=120
)
st.title("📱 Phone Price Prediction App  (by :- PRINCE RAJPUT)")
st.write("Enter phone details to predict price")

# -------------------------
# Load trained pipeline
# (get_dummies + scaler + model)
# -------------------------
model = joblib.load("Phone_price.pkl")

# -------------------------
# User Inputs
# -------------------------
brand = st.selectbox(
    "Brand",
    ["Apple", "Samsung", "OnePlus", "Xiaomi", "Google"]
)

storage = st.number_input("Storage (GB)", min_value=0, value=128)
ram = st.number_input("RAM (GB)", min_value=0, value=8)
battery = st.number_input("Battery (mAh)", min_value=0, value=4000)
back_camera = st.number_input("Back Camera (MP)", min_value=0, value=48)
front_camera = st.number_input("Front Camera (MP)", min_value=0, value=16)

# -------------------------
# Prediction
# -------------------------
if st.button("Predict Price 💰"):
    input_df = pd.DataFrame({
        "Brand": [brand],
        "Storage": [storage],
        "RAM": [ram],
        "Battery(mAh)": [battery],
        "back camera": [back_camera],
        "front camera": [front_camera]
    })

    prediction = model.predict(input_df)

    st.success(f"💰 Predicted Price: ₹ {int(prediction[0]):,}")
