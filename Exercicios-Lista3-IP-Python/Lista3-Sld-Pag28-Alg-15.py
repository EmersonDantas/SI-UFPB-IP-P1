#Emerson Dantas S.I IP-P1
#02/08/2017 17:02

print('Digite o valor em reais:')
RS= int(input('R$'))
N100=RS/100
R1=RS%100
N50=R1/50
R2=R1%50
N10=R2/10
R3=R2%10
N5=R3/5
N1=R3%5
if N100 != 0:
    print('Notas de R$100:',int(N100))
else :
    print('Notas de R$100:0')
if N50 != 0:
    print('Notas de R$50:',int(N50))
else :
    print('Notas de R$50:0')
if N10 != 0:
    print('Notas de R$10:',int(N10))
else :
    print('0')
if N5 != 0:
    print('Notas de R$5:',int(N5))
else :
    print('Notas de R$5:0')
if N1 != 0:
    print('Notas de R$1:',int(N1))
else :
    print('Notas de R$1:0')
    


