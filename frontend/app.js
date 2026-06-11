const form = document.getElementById('prediction-form');
const result = document.getElementById('result');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const payload = {
    vehicle_count: Number(document.getElementById('vehicle_count').value),
    temperature_c: Number(document.getElementById('temperature_c').value),
    rain_mm: Number(document.getElementById('rain_mm').value),
    hour: Number(document.getElementById('hour').value),
  };

  try {
    const response = await fetch('http://127.0.0.1:8080/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    result.innerHTML = `Prediksi: <strong>${data.label}</strong> dengan skor ${data.congestion_score}. ${data.message}`;
  } catch (error) {
    result.innerHTML = 'Tidak dapat terhubung ke backend API. Jalankan server dulu sebelum mencoba.';
  }
});