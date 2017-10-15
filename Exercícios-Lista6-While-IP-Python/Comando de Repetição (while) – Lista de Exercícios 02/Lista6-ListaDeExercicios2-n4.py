soma = 0
aux = 0
numero = 0
while numero != 100:
    numero = int(input('Digite um número:'))
    if numero % 2 == 0 and numero != 100:
        aux += 1
        soma += numero
if aux >= 1:
    media = soma // aux
    print('Média da soma dos números pares: {m3}'.format(m3=media))
elif aux == 0:
    print('Não foram lidos números pares!')
