import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open("energy_model.pkl", "rb") as file:
    model = pickle.load(file)

# Set Page Configuration
st.set_page_config(
    page_title="Energy Prediction ⚡",
    page_icon="🔋",
    layout="centered"
)

# Custom Background Color
st.markdown(
    """
    <style>
    body {
        background-color: grey; 
    }
    .stApp {
            background-color:#7a604a ; 
        color:white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
     /* Custom slider */
    div[data-baseweb="slider"] {
        background: #cad076 !important;  /* Light blue */
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Custom input box */
    input[type="number"] {
        background-color:  #cad076 !important; /* Light Blue */
        border-radius: 5px;
        padding: 8px;
        color: black;
        border: 1px solid;
    }
    
      button[title="Increment"] {
        background-color: #68aeac !important; /* Blue */
        color: white !important;
        border-radius: 50%;
        padding: 5px 10px;
    }

    button[title="Decrement"] {
        background-color: #68aeac !important; /* Red */
        color: white !important;
        border-radius: 50%;
        padding: 5px 10px;
    }

    /* Custom Button */
    .stButton>button {
        background-color: #3e3524 !important;
        color: white !important;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Title with Emoji
st.title("🏡 Household Energy Consumption Prediction ")

# Subtitle
st.markdown("### Estimate your home's energy usage based on conditions.")

# Use Columns for Better Layout
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("🌡 Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
    humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    
with col2:
    appliances = st.number_input("🔌 Number of Appliances", min_value=0, max_value=100, value=5)
    hour = st.slider("🕒 Hour of the Day", 0, 23, 12)
    day_of_week = st.slider("📅 Day of the Week (0=Monday, 6=Sunday)", 0, 6, 3)

# Add a Cool Button for Prediction
if st.button("🚀 Predict Energy Consumption"):
    input_data = np.array([[temperature, humidity, appliances, hour, day_of_week]])
    prediction = model.predict(input_data)
    
    st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.2f} kWh")


