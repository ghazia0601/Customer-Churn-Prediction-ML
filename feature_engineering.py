import pandas as pd

def add_features(X):
    X = X.copy()

    X['tenure_segment'] = pd.cut(
        X['tenure'],
        bins=[0, 12, 48, 100],
        labels=['Short-term', 'Mid-term', 'Long-term']
    )

    service_cols = [
        'PhoneService','InternetService','OnlineSecurity','OnlineBackup',
        'DeviceProtection','TechSupport','StreamingTV','StreamingMovies'
    ]

    X['Number_of_Services'] = X[service_cols].apply(
        lambda row: sum(1 for v in row if v == 'Yes'),
        axis=1
    )

    return X
