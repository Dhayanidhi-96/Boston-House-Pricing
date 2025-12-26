import joblib
import numpy as np

MODEL_PATH = r"model/boston_model.pkl"
SCALER_PATH = r"models/scaler.pkl"

FEATURE_ORDER = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX",
    "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_price(input_data : dict) -> float:
    """
    input_data: dict of 13 feature values
    """
    data_array = np.array([[input_data[col] for col in FEATURE_ORDER]])
    scaled_data = scaler.transform(data_array)
    scaled_data = model.predict(scaled_data)
    prediction = model.predict(scaled_data)
    return round(float(prediction[0]),2)