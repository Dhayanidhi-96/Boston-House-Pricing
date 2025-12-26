import joblib
import numpy as np

MODEL_PATH = "models/boston_model.pkl"
SCALER_PATH = "models/scaler.pkl"

FEATURE_ORDER = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX",
    "RM", "AGE", "DIS", "RAD", "TAX", 
    "PTRATIO", "B", "LSTAT"]

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_price(input_data: dict) -> float:
    missing = [f for f in FEATURE_ORDER if f not in input_data]
    if missing:
        raise ValueError(f"Missing input features: {missing}")

    data_array = np.array([[input_data[col] for col in FEATURE_ORDER]])
    scaled_data = scaler.transform(data_array)
    prediction = model.predict(scaled_data)
    return round(float(prediction[0]), 2)
