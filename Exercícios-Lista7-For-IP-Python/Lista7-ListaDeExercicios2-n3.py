num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
quantiNumM4 = 0
if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux
for a in range(num1,num2):
    if a % 4 == 0 and a > num1 and a < num2:
        quantiNumM4 += 1
print('{0} múltiplos.'.format(quantiNumM4))