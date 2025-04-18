#function 1 
def HitungDiskon(harga,DiskonPersen):
    diskon = harga * (DiskonPersen/100)
    HargaSetelahDiskon = harga - diskon
    return HargaSetelahDiskon

#contoh penggunaan
HargaAwal = 100000
PersenDiskon = 10
HargaAKhir = HitungDiskon(HargaAwal,PersenDiskon)

#panggil function
print(f"harga awal : Rp {HargaAwal}")
print(f"diskon : {PersenDiskon}%")
print(f"harga setelah diskon : Rp {HargaAKhir}")