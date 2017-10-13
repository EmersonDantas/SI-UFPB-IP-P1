orcamento = []
totalR = 0
totalD = 0
for i in range(12):
    mes = str.lower(input('Qual o mês: '))
    receita = float(input('Qual a receita do mês {}: '.format(mes)))
    despesa = float(input('Qual a despesa do mês {}: '.format(mes)))
    orcamento.append([mes,receita,despesa])

for a in orcamento:
    totalR += a[1]
    totalD += a[2]

print('Total de receitas obtidas no ano: {}'
      'Total de despesas do ano: {}'.format(totalR,totalD))

if totalR >= totalD:
    print('O saldo financeiro do ano foi positivo.')
else:
    print('O saldo financeiro do ano foi negativo.')

for c in range(len(orcamento)):
    if orcamento[c][1] > orcamento[c][2]:
        print('No mês {} a receita superou as despesas.'.format(orcamento[c][0]))