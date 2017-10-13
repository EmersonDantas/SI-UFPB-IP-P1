numero = int(input('Digite um número:\n'))
cont = 0
for i in range(numero+1):
    if numero % i == 0:
        cont += 1
if cont == 2:
    print('O número {} é primo.'.format(numero))
else:
    print('O número {} não é primo.'.format(numero))
