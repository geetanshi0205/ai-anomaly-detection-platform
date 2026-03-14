import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("data/patient_data.csv")

model = IsolationForest(contamination=0.1)

model.fit(data)

joblib.dump(model,"model/anomaly_model.pkl")

print("Model trained")