from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from feature_engineering import add_features
import joblib
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
import lightgbm as lgb
from sklearn.preprocessing import FunctionTransformer

app = Flask(__name__)

# Load model
model_data = joblib.load("final_churn_ensemble_model.pkl")
ensemble_model = model_data["model"]
optimal_threshold = model_data["threshold"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data as dict (KEEP STRINGS)
        form_data = request.form.to_dict()

        # Convert only numeric fields
        numeric_fields = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
        for field in numeric_fields:
            form_data[field] = float(form_data[field])

        # Create DataFrame with ONE row
        input_df = pd.DataFrame([form_data])

        # Predict probability
        prob = ensemble_model.predict_proba(input_df)[0][1]

        prediction = "Churn" if prob >= optimal_threshold else "Not Churn"

        return render_template(
            'index.html',
            prediction_text=f"{prediction} (probability = {prob:.2f})"
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
