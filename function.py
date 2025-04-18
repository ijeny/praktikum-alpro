#membuat function
def sapa():
    print('HALO!!')
    print('Selamat Datang di Toko Seiji!')
    print('-----------------------------')

def tanya():
    belanja = input('Apakah anda ingin berbelanja(ya/tidak)?')
    if belanja == "ya":
        print('Selamat Berbelanja!')
    else:
        print('Semoga Harimu Menyenangkan!')

#panggil function
sapa()
tanya()