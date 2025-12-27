from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routes import router

app = FastAPI(
    title="Boston House Price Prediction",
    version="1.0"
)

# Load templates
templates = Jinja2Templates(directory="templates")

# API routes
app.include_router(router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": None}
    )
