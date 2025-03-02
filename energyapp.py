import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open("energy_model.pkl", "rb") as file:
    model = pickle.load(file)

# UI Title
st.title("Household Energy Consumption Prediction")

# User Input Form
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
appliances = st.number_input("Number of Appliances", min_value=0, max_value=100, value=5)
hour = st.slider("Hour of the Day", 0, 23, 12)
day_of_week = st.slider("Day of the Week (0=Monday, 6=Sunday)", 0, 6, 3)

# Prediction
if st.button("Predict Energy Consumption"):
    input_data = np.array([[temperature, humidity, appliances, hour, day_of_week]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Energy Consumption: {prediction[0]:.2f} kWh")
