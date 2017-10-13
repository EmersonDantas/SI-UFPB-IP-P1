nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))
media = (nota1 + nota2) / 2

if media == 9 or media == 10:
    conceito = 'A'
elif media >= 7.5 and media <= 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
elif media >= 0 and media < 4:
    conceito = 'E'
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    situ = 'APROVADO'
else:
    situ = 'REPROVADO'

print('1º nota: {} \n2º nota: {} \nMédia: {}\n'
      'Conceito: {}\nSituação: {}'.format(nota1,nota2,media,conceito,situ))

