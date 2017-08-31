itens = int(input('Quantidade de itens:\n'))
contMarfim, contBranco = 0 , 0
contBrastemp, contElectrolux = 0, 0
quantiMoveis, quantiEletros, quantiDeco = 0, 0, 0
contMoveis, contEletro, contDeco = 0, 0, 0
totalPreco = 0
for a in range(itens):
    tipodeProduto = str.lower(input('Tipo de produto:\n'))
    if tipodeProduto == 'móvel':
        contMoveis += 1
        cor = str.lower(input('Cor:\n'))
        if cor == 'marfim':
            contMarfim += 1
        elif cor == 'branco':
            contBranco += 1
        totalMarfim = (contMarfim / contMoveis) * 100
        totalBranco = (contBranco / contMoveis) * 100
    elif tipodeProduto == 'eletrodoméstico':
        contEletro += 1
        marca = str.lower(input('Marca:\n'))
        if marca == 'brastemp':
            contBrastemp += 1
        elif marca == 'electrolux':
            contElectrolux += 1
        totalElectrolux = (contElectrolux / contEletro) * 100
        totalBrastemp = (contBrastemp / contEletro) * 100
    elif tipodeProduto == 'decoração':
        contDeco += 1
        descricao = str(input('Descrição:\n'))
        preco = float(input('Preço:\n'))
        totalPreco += preco
if contMoveis > 0 and contEletro == 0 and contDeco == 0:
    print('Percentuais: {m:.2f}% Marfim, {b:.2f}% Branco'.format(m = totalMarfim, b = totalBranco))
    print('Nenhum eletrodoméstico vendido\nNenhum objeto de decoração vendido')
elif contEletro > 0 and contDeco == 0 and contMoveis == 0:
    if contBrastemp > contElectrolux or contElectrolux > contBrastemp:
        print('Percentuais: {e:.2f}% Electrolux {b:.2f}% Brastemp'.format(e = totalElectrolux, b = totalBrastemp))
    elif contBrastemp == contEletro:
        print('As duas marcas foram igualmente vendidas')
elif contDeco > 0 and contMoveis == 0 and contEletro == 0:
    if contDeco == 1:
        print('Foi vendido somente 1 decoração: {d}\nPreço = R${p:.2f}'.format(d = descricao, p = preco))
    else:
        print('Preço médio de decoração: R${d:.2f}'.format(d = totalPreco / contDeco))
        print('Nenhum móvel foi vendido\nNenhum eletrodoméstico vendido')
elif contMoveis > 0 and contEletro > 0 and contDeco == 0:
    print('Percentuais: {m:.2f}% Marfim, {b:.2f}% Branco'.format(m=totalMarfim, b=totalBranco))
    print('Percentuais: {e:.2f}% Electrolux {b:.2f}% Brastemp'.format(e=totalElectrolux, b=totalBrastemp))
elif contMoveis == 0 and contEletro > 0 and contDeco > 0:
    print('Percentuais: {e:.2f}% Electrolux {b:.2f}% Brastemp'.format(e=totalElectrolux, b=totalBrastemp))
    print('Preço médio de decoração: R${d:.2f}'.format(d = totalPreco / contDeco))
elif contMoveis > 0 and contDeco > 0 and contEletro == 0:
    print('Percentuais: {m:.2f}% Marfim, {b:.2f}% Branco'.format(m=totalMarfim, b=totalBranco))
    print('Preço médio de decoração: R${d:.2f}'.format(d=totalPreco / contDeco))
else:
    print('Percentuais: {m:.2f}% Marfim, {b:.2f}% Branco'.format(m=totalMarfim, b=totalBranco))
    if contElectrolux == contBrastemp:
        print('As duas marcas foram igualmente vendidas')
    else:
        print('Percentuais: {e:.2f}% Electrolux {b:.2f}% Brastemp'.format(e=totalElectrolux, b=totalBrastemp))
    print('Preço médio de decoração: R${d:.2f}'.format(d=totalPreco / contDeco))