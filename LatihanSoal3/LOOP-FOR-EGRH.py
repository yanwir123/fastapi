from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Model untuk menerima input dari user
class LahirRequest(BaseModel):
    tahun_lahir: int
    bulan_lahir: int

# Fungsi untuk menghitung umur dalam tahun dan bulan
def Umur(tahun_lahir, bulan_lahir):
    sekarang = datetime.now()
    tahun_sekarang = sekarang.year
    bulan_sekarang = sekarang.month

    # Menghitung umur dalam tahun dan bulan
    umur_tahun = tahun_sekarang - tahun_lahir
    umur_bulan = bulan_sekarang - bulan_lahir

    if umur_bulan < 0:
        umur_tahun -= 1
        umur_bulan += 12

    return umur_tahun, umur_bulan

# Endpoint dengan loop for-each (for loop di Python)
@app.post("/umur")
def umur_for_each(request: LahirRequest):
    tahun_lahir = request.tahun_lahir
    bulan_lahir = request.bulan_lahir
    
    sekarang = datetime.now()
    tahun_sekarang = sekarang.year
    bulan_sekarang = sekarang.month
    
    umur_tahun, umur_bulan = Umur(tahun_lahir, bulan_lahir)
    bulan_nama = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    
    hasil = []
    
    # Menggunakan for loop untuk iterasi
    for tahun in range(tahun_lahir, tahun_sekarang + 1):
        if tahun == tahun_lahir:
            mulai_bulan = bulan_lahir
        else:
            mulai_bulan = 1
        
        if tahun == tahun_sekarang:
            akhir_bulan = bulan_sekarang
        else:
            akhir_bulan = 12

        for bulan in range(mulai_bulan, akhir_bulan + 1):
            hasil.append(f"[{bulan_nama[bulan-1]} {tahun}] 'Umur saya {tahun - tahun_lahir} tahun {bulan - bulan_lahir} bulan'")
    
    # Mengambil hasil akhir dari list hasil
    hasil_akhir = hasil[-1] if hasil else "Data tidak ditemukan"

    return {"Data": hasil_akhir}
