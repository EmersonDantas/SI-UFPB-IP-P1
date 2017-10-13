atleta = str(input('Nome do atleta:\n'))
nota = float(input('Digite sua nota:\n'))
menornota = nota
maiornota = nota
total = nota

for i in range(6):
    nota = float(input('Digite sua nota:\n'))
    total += nota
    if nota > maiornota:
        maiornota = nota
    if nota < menornota:
        menornota = nota
media = (total - (menornota + maiornota))/5

print('Resultado final:\n' 
      'Atleta: {}\n'
      'Melhor nota: {}\n'
      'Pior nota: {}\n'
      'Média: {:.2f}'.format(atleta,maiornota,menornota,media))
