📊 Telecom Customer Churn Prediction
🚀 Overview

This project builds a machine learning model to predict whether a telecom customer is likely to churn. It combines data analysis, model development, and an interactive Streamlit web application for real-time predictions.

🎯 Business Problem

Customer churn leads to significant revenue loss in telecom companies. Identifying high-risk customers early enables businesses to take proactive retention actions and reduce churn.

⚙️ Key Highlights
Applied SMOTE to handle class imbalance
Compared multiple models: Logistic Regression, Random Forest, Gradient Boosting
Achieved ~81% recall for churn prediction
Used SHAP for model explainability
Built a Streamlit web app for real-time predictions
🧠 Model Performance
Model	Accuracy
Logistic Regression	~61%
Gradient Boosting	~62%
Random Forest	Best Model

Key Metric:
➡️ Recall (Churn Class): ~0.81

🔍 Features Used
Tenure (Months)
Number of Complaints (Last 3 Months)
Average Payment Delay (Days)
Service Rating (Last 6 Months)
📊 Key Insights
Customers with low tenure are more likely to churn
High monthly charges increase churn probability
Frequent complaints strongly indicate churn
Payment delays signal dissatisfaction
💡 Business Recommendations
Focus on early-stage customers (first year)
Offer personalized retention offers
Improve complaint resolution systems
Monitor payment delays proactively
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
SHAP
Streamlit
Imbalanced-learn (SMOTE)
▶️ How to Run the Project
pip install -r requirements.txt
streamlit run app/app.py
📁 Project Structure
telecom-churn-prediction/
│
├── app/
├── data/
├── notebooks/
├── README.md
├── requirements.txt
📸 App Preview
<img width="1365" height="609" alt="image" src="https://github.com/user-attachments/assets/e319df98-8ed7-4309-8844-97dc512ee207" />

<img width="1366" height="627" alt="image" src="https://github.com/user-attachments/assets/11bd7ead-1e80-457c-85eb-eb1493081c53" />



👤 Author

Divya Sharma
