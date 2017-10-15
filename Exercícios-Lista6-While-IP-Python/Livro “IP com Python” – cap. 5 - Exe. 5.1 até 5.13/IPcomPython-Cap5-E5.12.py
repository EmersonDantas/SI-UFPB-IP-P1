deposito = float(input('Digite o valor em R$ a ser depositado:'))
taxaIn = float(input('Digite a taxa de juros:'))
depositoMensal = float(input('Diga o valor a res depositado mensalmente :'))
mes = 1
taxa = taxaIn/100
valor = deposito
while mes <= 24:
    valor = valor + (valor * taxa) + depositoMensal
    print('Ganhos com juros na poupaça no {m}º mês: R${r:.2f}'.format(m=mes, r=valor))
    mes += 1
print('O ganho total com juros foi de R${0:.2f}'.format(valor - deposito))