from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Membuat model untuk menerima data dari body
class NilaiRequest(BaseModel):
    Matkul_1: int
    Matkul_2: int
    Proses: str

# Fungsi aritmatika dengan ternary operator
def operasi_aritmatika(angka_1: int, angka_2: int, operasi: str):
    hasil = (
        angka_1 + angka_2 if operasi == "+" else
        angka_1 - angka_2 if operasi == "-" else
        angka_1 * angka_2 if operasi == "*" else
        (angka_1 / angka_2 if angka_2 != 0 else None) if operasi == "/" else
        None
    )

    if hasil is None:
        if operasi == "/" and angka_2 == 0:
            raise HTTPException(status_code=400, detail="Pembagian dengan nol tidak diperbolehkan")
        else:
            raise HTTPException(status_code=400, detail="Operasi tidak valid. Gunakan +, -, *, atau /")

    return hasil

@app.post("/proses")
def proses_nilai(request: NilaiRequest):
    angka_1 = request.Matkul_1
    angka_2 = request.Matkul_2
    operasi = request.Proses

    # Menghitung hasil operasi dengan menggunakan ternary operator
    hasil = operasi_aritmatika(angka_1, angka_2, operasi)

    return {
        "Code": "200",
        "Mess": "succ",
        "Data": f"Hasil dari {angka_1} {operasi} {angka_2} adalah {hasil}"
    }
