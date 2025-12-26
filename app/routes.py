from fastapi import APIRouter
from app.schemas import HouseInput
from src.predict import predict_price

router  = APIRouter()

@router.post("/predict")
def predict_house_price(data: HouseInput):
    price = predict_price(data.dict())
    return{
        "status": "success",
        "predicted_price" : price
    }