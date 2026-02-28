**Project Overview**

This project is a Machine Learning–based Customer Churn Prediction System that predicts whether a telecom customer is likely to leave (Churn) or stay (Not Churn) based on customer service usage and billing information.
The model is deployed as an interactive web application where users can input customer details and instantly receive churn predictions along with probability scores.

**Live Deployment**
The application is successfully deployed on Render:
Live App: https://customer-churn-prediction-ml-wf6h.onrender.com

**Objective** 
Customer churn is one of the biggest challenges for subscription-based companies.
The goal of this project is to:
Identify customers at risk of leaving
Help businesses take preventive actions
Apply end-to-end Machine Learning deployment

**Machine Learning Approach**
**Data Preprocessing**
Handling categorical & numerical features
Feature engineering pipeline
Encoding categorical variables
Data transformation using Scikit-learn Pipeline

**Model Architecture**
An Ensemble Learning Model was used:
Logistic Regression
LightGBM
Stacking Classifier Ensemble
The final prediction is based on optimized probability threshold selection.

 **Features Used**
The model predicts churn using customer attributes such as:
Gender
Senior Citizen Status
Partner & Dependents
Tenure
Internet Service
Online Security / Backup
Contract Type
Payment Method
Monthly Charges
Total Charges
Streaming Services and more

**Web Application**
The system provides:
✅ User-friendly form interface
✅ Real-time churn prediction
✅ Probability-based output
✅ Flask backend integration

Example Output:
Prediction: Churn (Probability = 0.86)

**Tech Stack**
Machine Learning
Python
Scikit-learn
LightGBM
NumPy
Pandas
Joblib
Backend
Flask
Frontend
HTML
Tailwind CSS
Deployment
GitHub
Render (Cloud Deployment)

**Key Learning Outcomes**
End-to-end ML pipeline development
Feature engineering integration
Ensemble model training
Model serialization using Joblib
Flask ML deployment
Cloud deployment using Render
