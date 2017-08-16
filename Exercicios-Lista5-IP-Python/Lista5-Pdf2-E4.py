#EMERSON DANTAS S.I IP-P1
num = float(input('Digite um número:'))
if num % 2 != 0:
    numpi = 'é impar'
else:
    numpi = 'não é impar'
if num % 3 == 0:
    numr3 = 'é múltipĺo de 3'
else:
    numr3 = 'não é múltipĺo de 3'
if 112 % num == 0:
    numd = 'é divisor de 112'
else:
    numd = 'não é divisor de 112'
print('O número {n} {pi}, {m} e {d}.'.format(n=num,pi=numpi,m=numr3,d=numd))