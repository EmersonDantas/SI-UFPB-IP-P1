pacote = 'pacote'
documento = 'documento'
pequena = 'pequena'
media = 'media'
grande = 'grande'
normal = 'normal'
sedex = 'sedex'
sedex10 = 'sedex10'

def validaTipoItem(item):
    item = str.lower(item)
    if item == pacote or item == documento:
        return True
    else:
        return False

def validaPeso(peso):
    if peso >= 0:
        return True
    else:
        return False

def convertePeso(peso): #Variavel peso é em Kilos
    gramas = peso * 1000
    return gramas

def calculaCustoItem(gramas, item):

    if item == pacote:
        precoItem = gramas * 0.003
    else:
        precoItem = gramas * 0.002
    return precoItem

def validaEmbalagem(embalagem):
    embalagem = str.lower(embalagem)
    if embalagem == pequena or embalagem == media or embalagem == grande:
        return True
    else:
        return False

def calculaCustoEmbalagem(embalagem):

    if embalagem == pequena:
        precoEmbalagem = 4

    elif embalagem == media or embalagem == 'média':
        precoEmbalagem = 7

    else:
        preco = 10
    return precoEmbalagem

def validaEntrega(entrega):
    entrega = str.lower(entrega)
    if entrega == normal or entrega == sedex or entrega == sedex10:
        return True
    else:
        return False

def calculaCustoEntrega(entrega):
    if entrega == sedex:
        precoEntrega = 5
    elif entrega == sedex10:
        precoEntrega = 8
    else:
        precoEntrega = 0
    return precoEntrega
