cont = 0
listaTotal = []
listaTemp =[]
perguntas = ['Digite o nome do artista:\n','Digite o nome da obra:\n','Digite o preço da obra:\n','Digite o tipo de obra:\n']

for i in range(30):
    for n in range(len(perguntas)):
        if n!= [2]:
            entrada = str(input(perguntas[n]))
        else:
            entrada = float(input(perguntas[n]))

        listaTemp.append(entrada)
    listaTotal.append(listaTemp)
    if str.lower(listaTemp[0]) == 'adélia machado' and str.lower(listaTemp[3]) == 'escultura':
        cont += 1
    listaTemp = []

print('Adélia Machado possui {} escultura(s).'.format(cont))