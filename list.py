#membuat list --> bracket, constructor
nilai = [80,85,90,95,100]
#berbagi = list(('luan','helen','dheja'))

#ORDERED --> urutan data tetap
print('nilai minimal matkul :',nilai)
#print('penerima beasiswa berbagi :',berbagi)
print('-------------------------------------')

#DUPLICATE --> data ganda
#hasil = [75,80,95,95]
#buah = list(('apel','jeruk','leci','apel'))
#print('Nilai duplikat :',hasil)
#print('Buah duplikat :',buah)
#print('------------------------')

#INDEX --> 0
#ex: tampilkan nilai 90 
#nilaiIndex = nilai.index(90)
#print('jumlah nilai 90 :',nilaiIndex)
#print('-----------------------------')

#CHANGE
#TAMBAH DATA
# -> append: last, insert: index
#nilai.append(85)
#nilai.append(70)
#print('nilai hasil append :',nilai)
#print('----------------------------')

#ex: menambahkan nilai 70 pada index 3
#nilai.insert(3,70)
#print('nilai hasil insert :',nilai)
#print('--------------------------------')

#HAPUS DATA
# --> pop: last, remove: spesific
#nilai.pop()
#print('nilai hasil pop :',nilai)
#print('-------------------------')

#ex: hapus angka 95 dari nilai
#nilai.remove(95)
#print('nilai hasil remove :',nilai)
#print('-----------------------------')

#EDIT DATA
#ex: ganti angka 2 dengan 60
nilai[2] = 60
print('nilai hasil edit :',nilai)
print('-------------------------')