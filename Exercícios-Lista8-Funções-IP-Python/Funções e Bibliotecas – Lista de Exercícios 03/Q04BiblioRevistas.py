#revistas = [[editora,titulo,preco,quantivendidas]]
def pesquisaEditora(titulo,revistas):
    titulo = str.lower(titulo)
    for index in range(len(revistas)):
        if titulo == revistas[i][1]:
            return revistas[0]

def pesquisaQuantVendas(titulo,revistas):
    titulo = str.lower(titulo)
    quantivendas = 0
    for livro in revistas:
        for dadoslivro in range(len(livro)):
            if livro[dadoslivro] == titulo:
                quantivendas += livro[3]

    return quantivendas

def pesquisaValor(titulo,revistas):
    titulo = str.lower(titulo)
    for index in revistas:
        if index[1] == titulo:
            return index[0]
