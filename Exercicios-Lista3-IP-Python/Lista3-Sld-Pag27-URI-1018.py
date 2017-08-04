RS= 1577
N100=RS/100
R1=RS%100
N50=R1/50
R2=R1%50
N20=R2/20
R3=R2%20
N10=R3/10
R4=R3%10
N5=R3/5
R5=R3%5
N2=R5/2
N1=R5%2
if N100 != 0:
    print('Notas de R$100:',int(N100))
else :
    print('0')

if N50 != 0:
          print('Notas de R$50:',int(N50))
else :
          print('0')
if N20 != 0:
    print('Notas de R$20:',int(N20))
else :
    print('0')

if N10 != 0:
                print('Notas de R$10:',int(N10))
else :
                print('0')

if N5 != 0:
                      print('Notas de R$5:',int(N5))
else :
                      print('0')
if N2 != 0:
                      print('Notas de R$2:',int(N2))
else :
                      print('0')

if N1 != 0:
    print('Notas de R$1:',int(N1))
else :
    print('0')
    


