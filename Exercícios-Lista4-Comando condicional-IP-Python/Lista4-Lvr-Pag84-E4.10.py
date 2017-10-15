# EMERSON DANTAS S.I IP-P1
consumo = float(input('Digite o consumo de energia em kWh:'))
tipo = str.lower(input('Digite o tipo de instalação conforme a tabela abaixo:\nR para Residências;\nI para indústrias\nC para comércios.\n'))
if tipo == 'r':
    if consumo > 500:
        preco = 0.65
    else:
        preco = 0.40
elif tipo == 'i':
    if consumo > 5000:
        preco = 0.60
    else:
        preco = 0.55
elif tipo == 'c':
    if consumo > 1000:
        preco = 0.60
    else:
        preco = 0.55
else:
    print('Tipo de instalação inválido!')
    exit()
print('Você deverá pagar R${r:.2f}'.format(r=(consumo * preco)))