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

# Endpoint untuk menghitung umur
@app.post("/umur")
def umur_for(request: LahirRequest):
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
    
    # Mengambil nama bulan lahir dan bulan saat ini
    bulan_lahir_nama = bulan_nama[bulan_lahir - 1]
    bulan_terkini = bulan_nama[bulan_sekarang - 1]
    
    # Format hasil akhir
    hasil_akhir = (
        f"Saya lahir pada {bulan_lahir_nama} {tahun_lahir},"
        f"Sekarang {bulan_terkini} {tahun_sekarang},"
        f"Umur saya adalah {umur_tahun} tahun {umur_bulan} bulan."
    )
    
    return {"Data": hasil_akhir}
