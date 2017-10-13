lista = []
soma = []
for i in range(4):
    n = int(input('Digite um número inteiro:\n'))
    lista.append(n)
for i in range(len(lista)-1):
    soma.append(lista[i]+lista[i+1])
soma.append(lista[-1])
print(soma)