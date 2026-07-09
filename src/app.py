import streamlit as st
from fuzzy_model import Kendaraan, hitung_lampu_merah

st.set_page_config(page_title="Simulasi Fuzzy Lampu Lalu Lintas", layout="centered")

st.title("Sistem Kendali Lampu Lalu Lintas Adaptif")
st.markdown("Implementasi logika Fuzzy Mamdani berdasarkan volume kendaraan (SMP), lebar jalan, dan panjang antrean.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Kendaraan")
    input_mobil = st.number_input("Jumlah Mobil", min_value=0, max_value=200, value=20, step=1)
    input_motor = st.number_input("Jumlah Motor", min_value=0, max_value=300, value=50, step=1)
    input_bus = st.number_input("Jumlah Bus", min_value=0, max_value=100, value=0, step=1)
    input_truk = st.number_input("Jumlah Truk", min_value=0, max_value=100, value=0, step=1)

with col2:
    st.subheader("Data Infrastruktur")
    input_lebar = st.slider("Lebar Jalan (meter)", min_value=5.0, max_value=15.0, value=8.0, step=0.1)
    input_panjang = st.slider("Panjang Antrean (meter)", min_value=10.0, max_value=100.0, value=30.0, step=1.0)

st.markdown("---")

if st.button("Hitung Durasi Lampu Merah", type="primary"):
    total_volume = Kendaraan.hitung_volume(input_mobil, input_motor, input_bus, input_truk)
    hasil_detik = hitung_lampu_merah(total_volume, input_lebar, input_panjang)

    st.success("Komputasi Fuzzy Berhasil!")

    metrik1, metrik2 = st.columns(2)
    metrik1.metric(label="Total Volume (SMP)", value=f"{total_volume:.1f}")
    metrik2.metric(label="Durasi Lampu Merah", value=f"{hasil_detik:.2f} Detik")