maior = 0
for i in range(5):
    numero = float(input('Digite um número:\n'))
    if numero > maior:
        maior = numero
print('O maior número é: {}'.format(maior))
