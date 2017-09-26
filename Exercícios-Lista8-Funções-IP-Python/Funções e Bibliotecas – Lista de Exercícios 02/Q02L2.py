import bibliotecaLista2

total = 0
listaAdd = []
listaTemp =[]
perguntas = ['Digite o nome do artista:\n','Digite o nome da obra:\n','Digite o preço da obra:\n','Digite o tipo de obra:\n']

for i in range(2):

    for n in range(len(perguntas)):

        entrada = input(perguntas[n])
        listaTemp.append(entrada)

    listaAdd.append(listaTemp)

    if listaTemp[0] == 'leonardo resende':

        preco = int(listaAdd[i][2])
        total += preco

    listaTemp = []

print('O preço total das obras de Leonado resende é R${}'.format(total))