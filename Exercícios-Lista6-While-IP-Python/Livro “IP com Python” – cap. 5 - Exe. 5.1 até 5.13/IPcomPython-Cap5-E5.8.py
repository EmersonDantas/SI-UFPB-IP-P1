num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
cont = 0
res = 0
while cont < num2:
    res += num1
    cont += 1
print('{0} x {1} = {2}'.format(num1, cont, res))