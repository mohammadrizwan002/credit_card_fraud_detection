import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("../model/xgboost_model.pkl")

# Title
st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter transaction details below:")

# 30 features input (V1 to V28, Amount, Time)
feature_names = [f"V{i}" for i in range(1, 29)] + ["Amount", "Time"]
inputs = []

# Input fields
for name in feature_names:
    value = st.number_input(f"Enter {name}", value=0.0)
    inputs.append(value)

# Convert to array
input_array = np.array(inputs).reshape(1, -1)

# Predict button
if st.button("🔍 Predict Fraud"):
    prediction = model.predict(input_array)[0]
    if prediction == 1:
        st.error("⚠️ Transaction is Fraudulent!")
    else:
        st.success("✅ Transaction is Legitimate.")
