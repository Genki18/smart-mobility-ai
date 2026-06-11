# API Documentation

## Health
GET /health
Returns a simple status payload.

## Predict congestion
POST /predict
Body:
{
  "vehicle_count": 120,
  "temperature_c": 30,
  "rain_mm": 5,
  "hour": 17
}

Response:
{
  "congestion_score": 68.45,
  "label": "High",
  "message": "AI congestion insight generated from the cloud-native backend."
}
