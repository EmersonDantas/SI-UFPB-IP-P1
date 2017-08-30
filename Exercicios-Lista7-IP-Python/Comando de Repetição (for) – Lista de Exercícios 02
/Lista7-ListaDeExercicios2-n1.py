numMaisAntigo = 0
itemMVa = 0
valorTotal = 0
maiorV = 0
anoItemMaisValioso = 0
quantidade = int(input('Qual a quantidade de itens no estoque: '))
for i in range(quantidade):
    item = str.lower(input('Qual o item: '))
    ano = int(input('Qual o ano de fabricação de {0}: '.format(item)))
    valor = float(input('Qual o valor: '))
    if valor > maiorV:
        maiorV = valor
        itemMVa = item
        anoItemMaisValioso = ano
    if ano <= 1827:
        numMaisAntigo += 1
valorTotal += valor
valorMedio = valorTotal / quantidade
print('Itens produzidos antes de 1827: {nma}\n'
    'Valor médio dos itens: {vm:.2f}\n'
    'Dados do objeto mais valioso: {ima};{aima}'.format(nma = numMaisAntigo, vm = valorMedio, ima = itemMVa, aima = anoItemMaisValioso))
