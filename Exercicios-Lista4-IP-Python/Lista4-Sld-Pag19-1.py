#EMERSON DANTAS S.I IP-P1
salario = float(input('Digite seu salário atual:'))
imposto_1000 = 0.17
imposto_geral = 0.06
if salario >= 1000:
    imposto_a_pagar = (salario*imposto_1000)
else:
    imposto_a_pagar = (salario*imposto_geral)
print('Você deverá pagar R${imp:.2f} de impostos.'.format(imp=imposto_a_pagar))