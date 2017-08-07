#Emerson Dantas S.I IP-P1
#02/08/2017 17:02

print('Digite o valor em reais:')
RS= int(input('R$'))
N100=int(RS/100)
R1=int(RS%100)
N50=int(R1/50)
R2=int(R1%50)
N10=int(R2/10)
R3=int(R2%10)
N5=int(R3/5)
N1=int(R3%5)
print('Notas de R$100: {N100:d}\nNotas de R$50: {N50:d}\nNotas de R$10: {N10:d}\nNotas de R$5: {N5:d}\nNotas de R$1: {N1:d}'.format(N100=N100,N50=N50,N10=N10,N5=N5,N1=N1))
    


