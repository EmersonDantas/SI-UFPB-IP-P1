notas = []
cont = 0
for i in range (5):
    nota = float(input('Digite uma nota:\n'))
    notas.append(nota)

for a in range(len(notas)):
    if notas[a] > 8:
        cont += 1
print(cont)