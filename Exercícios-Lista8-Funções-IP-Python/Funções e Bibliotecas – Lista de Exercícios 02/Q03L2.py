
listaAdd = []
listaTemp =[]
perguntas = ['Digite o nome do artista:\n','Digite o nome da obra:\n','Digite o preço da obra:\n','Digite o tipo de obra:\n']
quadro = 0
escultura = 0
for i in range(50):
    for n in range(len(perguntas)):
        entrada = input(perguntas[n])
        listaTemp.append(entrada)

    if listaTemp[-1] == 'quadro':
        quadro += 1

    elif listaTemp[-1] == 'escultura':
        escultura += 1

    listaAdd.append(listaTemp)
    listaTemp = []
if quadro > escultura:
    res = 'mais quadros que esculturas.'

elif quadro == escultura:
    res = 'a mesma quantidade de quadros e esculturas.'

else:
    res = 'mais esculturas que quadros.'
print('A galeria possui {}'.format(res))