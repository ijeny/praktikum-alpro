#input
print('PREDIKAT IPK')
IPK = float(input('masukkan IPK anda :'))
#proses
if IPK >= 3.4 :
    status = 'PERBAIKAN'
    if IPK >= 3.7 :
        status = 'LULUS'
        predikat = 'MEMUASKAN'
    else :
        predikat = 'CUKUP'
else :
    status = 'GAGAL'
    predikat = 'KURANG'

#output
print('status :',status)
print('predikat :',predikat)
print('--------------------')