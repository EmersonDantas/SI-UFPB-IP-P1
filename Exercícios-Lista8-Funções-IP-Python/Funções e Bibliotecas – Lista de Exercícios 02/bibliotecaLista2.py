listaAOP = [['vitas','obra1',90,'quadro'], ['vitas','obra2',100,'escultura'],
            ['irineu', 'obra3',123,'escultura'], ['irineu','obra4',1234,'quadro'],['leonardo resende','obradele',1000,'quadro']]

def adicionarValores(artista,obra,preco,tipo):

    listaAOP.append(artista,obra,preco,tipo)

def consultaPreco(titulo):
    titulo = str.lower(titulo)

    for index in listaAOP:
        if titulo == index[0]:
            preco = index[2]

    return preco

def consultaArtista(obra):

    obra = str.lower(obra)
    for index in listaAOP:
        if obra == index[1]:
            artista = index[0]

    return artista

def consultaQuantObras(artista):

    cont = 0

    artista = str.lower(artista)
    for index in listaAOP:
        if artista == index[0]:
            cont += 1

    return cont

def consultaTipo(obra):
    obra = str.lower(obra)

    for index in listaAOP:
        if obra == index[1]:
            tipo = index[3]

    return tipo

