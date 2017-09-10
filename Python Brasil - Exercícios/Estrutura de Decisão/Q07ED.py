num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))
num3 = float(input('Digite o terceiro número:\n'))
#Maior
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3
#Menor
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3
print('O maior número é {}\n'
      'O menor número é {}'.format(maior,menor))
