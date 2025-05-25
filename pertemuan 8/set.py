#MEMBUAT SET --> bracket, constructor
set1 = {'N','J','S',5}
#set2 = set(('N','J','Z',6))

#UNORDERED --> urutan tidak sama
print('data: ',set1)
#print('data: ',set2)
print('---------------')

#UNDUPLICATE --> unique
#set1 = {'N','J','S',5,5}
#set2 = set(('N','J','Z',6,6))
#print('duplikat: ',set1)
#print('duplikat: ',set2)
#print('---------------')

#UNINDEXED --> tidak punya index
#ex: menampilkan index angka 1
#Myindex = set1.index(1)
#print('index angka 1: ',Myindex)
#print('-------------------------')

#UNCHANGABLE --> tidak dapat dirubah
#ex: ubah angka index 3 dan 9
#set1[3] = 9
#print('Hasil edit: ',set1)
#print('-----------------------------')

#MENAMBAHKAN DATA --> add
#set1.add(4)
#print('hasil add: ',set1)
#print('--------------------')

#HAPUS DATA
#pop: random, remove: spesific
#set1.pop()
#print('hasil pop: ',set1)
#print('---------------------')

#ex: hapus 'J' dari set1
set1.remove('J')
print('hasil remove: ',set1)
print('----------------------------')