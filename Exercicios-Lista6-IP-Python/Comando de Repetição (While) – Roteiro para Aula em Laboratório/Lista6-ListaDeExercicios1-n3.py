cont = 1
num1 = int(input('Digite um número:'))
while cont < 2:
    aux += 1
    cont += 1
    num2 = int(input('Digite um número:'))
    if num1 > 0 and num2 > 0:
        res1 = num1 + num2
        res2 = num1 * num2
        print('A soma de {num1} + {num2} foi igual a {res1}\nO produto de {num1} * {num2} foi igual a {res2}'.format(
            num1=num1, num2=num2, res1=res1, res2=res2))
    else:
        print('Você digitou um número inválido')