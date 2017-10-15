#EMERSON DANTAS S.I IP-P1
Preco_mercadoria=float(input('Digite o preço:'))
Desconto_p=float(input('Digite o percentual de desconto:'))
Desconto_v=(Preco_mercadoria*Desconto_p/100)
Novo_preco_m=(Preco_mercadoria-Desconto_v)
print('Seu desconto foi de R$%2.2f, o novo preço é R$%2.2f'%(Desconto_v, Novo_preco_m))