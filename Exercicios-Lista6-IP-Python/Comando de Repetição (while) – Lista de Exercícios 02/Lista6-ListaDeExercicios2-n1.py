'''Programa para ler 20 números e
exibir a soma dos pares'''
cont = 1
soma = 0
while (cont <= 20):
    numero = int(input('Digite um número:'))
    cont += 1
    if numero % 2 == 0:
        soma += numero
print(soma)
