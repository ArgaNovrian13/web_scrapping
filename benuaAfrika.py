import requests
from bs4 import BeautifulSoup
import pandas as pd
#  Mengambil Data-Data Nama Negara Benua Afrika
url = 'https://id.m.wikipedia.org/wiki/Daftar_negara_menurut_benua'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    section = soup.find('section', class_="mf-section-1")
    table = section.find('table', class_='wikitable sortable')
    if table:
        rows = table.find_all('tr')
        # Inisialisasi list untuk header dan data
        table_data = []
        isi_data = []
        # Proses setiap baris tabel
        for row in rows:
            headers = row.find_all('th')
            cells = row.find_all('td')
            if headers:
                header_text = [header.get_text(strip=True) for header in headers]
                table_data.append(header_text)
            if cells:
                cells_text = [cell.get_text(strip=True) for cell in cells]
                isi_data.append(cells_text)
        # Cetak header dan data
        for row_data in table_data:
            print(row_data)
        for row_data in isi_data:
            print(row_data)
        # Simpan ke file Excel jika ada data
        if table_data and isi_data:
            df = pd.DataFrame(isi_data, columns=table_data[0])
            df.to_excel('Negara-negara-Benua-Afrika.xlsx', index=False)
            print("Data berhasil disimpan ke file Excel")
    else:
        print("Tabel tidak ditemukan di halaman")
else:
    print("Gagal memuat URL")
