vetor = []
soma = 0
for i in range(10):
    vetor.append(int(input('Digite um número inteiro:\n')))

for a in vetor:
    soma += a**2

print(soma)
