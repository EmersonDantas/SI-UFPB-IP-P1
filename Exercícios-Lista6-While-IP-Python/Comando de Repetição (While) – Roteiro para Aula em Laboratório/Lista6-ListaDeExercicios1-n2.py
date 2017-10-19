num1 = int(input('Digite um número:'))
cont = 1
while cont < 2:
    num2 = int(input('Digite um número:'))
    cont += 1
res1 = num1 + num2
res2 = num1 * num2
print('A soma de {num1} + {num2} foi igual a {res1}\nO produto de {num1} * {num2} foi igual a {res2}'.format(num1=num1,num2=num2,res1=res1,res2=res2))