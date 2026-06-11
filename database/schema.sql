CREATE TABLE IF NOT EXISTS traffic_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vehicle_count INTEGER NOT NULL,
  temperature_c REAL NOT NULL,
  rain_mm REAL NOT NULL,
  hour INTEGER NOT NULL,
  congestion_score REAL NOT NULL,
  label TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
