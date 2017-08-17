plateiaVip = 350 * 1.05
cadeiras = 200 * 1.05
arquibancada = 100 * 1.05
lugar = str.lower(input('Escolha o setor. Platéia Vip, cadeira ou arquibancada:'))
tipo = str.lower(input('Escolha seu ingresso. meia ou inteira:'))
if lugar == 'cadeira' and tipo == 'meia':
    preco = (cadeiras / 2)
elif lugar == 'cadeira' and tipo == 'inteira':
    preco = cadeiras
elif lugar == 'arquibancada' and tipo == 'meia':
    preco = (arquibancada / 2)
elif lugar == 'arquibancada' and tipo == 'inteira':
    preco = arquibancada
elif lugar == 'platéia vip' and tipo == 'inteira':
    preco = plateiaVip
elif lugar == 'platéia vip' and tipo == 'meia':
    print('Tipo de ingresso inválido!')
    exit()
else:
    print('Setor inválido!')
    exit()
print('R${p:.2f}'.format(p=preco))