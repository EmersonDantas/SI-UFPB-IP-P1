#EMERSON DANTAS S.I IP-P1
num = int(input('Digite um número:'))
if num % 2 == 0:
    numres = 'Par'
else:
    numres = 'Impar'
print('O número {n} é {r}'.format(n=num,r=numres))