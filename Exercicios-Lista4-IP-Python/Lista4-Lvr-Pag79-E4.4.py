#EMERSON DANTAS S.I IP-P1
salario = float(input('Digite seu salário atual:'))
aumento_superior = 0.1
aumento_basico = 0.15
if salario > 1250:
    aumento = (salario*aumento_superior)
else:
    aumento = (salario*aumento_basico)
print('Seu almento foi de R${a:.2f}.'.format(a=aumento))