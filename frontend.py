import streamlit as st
import requests
import json

# FastAPI endpoint URL
API_URL = "https://customer-churn-predict.onrender.com/predict"

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict if they will churn or stay.")

# Form layout
with st.form("churn_form"):
    st.subheader("Customer Information")
    gender = st.radio("Gender:", ["Male", "Female"], index=0)
    SeniorCitizen = st.radio("Senior Citizen:", ["Yes", "No"], index=1)
    Partner = st.radio("Partner:", ["Yes", "No"], index=1)
    Dependents = st.radio("Dependents:", ["Yes", "No"], index=1)
    
    st.subheader("Service Details")
    tenure = st.number_input("Tenure (months):", min_value=0, step=1)
    PhoneService = st.radio("Phone Service:", ["Yes", "No"], index=0)
    MultipleLines = st.radio("Multiple Lines:", ["Yes", "No"], index=1)
    InternetService = st.radio("Internet Service:", ["DSL", "Fiber Optic", "No"], index=2)
    OnlineSecurity = st.radio("Online Security:", ["Yes", "No"], index=1)
    OnlineBackup = st.radio("Online Backup:", ["Yes", "No"], index=1)
    DeviceProtection = st.radio("Device Protection:", ["Yes", "No"], index=1)
    TechSupport = st.radio("Tech Support:", ["Yes", "No"], index=1)
    StreamingTV = st.radio("Streaming TV:", ["Yes", "No"], index=1)
    StreamingMovies = st.radio("Streaming Movies:", ["Yes", "No"], index=1)
    
    st.subheader("Billing Details")
    Contract = st.radio("Contract:", ["Month-to-month", "One year", "Two year"], index=0)
    PaperlessBilling = st.radio("Paperless Billing:", ["Yes", "No"], index=0)
    PaymentMethod = st.radio("Payment Method:", ["Electronic Check", "Mailed Check", "Bank Transfer", "Credit Card"], index=0)
    MonthlyCharges = st.number_input("Monthly Charges:", min_value=0.0, step=0.1)
    TotalCharges = st.number_input("Total Charges:", min_value=0.0, step=0.1)
    
    submit_button = st.form_submit_button("Predict Churn")

if submit_button:
    # Convert categorical values to numeric
    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if SeniorCitizen == "Yes" else 0,
        "Partner": 1 if Partner == "Yes" else 0,
        "Dependents": 1 if Dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if PhoneService == "Yes" else 0,
        "MultipleLines": 1 if MultipleLines == "Yes" else 0,
        "InternetService": ["No", "DSL", "Fiber Optic"].index(InternetService),
        "OnlineSecurity": 1 if OnlineSecurity == "Yes" else 0,
        "OnlineBackup": 1 if OnlineBackup == "Yes" else 0,
        "DeviceProtection": 1 if DeviceProtection == "Yes" else 0,
        "TechSupport": 1 if TechSupport == "Yes" else 0,
        "StreamingTV": 1 if StreamingTV == "Yes" else 0,
        "StreamingMovies": 1 if StreamingMovies == "Yes" else 0,
        "Contract": ["Month-to-month", "One year", "Two year"].index(Contract),
        "PaperlessBilling": 1 if PaperlessBilling == "Yes" else 0,
        "PaymentMethod": ["Electronic Check", "Mailed Check", "Bank Transfer", "Credit Card"].index(PaymentMethod),
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }
    
    # Send request to FastAPI
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction", "Unknown")
        if prediction == "Churn":
            st.error("⚠️ Prediction: Customer is likely to churn.")
        else:
            st.success("✅ Prediction: Customer is likely to stay.")
    else:
        st.error("❌ Error: Unable to get prediction. Check API status.")
