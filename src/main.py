import csv
from fuzzy_model import Kendaraan, hitung_lampu_merah


def jalankan_pengujian(file_path):
    print(f"{'Mobil':<6} | {'Motor':<6} | {'Bus':<6} | {'Truk':<6} | {'Volume':<8} | {'Lebar':<6} | {'Panjang':<8} | {'Hasil (Detik)':<15}")

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            crisp_mobil = float(row.get('Mobil', 0))
            crisp_motor = float(row.get('Motor', 0))
            crisp_bus = float(row.get('Bus', 0))
            crisp_truk = float(row.get('Truk', 0))
            crisp_lebar = float(row['Lebar_Jalan'])
            crisp_panjang = float(row['Panjang_Jalan'])

            total_volume = Kendaraan.hitung_volume(crisp_mobil, crisp_motor, crisp_bus, crisp_truk)
            hasil_defuzz = hitung_lampu_merah(total_volume, crisp_lebar, crisp_panjang)

            print(f"{crisp_mobil:<6.0f} | {crisp_motor:<6.0f} | {crisp_bus:<6.0f} | {crisp_truk:<6.0f} | {total_volume:<8.1f} | {crisp_lebar:<6.1f} | {crisp_panjang:<8.0f} | {hasil_defuzz:<15.2f}")


if __name__ == "__main__":
    jalankan_pengujian('../data/test.csv')