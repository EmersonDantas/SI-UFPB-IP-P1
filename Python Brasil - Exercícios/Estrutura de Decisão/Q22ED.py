num = int(input('Digite um número:'))
if num % 2 == 0:
    res = 'par'
else:
    res = 'impar'
print('{} é {}'.format(num,res))
