soma = 0
cont = 0
listaTemp = []
listaTotal = []
perguntas = ['Digite o nome do artista:\n','Digite o nome da obra:\n','Digite o preço da obra:\n','Digite o tipo de obra:\n']
for i in range(4):
    for n in range(len(perguntas)):
        if n != 2:
            entrada = str(input(perguntas[n]))
        else:
            entrada = float(input(perguntas[n]))

        listaTemp.append(entrada)

    listaTotal.append(listaTemp)
    listaTemp = []

    if str.lower(listaTotal[i][3]) == 'quadro':
        soma += float(listaTotal[i][2])
        cont += 1

print('A média dos preços dos quadros é R${:.2f}'.format(soma/cont))