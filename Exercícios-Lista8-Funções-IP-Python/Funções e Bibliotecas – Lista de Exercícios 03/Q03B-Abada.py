import Q03AbiblioAbada

totalVendidos = 0
for i in range(100):

    quantidade = int(input('Digite a quantidade de abadás vendidos:\n'))
    totalVendidos += quantidade
    comissao = Q03AbiblioAbada.calculaComissao(quantidade)
    bonus = Q03AbiblioAbada.calculaBonus(quantidade)
    print('Sua comissão é R${:.2f};\nSeu bônus é R${:.2f}.'.format(comissao,bonus))
     
print('Quantidade de abadás vendidos: {}'.format(totalVendidos))
