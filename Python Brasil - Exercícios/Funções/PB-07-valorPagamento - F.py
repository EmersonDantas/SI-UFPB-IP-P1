def valorPagamento(valor,dias):
    if dias == 0:
        return valor
    else:
        return ((valor * 0.03) + (dias * 0.01)* valor) + valor

valor = 1
cont = 0
soma = 0
while valor != 0:
    valor = float(input('Digite o valor da prestação:\n'))
    dias = int(input('Digite os dias de atrazo no pagamento:\n'))
    print('Valor a ser pago: R${:.2f}'.format(valorPagamento(valor,dias)))
    cont += 1
    soma += valorPagamento(valor,dias)
    
print('Total de pagamentos: {}\n'
      'Total arrecadado: R${:.2f}'.format(cont,soma))
