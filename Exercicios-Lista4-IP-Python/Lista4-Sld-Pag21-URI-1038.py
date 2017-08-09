#EMERSON DANTAS S.I IP-P1
idade = int(input('Digite sua idade:'))
if idade <= 5:
    pagar = (10)
elif idade >= 60:
    pagar = (15)
else:
    pagar = (25)
print('Seu ingresso custa R${pg}.'.format(pg=pagar))