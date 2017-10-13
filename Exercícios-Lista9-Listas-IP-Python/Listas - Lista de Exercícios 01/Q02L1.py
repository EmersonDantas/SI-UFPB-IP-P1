lista = []
for i in range(5):
    n = int(input('Digite um número inteiro:\n'))
    lista.append(n)

menor = lista[0]
for a in range(len(lista)):
    if lista[a] < menor:
        menor = lista[a]
print(menor)