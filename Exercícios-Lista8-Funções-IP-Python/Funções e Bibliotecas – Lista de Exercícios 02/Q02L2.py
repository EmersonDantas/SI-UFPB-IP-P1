import bibliotecaLista2

for i in range(5):

    artista = str.lower(input('Digite o nome do artista:\n'))
    obra = str.lower(input('Digite o nome da obra de {}:\n'.format(artista)))
    preco = float(input('Digite o preço da obra {}:\n'.format(obra)))
    tipo = str.lower('Digite o tipo de obra:\n')

    bibliotecaLista2.adicionarValores(artista,obra,preco,tipo)

quantidade = bibliotecaLista2.consultaQuantObras(artista)
preco = bibliotecaLista2.consultaPreco(artista)
print(preco)