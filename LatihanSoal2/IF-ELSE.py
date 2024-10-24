from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

# Membuat model untuk menerima data dari body
class NilaiRequest(BaseModel):
    Matkul_1: int
    Matkul_2: int
    Proses: str

@app.get("/proses")
def get_NilaiRequest(Matkul_1: int, Matkul_2: int, Proses: str):
    print(Matkul_1, Matkul_2, Proses)
    print(type(Matkul_1), type(Matkul_2), type(Proses))
    return {
        "Code": "200",
        "Mess": "succ",
        "Data": f"Nilai {Matkul_1} dan Nilai {Matkul_2}"
    }

@app.post("/proses")
def operasi_aritmatika(request: NilaiRequest):
    angka_1 = request.Matkul_1
    angka_2 = request.Matkul_2
    operasi = request.Proses

    # Memilih operasi berdasarkan input
    if operasi == "+":
        hasil = angka_1 + angka_2
        operator = "penjumlahan"
    elif operasi == "-":
        hasil = angka_1 - angka_2
        operator = "pengurangan"
    elif operasi == "*":
        hasil = angka_1 * angka_2
        operator = "perkalian"
    elif operasi == "/":
        if angka_2 == 0:
            raise HTTPException(status_code=400, detail="Pembagian dengan nol tidak diperbolehkan")
        hasil = angka_1 / angka_2
        operator = "pembagian"
    else:
        raise HTTPException(status_code=400, detail="Operasi tidak valid. Gunakan +, -, *, atau /")

    return {
        "Code": "200",
        "Mess": "succ",
        "Data": f"Nilai Matkul 1 Adalah {angka_1} {operator} Dengan Nilai Matkul 2 Adalah {angka_2} Hasil Adalah {hasil}, Ini Adalah Nilai Anda Dalam Semester Susulan.",
    }
