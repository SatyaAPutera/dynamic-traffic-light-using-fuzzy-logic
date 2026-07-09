import numpy as np

class Kendaraan:
    BOBOT_MOBIL = 1.0
    BOBOT_MOTOR = 0.3
    BOBOT_BUS = 1.2
    BOBOT_TRUK = 1.3

    @staticmethod
    def hitung_volume(jumlah_mobil, jumlah_motor, jumlah_bus, jumlah_truk):
        volume_total = (
            (jumlah_mobil * Kendaraan.BOBOT_MOBIL) +
            (jumlah_motor * Kendaraan.BOBOT_MOTOR) +
            (jumlah_bus * Kendaraan.BOBOT_BUS) +
            (jumlah_truk * Kendaraan.BOBOT_TRUK)
        )
        return volume_total


def _trapmf(x, a, b, c, d):
    if x <= a or x >= d:
        return 0.0
    if a < x < b:
        return (x - a) / (b - a) if b > a else 1.0
    if b <= x <= c:
        return 1.0
    if c < x < d:
        return (d - x) / (d - c) if d > c else 1.0
    return 0.0


def _trimf(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    if x == b:
        return 1.0
    if a < x < b:
        return (x - a) / (b - a) if b > a else 1.0
    if b < x < c:
        return (c - x) / (c - b) if c > b else 1.0
    return 0.0


def _membership(value, params):
    if len(params) == 4:
        return _trapmf(value, *params)
    return _trimf(value, *params)

VOLUME_SETS = {
    'sedikit': (0, 0, 50, 100),
    'sedang': (70, 125, 180),
    'banyak': (150, 200, 250, 250),
}

LEBAR_JALAN_SETS = {
    'sempit': (5, 5, 6, 8),
    'sedang': (6, 8, 10),
    'lebar': (8, 10, 15, 15),
}

PANJANG_JALAN_SETS = {
    'pendek': (10, 10, 30, 50),
    'sedang': (30, 55, 80),
    'panjang': (60, 80, 100, 100),
}

OUTPUT_SETS = {
    'cepat': (0, 0, 20, 25),
    'sedang': (20, 30, 40),
    'lama': (35, 40, 70, 70),
}

RULES = [
    ('sedikit', 'sempit', 'pendek', 'lama'),
    ('sedikit', 'sempit', 'sedang', 'sedang'),
    ('sedikit', 'sempit', 'panjang', 'cepat'),
    
    ('sedikit', 'sedang', 'pendek', 'lama'),
    ('sedikit', 'sedang', 'sedang', 'sedang'),
    ('sedikit', 'sedang', 'panjang', 'sedang'),
    
    ('sedikit', 'lebar', 'pendek', 'lama'),
    ('sedikit', 'lebar', 'sedang', 'lama'),
    ('sedikit', 'lebar', 'panjang', 'sedang'),

    ('sedang', 'sempit', 'pendek', 'sedang'),
    ('sedang', 'sempit', 'sedang', 'cepat'),
    ('sedang', 'sempit', 'panjang', 'cepat'),
    
    ('sedang', 'sedang', 'pendek', 'sedang'),
    ('sedang', 'sedang', 'sedang', 'sedang'),
    ('sedang', 'sedang', 'panjang', 'cepat'),
    
    ('sedang', 'lebar', 'pendek', 'lama'),
    ('sedang', 'lebar', 'sedang', 'sedang'),
    ('sedang', 'lebar', 'panjang', 'sedang'),

    ('banyak', 'sempit', 'pendek', 'cepat'),
    ('banyak', 'sempit', 'sedang', 'cepat'),
    ('banyak', 'sempit', 'panjang', 'cepat'),
    
    ('banyak', 'sedang', 'pendek', 'sedang'),
    ('banyak', 'sedang', 'sedang', 'cepat'),
    ('banyak', 'sedang', 'panjang', 'cepat'),
    
    ('banyak', 'lebar', 'pendek', 'sedang'),
    ('banyak', 'lebar', 'sedang', 'sedang'),
    ('banyak', 'lebar', 'panjang', 'cepat'),
]


def hitung_lampu_merah(volume, lebar_jalan, panjang_jalan):
    universe = np.arange(0, 71, 1)
    aggregated = np.zeros(len(universe), dtype=float)

    for volume_label, lebar_label, panjang_label, output_label in RULES:
        strength = min(
            _membership(volume, VOLUME_SETS[volume_label]),
            _membership(lebar_jalan, LEBAR_JALAN_SETS[lebar_label]),
            _membership(panjang_jalan, PANJANG_JALAN_SETS[panjang_label]),
        )
        if strength <= 0:
            continue

        output_membership = np.array([
            _membership(value, OUTPUT_SETS[output_label]) for value in universe
        ], dtype=float)
        aggregated = np.maximum(aggregated, np.minimum(output_membership, strength))

    total_strength = aggregated.sum()
    if total_strength == 0:
        return 35.0

    return float(np.sum(universe * aggregated) / total_strength)


def sistem_fuzzy():
    return {
        'volume': VOLUME_SETS,
        'lebar_jalan': LEBAR_JALAN_SETS,
        'panjang_jalan': PANJANG_JALAN_SETS,
        'lampu_merah': OUTPUT_SETS,
    }