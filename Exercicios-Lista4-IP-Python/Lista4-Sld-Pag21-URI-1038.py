#EMERSON DANTAS S.I IP-P1
tipo = str.lower(input('Digite, de acordo com o cardápio, qual refeição você quer:\nCardapio:\ncachorro quente;\nx-salada;\nx-bacon;\ntorrada simples;\nrefrigerante.\nDigite aqui:'))
quantidade = int(input('Digite a quantidade de {tp}:'.format(tp=tipo)))
if tipo == 'cachorro quente':
    preco = (quantidade*4)
elif tipo == 'x-salada':
    preco = (quantidade*4.50)
elif tipo == 'x-bacon':
    preco = (quantidade*5)
elif tipo == 'torrada simples':
    preco = (quantidade*2)
elif tipo == 'refrigerante':
    preco = (quantidade*1.5)
else:
    print('Refeição inválida!')
    exit()
print('Total: R$ {p:.2f}'.format(p=preco))