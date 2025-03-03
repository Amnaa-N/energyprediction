import streamlit as st
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

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-color: black; 
    }
    .stApp {
        background-color:#503D42; 
        color:#EEF4ED;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .custom-label {
        color: white;  
        font-size: 14px;
        font-weight: bold;
    }
    /* Custom slider */
    div[data-baseweb="slider"] {
        background: #92AD94 !important;  
        border-radius: 10px;
        padding: 8px;
    }
    /* Custom input box */
    input[type="number"] {
        background-color: #92AD94 !important;
        color: black;
        border-radius: 5px;
        padding: 8px;
        border: 1px solid;
    }
    /* Custom + and - buttons */
    button[title="Increment"], button[title="Decrement"] {
        background-color: #68aeac !important;
        color: white !important;
        border-radius: 50%;
        padding: 5px 10px;
    }
    /* Custom Button */
    .stButton>button {
        background-color: #748B75 !important;
        color: black !important;
        border-radius: 8px;
        padding: 10px;
    }
    /* Custom Output Box */
    .custom-alert {
        background-color: #92AD94; 
        color: #171829;  
        padding: 15px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        border: 2px solid #64b5f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Title
st.title("🏡 Household Energy Consumption Prediction 🔋")

# Subtitle
st.markdown("### Estimate your home's energy usage based on conditions.")

# Layout using columns
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="custom-label">🌡 Temperature (°C)</p>', unsafe_allow_html=True)
    temperature = st.number_input("", min_value=0.0, max_value=50.0, value=25.0)

    st.markdown('<p class="custom-label">💧 Humidity (%)</p>', unsafe_allow_html=True)
    humidity = st.number_input("", min_value=0.0, max_value=100.0, value=50.0)

    st.markdown('<p class="custom-label">🕒 Hour of the Day</p>', unsafe_allow_html=True)
    hour = st.slider("", 0, 23, 12, key="hour_slider")

with col2:
    st.markdown('<p class="custom-label">🔌 Number of Appliances</p>', unsafe_allow_html=True)
    appliances = st.number_input("", min_value=0, max_value=100, value=5)

    st.markdown('<p class="custom-label">📅 Day of the Week (0=Monday, 6=Sunday)</p>', unsafe_allow_html=True)
    day_of_week = st.slider("", 0, 6, 3, key="day_slider")

# Centered Predict Button
st.markdown("<br>", unsafe_allow_html=True)
center_col = st.columns([2, 1, 2])[1]
with center_col:
    predict_btn = st.button("🚀 Predict Energy Consumption")

# Handle Prediction
if predict_btn:
    input_data = np.array([[temperature, humidity, appliances, hour, day_of_week]])
    prediction = model.predict(input_data)

    # Custom Alert Box for Output
    st.markdown(
        f"""
        <div class="custom-alert">
            ⚡ Predicted Energy Consumption: <strong>{prediction[0]:.2f} kWh</strong>
        </div>
        """,
        unsafe_allow_html=True
    )
