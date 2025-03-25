#input
print('MENENTUKAN UMUR PEMBUATAN KTP')
umur=int(input('masukkan umur : '))

#proses
if umur >= 16 :
    status = 'buat KTP'
else :
    status =  'belum waktunya'

#output
print('status :',status)
print('---------------')