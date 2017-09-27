def consultaPreco(obra,listaAOPT):
    obra = str.lower(obra)

    for index in listaAOPT:
        if obra == str.lower(index[1]):
            return index[2]

def consultaArtista(obra,listaAOPT):

    obra = str.lower(obra)
    for index in listaAOPT:
        if obra == str.lower(index[1]):
            return index[0]

def consultaQuantObras(artista,listaAOPT):

    cont = 0
    artista = str.lower(artista)
    for index in listaAOPT:
        if artista == str.lower(index[0]):
            cont += 1

    return cont

def consultaTipo(obra,listaAOPT):
    obra = str.lower(obra)

    for index in listaAOPT:
        if obra == str.lower(index[1]):
            return index[3]