#input
print('TRANSKIP IPK')
ipk = float(input('masukkan IPK anda : '))

#proses
if ipk > 3.85 :
    transkip = 'A'
elif ipk > 3.60 :
    transkip = 'B'
elif ipk > 3.45 :
    transkip = 'C'
elif ipk > 3.35 :
    transkip = 'D'
else :
    transkip = 'E'

#output
print('nilai transkip IPK anda :',transkip)
print('-----------------------------------')