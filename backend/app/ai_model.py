import random

import pandas as pd
from sklearn.linear_model import LinearRegression


def build_synthetic_dataset() -> pd.DataFrame:
    rows = []
    for hour in range(24):
        for vehicle_count in [30, 60, 90, 120, 150, 180]:
            for rain_mm in [0, 2, 5, 8]:
                temperature_c = 24 + (hour % 6) * 2 + (rain_mm * 0.4)
                congestion = (
                    vehicle_count * 0.25
                    + temperature_c * 0.8
                    + rain_mm * 2.5
                    + max(0, hour - 12) * 1.8
                    + random.randint(0, 10)
                )
                rows.append({
                    "vehicle_count": vehicle_count,
                    "temperature_c": temperature_c,
                    "rain_mm": rain_mm,
                    "hour": hour,
                    "congestion": min(100, congestion),
                })
    return pd.DataFrame(rows)


def train_model():
    df = build_synthetic_dataset()
    model = LinearRegression()
    X = df[["vehicle_count", "temperature_c", "rain_mm", "hour"]]
    y = df["congestion"]
    model.fit(X, y)
    return model


def predict_congestion(model, vehicle_count: int, temperature_c: float, rain_mm: float, hour: int) -> float:
    frame = pd.DataFrame(
        [{"vehicle_count": vehicle_count, "temperature_c": temperature_c, "rain_mm": rain_mm, "hour": hour}]
    )
    score = model.predict(frame)[0]
    return max(0, min(100, float(score)))
