# 🏡 Boston House Price Prediction – End-to-End ML Web App

An end-to-end **Machine Learning web application** that predicts house prices in Boston using socioeconomic and environmental features.  
The project demonstrates the complete ML workflow: **EDA → Model Training → API → Frontend → Cloud Deployment**.

🔗 **Live Demo**  
https://boston-house-pricing-pdwk.onrender.com

---

## 📌 Project Overview

This project uses the **Boston Housing Dataset** to train a regression model that predicts the median house value (MEDV) based on 13 input features such as crime rate, number of rooms, tax rate, and more.

The trained model is served using **FastAPI**, provides a **web-based UI using Jinja2**, and is deployed on **Render (free tier)**.

---

## 🧠 Key Features

- 📊 Exploratory Data Analysis (EDA)
- 🔍 Feature scaling and preprocessing
- 🤖 Machine learning model training
- ⚙️ REST API for predictions
- 🖥️ Web-based frontend (served by FastAPI)
- ☁️ Live cloud deployment
- 📦 Clean, modular, production-style project structure

---

## 🛠️ Tech Stack

### Programming & ML
- Python 3.9
- NumPy
- Pandas
- Scikit-learn
- Joblib

### Backend & Frontend
- FastAPI
- Uvicorn
- Jinja2 Templates
- HTML & CSS

### Deployment & Tools
- Render (Free Tier)
- Git & GitHub

---

## 📂 Project Structure
```
Boston_house_price/
│
├── app/
│ ├── main.py # FastAPI entry point (UI + API)
│ ├── routes.py # Prediction routes
│ └── schemas.py # Input schema
│
├── src/
│ ├── data_preprocessing.py
│ ├── train.py
│ └── predict.py
│
├── templates/
│ └── index.html # Frontend UI
│
├── models/
│ ├── boston_model.pkl
│ └── scaler.pkl
│
├── data/
│ └── boston.csv
│
├── EDA/
│ └── exploratory_analysis.ipynb
│
├── requirements.txt
├── Procfile
└── README.md

```
---

## 📊 Exploratory Data Analysis (EDA)

The EDA includes:
- Target variable distribution analysis
- Correlation heatmaps
- Outlier detection using boxplots
- Feature importance intuition

### Key Insights
- `RM` (average number of rooms) has strong positive correlation with house price
- `LSTAT` (% lower status population) has strong negative correlation
- Several features show non-linear behavior, motivating more advanced models

---

## 🤖 Model Training

- **Model**: Linear Regression
- **Scaling**: StandardScaler
- **Train/Test Split**: 80/20
- **Evaluation Metric**: R² Score

**Initial R² Score**: ~0.67

---

## 🌐 Web Application

The application provides:
- A clean UI to input housing features
- Real-time house price prediction
- JSON-based prediction API

### Available Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/` | Web UI |
| POST | `/predict` | Prediction API |
| GET | `/docs` | Swagger API documentation |

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Dhayanidhi-96/Boston-House-Pricing.git
cd Boston_house_price
```
### 2️⃣ Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Train the model
```
python -m src.train
```
### 5️⃣ Run the application
```
uvicorn app.main:app --reload
```

### 6️⃣ Open in browser
```
http://127.0.0.1:8000
```

## ☁️ Deployment

- Deployed on **Render**
- Single **FastAPI** service serving both frontend and backend
- Free-tier compatible
- Automatic deployment via **GitHub**

---

## 🚀 Future Enhancements

- Improve accuracy using **Random Forest** or **XGBoost**
- Add better input validation and error handling
- Enhance UI using **Bootstrap**
- Add **Docker** support
- Implement **CI/CD pipeline**
- Add logging and monitoring

---

## 👤 Author

**Dhayanidhi**  
M.Sc Data Science Student  
Aspiring Data Scientist / AI Engineer  

🔗 GitHub: https://github.com/Dhayanidhi-96

---

## ⭐ Acknowledgements

- Boston Housing Dataset  
- FastAPI Documentation  
- Render Cloud Platform  
