from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title= "Boston House Price Prediction API",
    version = "1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API is running sucessfully"}