#membuat function
#membuat function
def sapa(user):
    print('HALO!!',user)
    print('Selamat Datang di Toko Seiji!')
    print('-----------------------------')

def tanya():
    belanja = input('Apakah anda ingin berbelanja(ya/tidak)?')
    if belanja == "ya":
        print('Selamat Berbelanja!')
    else:
        print('Semoga Harimu Menyenangkan!')
        print('---------------------------')

#panggil function
sapa('chiro')
tanya()

#contoh 2
#membuat function 
def beli(harga,jumlah):
    jumlah = harga * jumlah
    print('Jumlah Belanja Anda : ',jumlah)
    print('-----------------------------')

#panggil function
beli(5000,6)