import requests

def test_prediction():
    payload = {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.09,
        "RAD": 1,
        "TAX": 296,
        "PTRATIO": 15.3,
        "B": 396.9,
        "LSTAT": 4.98
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    assert response.status_code == 200
