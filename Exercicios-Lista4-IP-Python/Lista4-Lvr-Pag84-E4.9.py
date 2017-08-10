#EMERSON DANTAS S.I IP-P1
valor_casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite seu salário:'))
parcela_anos = int(input('Por quantos anos deseja pagar:'))
limitepm = salario*0.30
parcela_a_pagar = valor_casa/(parcela_anos*12)
if parcela_a_pagar < limitepm:
    print('Emprestimo aprovado! Você pagara R${valor:.2f} por {meses} meses.'.format(valor=parcela_a_pagar,meses=(parcela_anos*12)))
else:
    print('Emprestimo negado!')