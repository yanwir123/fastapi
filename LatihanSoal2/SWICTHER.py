from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Membuat model untuk menerima data dari body
class NilaiRequest(BaseModel):
    Matkul_1: int
    Matkul_2: int
    Proses: str

# Fungsi operasi dengan switch-case menggunakan dictionary
def operasi_aritmatika(angka_1: int, angka_2: int, operasi: str):
    # Dictionary yang bertindak sebagai "switch-case"
    def pembagian(angka_1, angka_2):
        if angka_2 == 0:
            raise HTTPException(status_code=400, detail="Pembagian dengan nol tidak diperbolehkan")
        return angka_1 / angka_2

    switcher = {
        "+": lambda: angka_1 + angka_2,
        "-": lambda: angka_1 - angka_2,
        "*": lambda: angka_1 * angka_2,
        "/": lambda: pembagian(angka_1, angka_2)
    }
    
    # Mengambil fungsi yang sesuai dari dictionary
    func = switcher.get(operasi)
    
    # Jika operasi tidak valid, raise HTTPException
    if func is None:
        raise HTTPException(status_code=400, detail="Operasi tidak valid. Gunakan +, -, *, atau /")
    
    # Menjalankan fungsi yang diambil dari dictionary
    return func()

@app.post("/proses")
def proses_nilai(request: NilaiRequest):
    
    angka_1 = request.Matkul_1
    angka_2 = request.Matkul_2
    operasi = request.Proses

    # Menghitung hasil operasi dengan menggunakan fungsi switch-case
    hasil = operasi_aritmatika(angka_1, angka_2, operasi)

    return {
        "Code": "200",
        "Mess": "succ",
        "Data": f"Hasil dari {angka_1} {operasi} {angka_2} adalah {hasil}"
    }
