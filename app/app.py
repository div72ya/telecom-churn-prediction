import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="Telecom Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
📊 Telecom Customer Churn Prediction
</h1>

<p style='text-align: center; font-size:18px;'>
Predict whether a telecom customer is likely to churn based on service behaviour
</p>
""", unsafe_allow_html=True)

st.markdown("---")
st.sidebar.title("Project Information")
st.sidebar.info(
"""
This app predicts **Telecom Customer Churn** using a Machine Learning model.

**Model Used**
- Random Forest Classifier

**Features Used**
- Tenure
- Complaints
- Payment Delay
- Service Rating

Built using:
- Python
- Scikit-learn
- Streamlit
"""
)

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "churn_model.pkl")

model_data = pickle.load(open(model_path, "rb"))
model = model_data["model"]
model_features = model_data["features"]

st.subheader("Enter Customer Details")
col1, col2 = st.columns(2)
with col1:
    tenure = st.slider("Tenure (Months)", 1, 72)
    complaints = st.slider("Number of Complaints (last 3 months)", 0, 10)
with col2:
    payment_delay = st.slider("Average Payment Delay (Days)", 0, 60)
    service_rating = st.slider("Service Rating (Last 6 months)", 1, 10)

data = pd.DataFrame({
    "tenure_months": [tenure],
    "num_complaints_3m": [complaints],
    "avg_payment_delay_days": [payment_delay],
    "service_rating_last_6m": [service_rating]
})
for col in model_features:
    if col not in data.columns:
        data[col] = 0

data = data[model_features]

if st.button("🔍 Predict Churn"):
    prediction = model.predict(data)
    st.markdown("---")
    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")

st.markdown("---")
st.markdown(
"""
<center>
Developed by **Divya Sharma**  

Capstone Project – Data Science with GenAI
</center>
""",
unsafe_allow_html=True
)