mes = []
receita = []
despesa = []
totalR = 0
totalD = 0
for i in range(12):
    mes.append(str.lower(input('Qual o mês:')))
    receita.append(float(input('Qual a receita do mês {}'.format(mes[i]))))
    despesa.append(float(input('Qual a despesa do mês {}'.format(mes[i]))))

for a in receita:
    totalR += a
for b in despesa:
    totalD += b

print('Total de receitas obtidas no ano: {}'
      'Total de despesas do ano: {}'.format(totalR,totalD))

if totalR >= totalD:
    print('O saldo financeiro do ano foi positivo.')
else:
    print('O saldo financeiro do ano foi negativo.')

for c in range(len(mes)):
    if receita[c] > despesa[c]:
        print('No mês {} a receita superou as despesas.'.format(mes[c]))