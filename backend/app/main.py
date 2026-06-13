from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

from app.ai_model import predict_congestion, train_model
from app.storage import upload_prediction_log

app = FastAPI(title="Smart Mobility AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = train_model()


class PredictRequest(BaseModel):
    vehicle_count: int
    temperature_c: float
    rain_mm: float
    hour: int


@app.get("/health")
def health():
    return {"status": "ok", "service": "smart-mobility-ai"}


@app.post("/predict")
def predict(payload: PredictRequest):
    score = predict_congestion(
        model,
        payload.vehicle_count,
        payload.temperature_c,
        payload.rain_mm,
        payload.hour,
    )
    if score < 35:
        label = "Low"
    elif score < 60:
        label = "Moderate"
    elif score < 80:
        label = "High"
    else:
        label = "Critical"

    return {
        "congestion_score": round(score, 2),
        "label": label,
        "message": "AI congestion insight generated from the cloud-native backend.",
    }


@app.post("/upload-log")
def upload_log(payload: PredictRequest):
    score = predict_congestion(
        model,
        payload.vehicle_count,
        payload.temperature_c,
        payload.rain_mm,
        payload.hour,
    )
    if score < 35: label = "Low"
    elif score < 60: label = "Moderate"
    elif score < 80: label = "High"
    else: label = "Critical"

    log_data = {
        "vehicle_count": payload.vehicle_count,
        "temperature_c": payload.temperature_c,
        "rain_mm": payload.rain_mm,
        "hour": payload.hour,
        "congestion_score": round(score, 2),
        "label": label,
        "timestamp": datetime.utcnow().isoformat(),
    }
    success = upload_prediction_log(log_data)
    return {
        "congestion_score": round(score, 2),
        "label": label,
        "uploaded_to_r2": success,
        "message": "Prediction logged to Cloudflare R2 (multi-cloud storage).",
    }
