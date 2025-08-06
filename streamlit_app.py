import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("malnutrition_model.pkl")

# Streamlit UI
st.set_page_config(page_title="Child Malnutrition Predictor", page_icon="🧠")
st.title("Child Malnutrition Risk Predictor")
st.write("Enter the details below to predict if the child is at risk of malnutrition.")

# Input fields
age = st.number_input("Child's Age (months)", min_value=0, max_value=60, value=24)
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=90.0, value=10.0, step=0.1)
height = st.number_input("Height (cm)", min_value=30.0, max_value=190.0, value=80.0, step=0.1)
income = st.number_input("Monthly Household Income (₹)", min_value=1000, max_value=50000, value=10000, step=500)

# Predict button
if st.button("🔍 Predict"):
    input_df = pd.DataFrame([[age, weight, height, income]], columns=['Age', 'Weight', 'Height', 'Income'])
    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error("🔴 The child is likely **MALNOURISHED**.")
    else:
        st.success("🟢 The child is likely **HEALTHY**.")

