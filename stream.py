import streamlit as st
import os
import requests

# Nama file lokal
local_filename = 'stream.py'


  
# Membuat pilihan untuk memilih web yang ingin diakses
option = st.radio(
    "Pilih aplikasi yang ingin diakses:",
    ('Stream 1', 'Stream 2')
)

# Mengarahkan ke stream.py sesuai dengan pilihan
if st.button('Akses Web'):
    if option == 'Stream 1':
        st.write("Mengakses Stream 1...")
      
        url = 'https://raw.githubusercontent.com/Analyst-FPnA/GIS-Cleaning/main/GIS.py'
        # Mengunduh file dari GitHub
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_filename, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download file: {response.status_code}")
        
        # Menjalankan file yang diunduh
        with open(local_filename, 'r') as f:
            exec(f.read())
          
    elif option == 'Stream 2':
        st.write("Mengakses Stream 2...")
      
        url = 'https://raw.githubusercontent.com/Analyst-FPnA/Rekap-SCM/main/stream.py'
        # Mengunduh file dari GitHub
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_filename, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download file: {response.status_code}")
        
        # Menjalankan file yang diunduh
        with open(local_filename, 'r') as f:
            exec(f.read())
