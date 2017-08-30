num1 = int(input('Digite o primeiro número: '))#20
num2 = int(input('Digite o segundo número: '))#4
quantiNumM4 = 0
if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux
for a in range(num1,num2):
    if a % 4 == 0:
        quantiNumM4 += 1
print('{0} múltiplos.'.format(quantiNumM4))