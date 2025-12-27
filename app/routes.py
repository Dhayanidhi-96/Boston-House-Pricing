from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.predict import predict_price

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/", response_class=HTMLResponse)
def predict_ui(
    request: Request,
    CRIM: float = Form(...),
    ZN: float = Form(...),
    INDUS: float = Form(...),
    CHAS: int = Form(...),
    NOX: float = Form(...),
    RM: float = Form(...),
    AGE: float = Form(...),
    DIS: float = Form(...),
    RAD: int = Form(...),
    TAX: float = Form(...),
    PTRATIO: float = Form(...),
    B: float = Form(...),
    LSTAT: float = Form(...)
):
    input_data = {
        "CRIM": CRIM,
        "ZN": ZN,
        "INDUS": INDUS,
        "CHAS": CHAS,
        "NOX": NOX,
        "RM": RM,
        "AGE": AGE,
        "DIS": DIS,
        "RAD": RAD,
        "TAX": TAX,
        "PTRATIO": PTRATIO,
        "B": B,
        "LSTAT": LSTAT,
    }

    prediction = predict_price(input_data)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": prediction
        }
    )


# API endpoint still available
@router.post("/predict")
def predict_api(data: dict):
    price = predict_price(data)
    return {"predicted_price": price}
