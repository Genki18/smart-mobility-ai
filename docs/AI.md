# AI Documentation — Smart Mobility AI

## Model Overview
| Komponen | Detail |
|----------|--------|
| Library | Scikit-Learn 1.5.2 |
| Algoritma | Linear Regression |
| Training Data | Synthetic dataset (576 sampel) |
| Framework | Python 3.11 |

## Fitur Input
| Fitur | Tipe | Rentang | Deskripsi |
|-------|------|---------|-----------|
| vehicle_count | integer | 30 - 180 | Jumlah kendaraan di jalan |
| temperature_c | float | 24 - 36 C | Suhu udara |
| rain_mm | float | 0 - 8 mm | Curah hujan |
| hour | integer | 0 - 23 | Jam dalam sehari |

## Output
| Field | Tipe | Deskripsi |
|-------|------|-----------|
| congestion_score | float | Skor kemacetan 0-100 |
| label | string | Kategori kemacetan |

## Cara Kerja Model
1. Data Sintesis — Model dilatih menggunakan dataset sintetis 576 sampel kombinasi 24 jam, 6 level kendaraan, dan 4 level hujan.
2. Formula: congestion = (vehicle_count x 0.25) + (temperature_c x 0.8) + (rain_mm x 2.5) + (max(0, hour-12) x 1.8)
3. Training — Linear Regression dilatih dengan 4 fitur input untuk memprediksi skor 0-100.
4. Prediksi — Input pengguna diproses model, skor dikategorikan menjadi label.

## Kategori Label
| Label | Skor | Deskripsi |
|-------|------|-----------|
| Low | 0 - 34 | Lalu lintas lancar |
| Moderate | 35 - 59 | Sedikit padat |
| High | 60 - 79 | Cukup macet |
| Critical | 80 - 100 |
