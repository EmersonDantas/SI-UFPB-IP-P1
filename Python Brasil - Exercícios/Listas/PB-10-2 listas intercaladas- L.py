vetorA = []
vetorB = []
vetorC = []

for a in range(10):
    vetorA.append(int(input('Digite um número inteiro:\n')))

for b in range(10):
    vetorB.append(int(input('Digite um número inteiro:\n')))

for c in range(len(vetorA)):
    vetorC.append(vetorA[c])
    vetorC.append(vetorB[c])
print(vetorC)
