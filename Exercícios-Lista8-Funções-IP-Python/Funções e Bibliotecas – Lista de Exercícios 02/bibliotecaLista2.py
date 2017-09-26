listaAOPT = []

def adicionarValores(listaAdd):

    listaAOPT.append(listaAdd)

def consultaPreco(titulo):
    titulo = str.lower(titulo)

    for index in listaAOPT:
        if titulo == index[0]:
            return index[2]

def consultaArtista(obra):

    obra = str.lower(obra)
    for index in listaAOPT:
        if obra == index[1]:
            return index[0]

def consultaQuantObras(artista):

    cont = 0
    artista = str.lower(artista)
    for index in listaAOPT:
        if artista == index[0]:
            cont += 1

    return cont

def consultaTipo(obra):
    obra = str.lower(obra)

    for index in listaAOPT:
        if obra == index[1]:
            return index[3]