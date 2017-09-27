import bibliotecaLista2

total = 0
listaAdd = []
listaTemp =[]
perguntas = ['Digite o nome do artista:\n','Digite o nome da obra:\n','Digite o preço da obra:\n','Digite o tipo de obra:\n']

for i in range(60):
    for n in range(len(perguntas)):
        if n!= [2]:
            entrada = str(input(perguntas[n]))
        else:
            entrada = float(input(perguntas[n]))
        listaTemp.append(entrada)
    listaAdd.append(listaTemp)

    if str.lower(listaTemp[0]) == 'leonardo resende':
        preco = float(listaAdd[i][2])
        total += preco

    listaTemp = []

print('O preço total das obras de Leonado resende é R${:.2f}'.format(total))