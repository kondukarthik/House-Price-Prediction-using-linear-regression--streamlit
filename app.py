
import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
pipeline = joblib.load("house_price_model_simple.pkl")

st.title("🏡 House Price Prediction App")

# Sidebar for user input
st.sidebar.header("Enter House Features")

def user_input():
    street = st.sidebar.selectbox("Street Type", ["Pave", "Grvl"])
    year_built = st.sidebar.number_input("Year Built", 1800, 2025, 2000)
    yr_sold = st.sidebar.number_input("Year Sold", 1900, 2025, 2010)

    data = {
        "Street": street,
        "YearBuilt": year_built,
        "YrSold": yr_sold
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Collect user input
input_data = user_input()

st.subheader("User Input Features")
st.write(input_data)

# Predict button
if st.button("Predict House Price"):
    prediction = pipeline.predict(input_data)
    st.subheader("Predicted Sale Price")
    st.success(f"${prediction[0]:,.2f}")


