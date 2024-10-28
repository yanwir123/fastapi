from fastapi import APIRouter, Query
from typing import List
from repo import ArithmeticRepository
from model import ArithmeticRequest
from repo3 import RepositoryUmur
from model3 import PermintaanUmur

router = APIRouter()

@router.get("/mahasiswa/")
def get_mahasiswa(nama: str = Query(...), tahun_masuk: int = Query(...)):
    return f"{nama} adalah seorang mahasiswa TI Unpam, saya masuk tahun {tahun_masuk}"

@router.post("/arithmetic/calculate_if_else/")
def calculate_if_else(request: ArithmeticRequest) -> dict:
    return ArithmeticRepository.calculate_if_else(request)

@router.post("/arithmetic/calculate_switch/")
def calculate_switch(request: ArithmeticRequest) -> dict:
    return ArithmeticRepository.calculate_switch(request)

@router.post("/arithmetic/calculate_ternary/")
def calculate_ternary(request: ArithmeticRequest) -> dict:
    return ArithmeticRepository.calculate_ternary(request)

# Endpoint untuk menghitung umur
@router.post("/umur/hitung_for_loop/")
def hitung_umur_for_loop(permintaan: PermintaanUmur) -> List[str]:
    return RepositoryUmur.hitung_umur_for_loop(permintaan)

@router.post("/umur/hitung_for_each/")
def hitung_umur_for_each(permintaan: PermintaanUmur) -> List[str]:
    return RepositoryUmur.hitung_umur_for_each(permintaan)

@router.post("/umur/hitung_while/")
def hitung_umur_while(permintaan: PermintaanUmur) -> List[str]:
    return RepositoryUmur.hitung_umur_while(permintaan)