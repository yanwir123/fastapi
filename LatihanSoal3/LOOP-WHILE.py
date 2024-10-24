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

# Endpoint dengan loop while, tapi hanya mengambil hasil akhir saja
@app.post("/umur")
def umur_while(request: LahirRequest):
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
    
    tahun = tahun_lahir
    bulan = bulan_lahir
    
    # Menggunakan while loop untuk iterasi waktu
    while tahun < tahun_sekarang or (tahun == tahun_sekarang and bulan < bulan_sekarang):
        bulan += 1
        if bulan > 12:
            bulan = 1
            tahun += 1
    
    # Hanya mengambil hasil akhir dari bulan dan tahun sekarang
    bulan_terkini = bulan_nama[bulan_sekarang - 1]
    hasil_akhir = f"[{bulan_terkini} {tahun_sekarang}] 'Umur saya {umur_tahun} tahun {umur_bulan} bulan'"
    
    return {"Data": hasil_akhir}
