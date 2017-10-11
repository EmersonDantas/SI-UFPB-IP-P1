medias = []
for i in range(10):
    nota0 = float(input('Digite a primeira nota:\n'))
    nota1 = float(input('Digite a segunda nota:\n'))
    nota2 = float(input('Digite a terceira nota:\n'))
    nota3 = float(input('Digite a quarta nota:\n'))
    media = (nota0 + nota1 + nota2 + nota3) / 4
    medias.append(media)
    print()

aprovados = 0
for i in medias:
    if i >= 7:
        aprovados += 1

print('Quantidade de alunos aprovados: {}'.format(aprovados))
