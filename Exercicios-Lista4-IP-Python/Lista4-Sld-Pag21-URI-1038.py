#EMERSON DANTAS S.I IP-P1
tipo = int(input('Digite, de acordo com o cardápio, qual o código da refeição que você quer:\nCardapio:\n1 - cachorro quente;\n2 - x-salada;\n3 - x-bacon;\n4 - torrada simples;\n5 - refrigerante.\nDigite aqui:'))
quantidade = int(input('Digite a quantidade:'))
if tipo == 1:
    preco = (quantidade*4)
elif tipo == 2:
    preco = (quantidade*4.50)
elif tipo == 3:
    preco = (quantidade*5)
elif tipo == 4:
    preco = (quantidade*2)
elif tipo == 5:
    preco = (quantidade*1.5)
else:
    print('Refeição inválida!')
    exit()
print('Total: R$ {p:.2f}'.format(p=preco))