salariosTot = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],[1000]]
lista = [0,0,0,0,0,0,0,0,0]
continuar = 'sim'

while continuar != 'não':
    venda = float(input('Quantos R$ obtidos com suas vendas:\n'))
    salario = venda * 0.09 + 200
    if salario < 1000:
        for i in range(len(salariosTot)):
            if salario >= salariosTot[i][0] and salario <= salariosTot[i][1]:
                lista[i] += 1
    else:
        lista[8] += 1
    continuar = str.lower(input('Continuar? Sim ou Não:\n'))

for a in range(len(lista)):
    print('{} = {}' .format(salariosTot[a],lista[a]))
