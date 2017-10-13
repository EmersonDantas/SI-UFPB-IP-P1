recife = 'recife'
natal = 'natal'
fortaleza = 'fortaleza'
diurno = 'diurno'
noturno = 'noturno'

def validaDadosVoo(destino,turno):
    destino = str.lower(destino)
    turno = str.lower(turno)
    if destino == recife and turno == diurno or turno == noturno:
        return True
    elif destino == natal and turno == diurno:
        return True
    elif destino == fortaleza and turno == noturno:
        return True
    else:
        return False

def calculaValorVoo(destino,turno):
    destino = str.lower(destino)
    turno = str.lower(turno)
    if destino == recife:
        if turno == diurno:
            preco = 100
        elif turno == noturno:
            preco = 90

    elif destino == natal:
            preco = 80

    elif destino == fortaleza:
            preco = 180
    return preco