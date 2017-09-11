pessoas = 5
totalidade = 0
for i in range(pessoas):
    idade = int(input('Quantos anos você tem:\n'))
    totalidade += idade
media = totalidade / pessoas
if media > 0 and media <= 25:
    print('Turma jovem.')
elif media > 25 and media < 60:
    print('Turma adulta.')
else:
    print('Turma idosa.')
