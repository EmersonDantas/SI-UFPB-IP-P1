from random import randrange

lista = []
valores = [0,0,0,0,0,0]

for i in range(100):
    dado = randrange(1, 7)
    lista.append(dado)
    valores[dado-1] += 1

for a,fance in enumerate(valores):
    print('{} dados de face número {}'.format(face,a+1))
