
listaAdd = []
listaTemp =[]
perguntas = ['Digite o nome do artista:\n','Digite o nome da obra:\n','Digite o preço da obra:\n','Digite o tipo de obra:\n']
quadro = 0
escultura = 0
for i in range(50):
    for n in range(len(perguntas)):
        if n!= [2]:
            entrada = str(input(perguntas[n]))
        else:
            entrada = float(input(perguntas[n]))
        listaTemp.append(entrada)

    if str.lower(listaTemp[3]) == 'quadro':
        quadro += 1

    elif str.lower(listaTemp[3]) == 'escultura':
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