orcamento = []
totalR = 0
totalD = 0
for i in range(12):
    mes = str.lower(input('Qual o mês: '))
    receita = float(input('Qual a receita do mês {}: '.format(mes)))
    despesa = float(input('Qual a despesa do mês {}: '.format(mes)))
    orcamento.append([mes,receita,despesa])

maiorDespesa = orcamento[0][2]
mesMD = orcamento[0][0]
for a in orcamento:
    totalR += a[1]
    totalD += a[2]
    if a[2] > maiorDespesa:
        maiorDespesa = a[2]
        mesMD = a[0]

print('Total de receitas obtidas no ano: R${:.2f}\n'
      'Total de despesas do ano: R${:.2f}'.format(totalR,totalD))

if totalR >= totalD:
    print('O saldo financeiro do ano foi positivo.')
else:
    print('O saldo financeiro do ano foi negativo.')

for c in range(len(orcamento)):
    if orcamento[c][1] > orcamento[c][2]:
        print('No mês {} a receita superou as despesas.'.format(orcamento[c][0]))

for d in orcamento:
    if d[1] > 2500:
        print('No mês {} a receita foi superior a R$2500.'.format(d[0]))
print('O mês em que houve a maior despesa foi {}.'.format(mesMD))
print('A receita média anual é R${:.2f}'.format(totalR/len(orcamento)))