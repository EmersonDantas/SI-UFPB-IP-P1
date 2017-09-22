import bibliotecaLista2

entrada = str.lower(input('Oque deseja fazer?\n'
                          '\n'
                          'A) Procurar um artista;\n'
                          'B) Quantidade de obras de um artista;\n'
                          'C) Obter o preço de uma obra;\n'
                          'D) Obter o tipo de uma obra.\n'
                          '\n'
                          '===>'))

if entrada == 'a': #Procurar um artista

    obra = str.lower(input('Digite o nome da obra:\n'))
    resultado = bibliotecaLista2.consultaArtista(obra)

elif entrada == 'b': #Saber quantas obras um dado artista tem

    artista = str.lower(input('Digite o nome do artista:\n'))
    resultado = bibliotecaLista2.consultaQuantObras(artista)

elif entrada == 'c': #Consulta de preço

    obra = str.lower(input('Digite o nome da obra:\n'))
    resultado = bibliotecaLista2.consultaPreco(obra)

elif entrada == 'd': #Consulta de tipo

    tipo = str.lower(input('Digite o nome da obra:\n'))
    resultado = bibliotecaLista2.consultaTipo(tipo)

else:

    resultado = 'Você digitou um opção incorreta!'

print(resultado)