turmas = []
soma = 0
for i in range(4):
    quantidade = int(input('Quantidade de alunos da turma:\n'))
    turmas.append(quantidade)
for a in range(len(turmas)):
    soma += turmas[a]
print(soma)