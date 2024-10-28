from pydantic import BaseModel
from typing import List

class PermintaanUmur(BaseModel):
    bulan_lahir: int
    tahun_lahir: int
    tahun_sekarang: int
    bulan: List[int]  # Daftar bulan