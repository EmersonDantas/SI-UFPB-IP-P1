from math import sqrt
A= float(10.0)
B= float(20.1)
C= float(5.1)
D= ((B**2)-(4*A*C))
if D<=0 :
        print ("Impossivel calcular\n")
        exit()
X1=((-B+sqrt(D))/(2*A))
X2=((-B-sqrt(D))/(2*A))
print("R1 = %f \nR2 = %f\n" %(X1,X2))