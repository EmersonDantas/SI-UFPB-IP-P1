lista = []
m3 = []
for i in range(8):
    n = int(input('Digite um número inteiro:\n'))
    lista.append(n)

for a in range(len(lista)):
    if lista[a] % 3 == 0:
        m3.append(lista[a])
print(m3)