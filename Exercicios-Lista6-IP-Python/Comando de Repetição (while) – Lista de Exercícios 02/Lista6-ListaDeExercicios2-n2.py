'''Escreva um programa que receba como entrada 25 números e exiba a quantidade de
números que são pares e positivos.'''
cont = 1
numpar = 0
numposi = 0
while (cont <= 25):
    numero = int(input('Digite um número:'))
    cont += 1
    if numero % 2 == 0:
        numpar += 1
        if numero > 0:
            numposi += 1
print('Quantidade de números pares: {pa}\nQuantidade de números pares positivos: {po}'.format(pa=numpar, po=numposi))
