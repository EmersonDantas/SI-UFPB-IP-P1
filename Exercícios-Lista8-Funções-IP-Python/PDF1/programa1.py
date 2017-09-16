import bibliotecaCorreios
precoTotal = 0

item = str(input('Digite o tipo de item:\n'))

if bibliotecaCorreios.validaTipoItem(item):

    peso = float(input('Digite o peso do {}:\n'.format(item)))
    
    if bibliotecaCorreios.validaPeso(peso):
        
        gramas = bibliotecaCorreios.convertePeso(peso)
        precoTotal = bibliotecaCorreios.calculaCustoItem(gramas, item)
        
        print(precoTotal)
    else:
        print('Peso inválido!')
else:
    print('Item inválido!')
