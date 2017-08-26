divida = float(input('Digite qual a sua dívida: '))
taxa = float(input('Digite os juros: '))
pagamento = float(input('Digite o pagamento mensal: '))
mes = 0
jurosmen = divida * (taxa/100)
if jurosmen > pagamento:
    print('Sua dívida nunca será paga, o valor mensal pago é menor que os juros!.')
else:
    saldo = divida
    jurosP = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = (saldo + juros) - pagamento
        jurosP += juros
        mes = mes + 1
        print('O valor da sua dívida no {m}º mês é de R${s:.2f}' .format(m=mes, s=saldo))
print ('Para que você possa pagar sua dívida de R${d:.2f}, a {t:.2f} % de juros mensais,\n'
        'você precisará de {m} meses, pagando um total de R${j:.2f} de juros no total.\n'
        'No último mês, você teria um saldo restante a pagar de R${s:.2f}.'
       .format (s=saldo, d=divida, t=taxa, j=jurosP, m=mes))