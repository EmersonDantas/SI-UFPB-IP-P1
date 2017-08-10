#EMERSON DANTAS S.I IP-P1
num1 = float(input('Digite um núemro:'))
operador  = str(input('Digite qual operação você quer?:\n+ ,- ,* , / :'))
num2 = float(input('Digite outro número:'))
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
else:
    print('operador inválido')
print('O resultado da operação realizada foi: {r}'.format(r=resultado))