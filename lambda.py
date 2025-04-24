#function
def hitung(p,l):
    luas = p*l
    return luas
print('luas tanah (function) :',hitung(50,20))

#LAMBDA
#cara 1 : use variable
luas = lambda p,l : p*l
print('luas tanah (lambda_1) :',luas(50,20))

#cara 2 : directly
print('luas tanah (lambda_2) :',(lambda p,l : p*l)(50,20))