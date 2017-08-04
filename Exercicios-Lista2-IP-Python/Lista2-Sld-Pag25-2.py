from math import sqrt
A= 2
B= 7
C= 1
D= ((B**2)-(4*A*C))
print("Delta é:", D)
#bhaskara
if D<0 :
        print ("Raiz negativa NÃO pode ser extraida. Saindo...")
        exit()
else :
    sqrt(D)
    X1=((-B+D)/(2*A))
    X2=((-B-D)/(2*A))
    print("X':",X1,"\n""X'':",X2)
