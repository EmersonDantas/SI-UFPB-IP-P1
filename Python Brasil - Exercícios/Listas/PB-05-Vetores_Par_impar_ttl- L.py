lista = []
listaPar = []
listaImpar = []
for i in range(5):
    num = int(input('Digite um número inteiro:\n'))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)

    else:
        listaImpar.append(num)

print('Lista dos números: {}\n'
      'Lista dos pares: {} \n'
      'Lista dos impares: {}'
      .format(lista,listaPar,listaImpar))
        
