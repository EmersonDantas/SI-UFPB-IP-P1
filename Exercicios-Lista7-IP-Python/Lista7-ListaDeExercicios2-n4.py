itens = 1
contMarfim = 0
contBranco = 0
contBrastemp = 0
contElectrolux = 0
quantiMoveis = 0
quantiEletros = 0
quantiDeco = 0
contMoveis = 0
contEletro = 0
contDeco = 0
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
        else:
            print('Cor inválida!')
            exit()
        totalMarfim = (contMarfim / contMoveis) * 100
        totalBranco = (contBranco / contMoveis) * 100
    elif tipodeProduto == 'eletrodoméstico':
        contEletro += 1
        marca = str.lower(input('Marca:\n'))
        if marca == 'brastemp':
            contBrastemp += 1
        elif marca == 'electrolux':
            contElectrolux += 1
        else:
            print('Marca inválida!')
            exit()
        totalElectrolux = (contElectrolux / contEletro) * 100
        totalBrastemp = (contBrastemp / contEletro) * 100
    elif tipodeProduto == 'decoração':
        contDeco += 1
        descricao = str(input('Descrição:\n'))
        preco = float(input('Preço:\n'))
        totalPreco += preco
    else:
        print('Entrada inválida!')
        exit()
if contMoveis > 0 and contEletro == 0 and contDeco == 0:
    print('Percentuais: {m:.2f}% Marfim, {b:.2f}% Branco'.format(m = totalMarfim, b = totalBranco))
    print('Nenhum eletrodoméstico vendido\n'
        'Nenhum objeto de decoração vendido')
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
        print('Nenhum móvel foi vendido'
            'Nenhum eletrodoméstico vendido')
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