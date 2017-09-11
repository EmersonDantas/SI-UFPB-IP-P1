salario = float(input('Digite seu salário:\n'))
if salario <= 280:
    aumento = salario * 0.2
    p = 20
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    p = 15
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    p = 10
else:
    aumento = salario * 0.05
    p = 5
print('Salário antigo: R${:.2f}\n'
      'Você recebeu um aumento de {:.2f}%, totalizando R${:.2f}\n'
      'Seu novo salario é R${}'.format(salario,p,aumento,salario+aumento))
