deposito = float(input('Digite o valor em R$ a ser depositado:'))
taxaIn = float(input('Digite a taxa de juros:'))
mes = 0
taxa = taxaIn/100
valor = deposito
while mes < 24:
    valor = valor + (valor * taxa)
    mes += 1
    print('Ganhos com juros na poupaça no {m}º mês: R${r:.2f}'.format(m=mes, r=valor))
print('O ganho total com juros foi de R${0:.2f}'.format(valor - deposito))