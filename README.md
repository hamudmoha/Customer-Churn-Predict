Customer Churn Prediction

Overview

This project predicts customer churn for a telecommunications company using machine learning. The model is deployed using FastAPI for backend processing and a frontend built with HTML, CSS, and JavaScript. A Streamlit-based UI is also available as an alternative.

Features

Predicts if a customer will Stay or Churn.

REST API powered by FastAPI.

Interactive frontend for user-friendly input.

Streamlit UI for quick visualization.

Dataset

The project uses the Telco Customer Churn Dataset from Kaggle, containing customer information such as:

Demographic Details: Gender, Senior Citizen, Partner, Dependents.

Service Details: Phone Service, Internet Service, Online Security, etc.

Account & Billing Info: Contract Type, Payment Method, Monthly Charges, Total Charges.

Target Variable: Churn (Yes/No).

Installation

Clone the Repository
 git clone https://github.com/your-username/customer-churn-prediction.git
 cd customer-churn-prediction
Install Dependencies
pip install -r requirements.txt

Run FastAPI Backend
uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000.

Run Frontend (HTML, CSS, JavaScript)

Open index.html in a web browser.

Run Streamlit UI (Optional)
streamlit run app.py


API Usage

The FastAPI backend exposes a prediction endpoint where users can send customer details and receive churn predictions.

Endpoint:

POST /predict

Example Input (JSON):
{
  "gender": "Female",
  "SeniorCitizen": 1,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 3,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 95.75,
  "TotalCharges": 287.25
}
{
  "prediction": "Churn"
}


{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "Yes",
  "tenure": 48,
  "PhoneService": "Yes",
  "MultipleLines": "Yes",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "Yes",
  "DeviceProtection": "Yes",
  "TechSupport": "Yes",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Two year",
  "PaperlessBilling": "No",
  "PaymentMethod": "Bank transfer (automatic)",
  "MonthlyCharges": 65.50,
  "TotalCharges": 3144.00
}

{
  "prediction": "Stay"
}


Future Improvements

Deploying on cloud platforms (AWS/GCP/Azure).

Adding real-time monitoring for predictions.

Enhancing model accuracy with advanced feature engineering.

License

This project is open-source under the MIT License.

Contributors

Developed by Your Name. Feel free to contribute by submitting pull requests!

below are the link where you can predict the customer churning:
**https://hamudmoha-customer-churn-predict-frontend-28lldx.streamlit.app/**

🚀 Happy Predicting! 🎯
