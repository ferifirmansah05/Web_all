import streamlit as st
import requests
from streamlit_option_menu import option_menu

# Membuat navigasi bar
option = option_menu(
    menu_title="Pilih Aplikasi Web",  # required
    options=["Stream 1", "Stream 2"],  # required
    icons=["house", "gear"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

# Fungsi untuk menjalankan file python yang diunduh
def run_stream_script(url):
    # Mengunduh file dari GitHub
    response = requests.get(url)
    if response.status_code == 200:
        # Menjalankan file yang diunduh
        exec(response.text, globals())
    else:
        st.error(f"Failed to download file: {response.status_code}")

# Arahkan ke aplikasi berdasarkan pilihan pengguna
if option == 'Stream 1':
    st.write("Mengakses Stream 1...")
    stream1_url = 'https://raw.githubusercontent.com/Analyst-FPnA/GIS-Cleaning/main/GIS.py'
    run_stream_script(stream1_url)
  
elif option == 'Stream 2':
    st.write("Mengakses Stream 2...")
    stream2_url = 'https://raw.githubusercontent.com/Analyst-FPnA/Rekap-SCM/main/stream.py'
    run_stream_script(stream2_url)

