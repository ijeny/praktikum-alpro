# CREATE -->  bracket, constructor
tuple1 = ('Luna',25)
#tuple2 = tuple(('Luna','Helen'))

# ORDERED --> urutan data tetap
print('data: ',tuple1)
#print('data: ',tuple2)
print('----------------')

#DUPLICATE --> data ganda
#tuple1 = ('Luna',25,25)
#tuple2 = tuple(('Luna','Helen','Helen'))
#print('duplikat: ',tuple1)
#print('duplikat: ',tuple2)
#print('-------------------------------')

#INDEX --> 0
#ex: menampilkan no index angka 25
#index = tuple1.index(25)
#print('index angka 25: ',index)
#print('-----------------------------')

#UNCHANGABLE --> tidak dapat dirubah
#ex: ubah data index 1 dengan 35
tuple1[1] = 35
print('hasil diubah: ',tuple1)
print('-------------------------')