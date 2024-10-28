from typing import List
from model3 import PermintaanUmur

class RepositoryUmur:
    @staticmethod
    def hitung_umur_for_loop(permintaan: PermintaanUmur) -> List[str]:
        hasil = []
        for bulan in permintaan.bulan:  # Menggunakan bulan dari input
            if bulan < 1 or bulan > 12:
                continue  # Lewati bulan yang tidak valid

            nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                          "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

            umur_tahun = permintaan.tahun_sekarang - permintaan.tahun_lahir
            umur_bulan = bulan - permintaan.bulan_lahir

            if umur_bulan < 0:
                umur_tahun -= 1
                umur_bulan += 12
            
            hasil.append(f"[{nama_bulan[bulan - 1]} {permintaan.tahun_sekarang}] Umur saya {umur_tahun} tahun {umur_bulan} bulan" if umur_bulan > 0 
                           else f"[{nama_bulan[bulan - 1]} {permintaan.tahun_sekarang}] Umur saya {umur_tahun} tahun")
        
        return hasil

    @staticmethod
    def hitung_umur_for_each(permintaan: PermintaanUmur) -> List[str]:
        hasil = []
        
        for bulan in permintaan.bulan:  # Menggunakan bulan dari input
            if bulan < 1 or bulan > 12:
                continue  # Lewati bulan yang tidak valid

            nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                          "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

            umur_tahun = permintaan.tahun_sekarang - permintaan.tahun_lahir
            umur_bulan = bulan - permintaan.bulan_lahir
            
            if umur_bulan < 0:
                umur_tahun -= 1
                umur_bulan += 12
            
            hasil.append(f"[{nama_bulan[bulan - 1]} {permintaan.tahun_sekarang}] Umur saya {umur_tahun} tahun {umur_bulan} bulan" if umur_bulan > 0 
                           else f"[{nama_bulan[bulan - 1]} {permintaan.tahun_sekarang}] Umur saya {umur_tahun} tahun")
        
        return hasil

    @staticmethod
    def hitung_umur_while(permintaan: PermintaanUmur) -> List[str]:
        hasil = []
        index = 0
        
        while index < len(permintaan.bulan):  # Menggunakan bulan dari input
            bulan = permintaan.bulan[index]
            if bulan < 1 or bulan > 12:
                index += 1
                continue  # Lewati bulan yang tidak valid

            nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                          "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

            umur_tahun = permintaan.tahun_sekarang - permintaan.tahun_lahir
            umur_bulan = bulan - permintaan.bulan_lahir
            
            if umur_bulan < 0:
                umur_tahun -= 1
                umur_bulan += 12
            
            hasil.append(f"[{nama_bulan[bulan - 1]} {permintaan.tahun_sekarang}] Umur saya {umur_tahun} tahun {umur_bulan} bulan" if umur_bulan > 0 
                           else f"[{nama_bulan[bulan - 1]} {permintaan.tahun_sekarang}] Umur saya {umur_tahun} tahun")
            
            index += 1
        
        return hasil
