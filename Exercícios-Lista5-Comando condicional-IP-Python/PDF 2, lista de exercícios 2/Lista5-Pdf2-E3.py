#EMERSON DANTAS S.I IP-P1
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
num3 = float(input('Digite o terceiro número:'))
if num1 > num2 and num1 > num3:
    res = num1
elif num2 > num1 and num2 > num3:
    res = num2
else:
    res = num3
print('O maior número é {r}.'.format(r=res))

