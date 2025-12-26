import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def load_and_preprocess_data():
    """
    Load dataset, split features & target, scale features
    """
    df = pd.read_csv(r"D:\Boston_house_price\data\Boston-house-price-data.csv")

    TARGET_COLUMN = "MEDV"

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
        )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled,X_test_scaled,y_train,y_test,scaler