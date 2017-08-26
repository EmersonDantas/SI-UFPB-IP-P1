'''Programa para ler 30 números e
exibir a quantidade de positivos'''
cont = 0
qtdePositivos = 0
while cont < 30:
    cont += 1
    numero = int(input('Digite um número:'))
    if (numero > 0):
        qtdePositivos += 1
print('A quantidade de números positivos é {0}'.format(qtdePositivos))