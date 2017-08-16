#EMERSON DANTAS S.I IP-P1
num = float(input('Digite um número:'))
if num > 0:
    numres = 'Positivo'
elif num < 0:
    numres = 'Negativo'
else:
    numres = 'Neutro'
print('O número {n} é {r}.'.format(n=num,r=numres))