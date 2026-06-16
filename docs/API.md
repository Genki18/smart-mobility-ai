# API Documentation — Smart Mobility AI

## Base URL
http://54.252.230.104:8000

## Endpoints

### GET /health
Mengecek status backend.

Response:
{
  "status": "ok",
  "service": "smart-mobility-ai"
}

---

### POST /predict
Memprediksi tingkat kemacetan lalu lintas menggunakan AI.

Request Body:
{
  "vehicle_count": 120,
  "temperature_c": 30.0,
  "rain_mm": 5.0,
  "hour": 8
}

| Field | Tipe | Deskripsi |
|-------|------|-----------|
| vehicle_count | integer | Jumlah kendaraan di jalan |
| temperature_c | float | Suhu udara dalam Celsius |
| rain_mm | float | Curah hujan dalam mm |
| hour | integer | Jam format 24 jam (0-23) |

Response:
{
  "congestion_score": 80.54,
  "label": "Critical",
  "message": "AI congestion insight generated from cloud-native backend."
}

| Label | Skor |
|-------|------|
| Low | 0 - 34 |
| Moderate | 35 - 59 |
| High | 60 - 79 |
| Critical | 80 - 100 |

---

### POST /upload-log
Prediksi kemacetan dan simpan log ke Cloudflare R2 multi-cloud storage.

Request Body: sama dengan /predict

Response:
{
  "congestion_score": 80.54,
  "label": "Critical",
  "uploaded_to_r2": true,
  "message": "Prediction logged to Cloudflare R2 (multi-cloud storage)."
}

---

## Contoh CURL

Health check:
curl http://54.252.230.104:8000/health

Prediksi kemacetan:
curl -X POST http://54.252.230.104:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"vehicle_count": 120, "temperature_c": 30.0, "rain_mm": 5.0, "hour": 8}'

Upload log ke R2:
curl -X POST http://54.252.230.104:8000/upload-log \
  -H "Content-Type: application/json" \
  -d '{"vehicle_count": 120, "temperature_c": 30.0, "rain_mm": 5.0, "hour": 8}'

## Interactive Docs Swagger
http://54.252.230.104:8000/docs
