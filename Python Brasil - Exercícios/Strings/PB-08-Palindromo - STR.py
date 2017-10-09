nome = str.lower(input('Digite a palavra:\n'))
nome = nome.replace(' ','')
if nome == nome[::-1]:
    print('É um Palíndromo.')
else:
    print('Não é um palíndromo.')
