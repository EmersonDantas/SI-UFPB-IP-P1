'''Escreva um programa que receba como entrada 50 números e exiba a soma dos que são
múltiplos de 3.'''
cont = 1
soma = 0
while (cont <= 50):
    numero = int(input('Digite um número:'))
    cont += 1
    if numero % 3 == 0:
        soma += numero
print('A soma dos números digitados que são multiplos de 3 é: {m3}'.format(m3=soma))
