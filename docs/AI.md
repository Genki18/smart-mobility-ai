# AI Documentation

This prototype uses a lightweight machine-learning congestion predictor implemented in the backend service.

The model uses:
- vehicle_count
- temperature_c
- rain_mm
- hour

It returns:
- congestion_score (0-100)
- label (Low / Moderate / High / Critical)

This is suitable for a cloud-native smart mobility prototype and can later be upgraded to a real model, OpenAI/Gemini API, or an Ollama-based service.
