l1 = int(input('Digite o valor do primeiro lado:\n'))
l2 = int(input('Digite o valor do segundo lado:\n'))
l3 = int(input('Digite o valor do terceiro lado:\n'))
if (l1 + l2) > l3 or (l1 + l3) > l2 or (l2 + l3) > l1:
    triangulo = True
else:
    triangulo = False
if triangulo:
    triangulo = 'Os valores informados formam um triangulo'
    if l1 == l2 and l2 == l3:
        tipo = 'Equilátero'
    elif l1 == l2 or l2 == l3 or l3 == l1:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print('{} do tipo {}.'.format(triangulo,tipo))
else:
    print('Os valores informados não formam um triangulo.')

