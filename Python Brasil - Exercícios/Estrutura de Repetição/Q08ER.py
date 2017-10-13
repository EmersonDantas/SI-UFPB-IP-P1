soma = 0
for i in range(5):
    numero = float(input('Digite um número:\n'))
    soma += numero
media = soma / 5
print('A média dos números digitados é: {:.2f}'.format(media))
