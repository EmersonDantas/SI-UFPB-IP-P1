quantiLas = 0
preco = 0
pessoas = 50
precoTotal = 0
numpedido = 0
for total in range(pessoas):
    tCobranca = str.lower(input('De que forma você prefere pagar, por peça ou peso: \n'))
    if tCobranca == 'peça':
        quantiPecas = int(input('Quantas peças: \n'))
        preco = quantiPecas * 7
    elif tCobranca == 'peso':
        quantiQuilos = int(input('Quantos quilos: \n'))
        preco = quantiQuilos * 5
    else:
        print('Forma inválida!')
        break
    lavagemASeco = str.lower(input('Deseja lavar a seco? \n'))
    if lavagemASeco == 'sim':
        preco += 3.50
        quantiLas += 1
    else:
        print('Sem lavagem a seco...\n')
    precoTotal += preco
    numpedido += 1
    print('Valor do {ped}º pedido R${p:.2f}\n'
          'A lavanderia arrecadou R${tl:.2f}\n'
          '{las} pessoas solicitaram lavagem a seco.\n\n'.format(p = preco, tl = precoTotal, las = quantiLas, ped = numpedido))
print('### A lavanderia arrecadou R${tl:.2f}\n'
    '{las} pessoa(s) solicitaram(ou) lavagem a seco. ###'.format(tl = precoTotal, las = quantiLas))
