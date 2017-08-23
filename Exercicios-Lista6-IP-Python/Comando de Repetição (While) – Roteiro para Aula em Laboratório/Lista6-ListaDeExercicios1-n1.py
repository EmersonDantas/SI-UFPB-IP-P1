num1 = int(input('Digite um número:'))
cont = 1
while cont < 2:
    num2 = int(input('Digite um número:'))
    cont += 1
res = num1 + num2
print('A soma de {num1} + {num2} foi igual a {res}'.format(num1=num1,num2=num2,res=res))