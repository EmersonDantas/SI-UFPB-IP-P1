import bibliotecaLista2
continuar = 'sim'
listaAOPT = [['leonardo resende','obraLR1',6,'escultura'],['artst1','obra1',1,'quadro'],['artst2','obra2',2,'quadro'],['artst3','obra3',3,'quadro'],['artst4','obra4',4,'quadro'],['leonardo resende','obraLR2',4,'escultura']]
while continuar == 'sim':
    entrada = str.lower(input('Oque deseja fazer?\n'
                              '\n'
                              'A) Procurar um artista;\n'
                              'B) Quantidade de obras de um artista;\n'
                              'C) Obter o preço de uma obra;\n'
                              'D) Obter o tipo de uma obra;\n'
                              '\n'
                              '===>'))

    if entrada == 'a': #Procurar um artista
        obra = str(input('Digite o nome da obra:\n'))
        resultado = ('O(a) artista da obra {} é {}.'.format(obra,bibliotecaLista2.consultaArtista(obra,listaAOPT)))

    elif entrada == 'b': #Saber quantas obras um dado artista tem
        artista = str(input('Digite o nome do artista:\n'))
        resultado = ('O(a) artista {} possui {} obras.'.format(artista,bibliotecaLista2.consultaQuantObras(artista,listaAOPT)))

    elif entrada == 'c': #Consulta de preço
        obra = str(input('Digite o nome da obra:\n'))
        resultado = ('O preço da obra {} é R${:.2f}'.format(obra,bibliotecaLista2.consultaPreco(obra,listaAOPT)))

    elif entrada == 'd': #Consulta de tipo
        tipo = str(input('Digite o nome da obra:\n'))
        resultado = ('{} é um(a) {}.'.format(tipo,bibliotecaLista2.consultaTipo(tipo,listaAOPT)))

    else:
        resultado = 'Você digitou um opção incorreta!'

    print(resultado)
    continuar = str.lower(input('Deseja fazer uma nova consulta? sim ou não:\n'))
