import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from src.data_preprocessing import load_and_preprocess_data

MODEL_PATH = r"models/boston_model.pkl"
SCALER_PATH = r"models/scaler.pkl"


def train_model():
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data()

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    print(f"Model trained successfully | R2 Score: {score:.4f}")


if __name__ == "__main__":
    train_model()
