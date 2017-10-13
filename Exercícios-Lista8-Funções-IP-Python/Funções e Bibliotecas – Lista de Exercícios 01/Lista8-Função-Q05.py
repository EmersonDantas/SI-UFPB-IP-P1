import bibliotecaLista1
quantiM4 = 0
somaD = 0
for i in range(2):
    num = int(input('Digite um número:\n'))

    if bibliotecaLista1.testaMultiplo4(num):
        quantiM4 += 1
    if bibliotecaLista1.testaDivisor(300, num):
        somaD += num
print('{} números multiplos de 4\n'
      'A soma dos divisores de 300: {}'.format(quantiM4,somaD))