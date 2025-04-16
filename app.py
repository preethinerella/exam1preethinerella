import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("imports-85.data")  # replace with your actual CSV file name

# App title
st.title("Exploratory Data Analysis - Preethi Nerella")

# Show the data
data = load_data()
st.write("### Dataset Preview")
st.write(data.head())

