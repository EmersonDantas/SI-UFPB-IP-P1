vetorA = []
vetorB = []
vetorC = []
vetorD = []

for a in range(10):
    vetorA.append(int(input('Digite um número inteiro:\n')))

for b in range(10):
    vetorB.append(int(input('Digite um número inteiro:\n')))

for c in range(10):
    vetorC.append(int(input('Digite um número inteiro:\n')))

for d in range(len(vetorA)):
    vetorD.append(vetorA[d])
    vetorD.append(vetorB[d])
    vetorD.append(vetorC[d])

print(vetorD)
