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
   
