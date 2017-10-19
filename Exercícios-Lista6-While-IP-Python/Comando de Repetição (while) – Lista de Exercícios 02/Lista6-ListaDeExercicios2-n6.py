totalFilhos = 0
cont = 0
quantiFilhos = int(input('Digite quantos filhos você tem:'))
while quantiFilhos >= 0:
    quantiFilhos = int(input('Digite quantos filhos você tem:'))
    totalFilhos += quantiFilhos
    cont += 1
res = totalFilhos // cont
print('A média do número de filhos dos funcionários é {0}'.format(res))