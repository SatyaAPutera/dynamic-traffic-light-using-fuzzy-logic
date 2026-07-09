# Dynamic Traffic Light Using Fuzzy Logic

Project ini merupakan simulasi sistem kendali lampu lalu lintas adaptif menggunakan logika fuzzy Mamdani. Aplikasi menghitung durasi lampu merah berdasarkan volume kendaraan, lebar jalan, dan panjang antrean.

## Fitur

- Menghitung volume kendaraan dalam satuan SMP
- Menggunakan aturan fuzzy untuk menentukan durasi lampu merah
- Menyediakan antarmuka interaktif dengan Streamlit
- Dapat diuji menggunakan data CSV sampel

## Struktur Proyek

- `src/app.py` : antarmuka aplikasi Streamlit
- `src/fuzzy_model.py` : implementasi logika fuzzy dan aturan inferensi
- `src/main.py` : skrip pengujian menggunakan data CSV
- `data/test.csv` : contoh data uji

## Persyaratan

- Python 3.9+
- `streamlit`
- `numpy`

## Cara Menjalankan

1. Masuk ke folder project
2. Buat dan aktifkan virtual environment
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependency
   ```powershell
   pip install streamlit numpy
   ```
4. Jalankan aplikasi Streamlit
   ```powershell
   streamlit run src/app.py
   ```

## Pengujian dengan Data CSV

Untuk menjalankan pengujian terhadap file CSV:

```powershell
python src/main.py
```

## Input dan Output

### Input
- Jumlah mobil
- Jumlah motor
- Jumlah bus
- Jumlah truk
- Lebar jalan (meter)
- Panjang antrean (meter)

### Output
- Durasi lampu merah dalam satuan detik

## Catatan

Aplikasi ini ditujukan untuk keperluan simulasi pembelajaran logika fuzzy dan belum sepenuhnya mewakili sistem kontrol real-time di lapangan.
