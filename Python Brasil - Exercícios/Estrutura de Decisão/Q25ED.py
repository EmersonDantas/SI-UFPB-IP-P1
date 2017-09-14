lp = ['Telefonou para a vítima?','Esteve no local do crime?',
      'Mora perto da vítima?','Devia para a vítima?',
      'Já trabalhou com a vítima?']

positivo = 0

for pergunta in range(len(lp)):
    pv = str.lower(input(lp[pergunta]+' Sim ou Não:'))
    if pv == 'sim' or pv == 's':
        positivo += 1
        
if positivo == 2:
    pessoa = 'suspeito'
    
elif positivo == 3 or positivo == 4:
    pessoa = 'cúmplice'
    
elif positivo == 5:
    pessoa = 'assassino'
    
else:
    pessoa = 'inocente'
    
print('Essa pessoa é {}.'.format(pessoa))
