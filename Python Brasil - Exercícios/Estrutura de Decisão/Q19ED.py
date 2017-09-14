num = int(input('Digite um número:\n'))
centena = num//100
dezena = (num%100)//10
unidade = (num%100)%10
if centena > 1:
    ncentena = 'centenas'
else:
    ncentena = 'centena'
if dezena > 1:
    ndezena = 'dezenas'
else:
    ndezena = 'dezena'
if unidade > 1:
    nunidade = 'unidades'
else:
    nunidade = 'unidade'
if centena > 0:
    print('{} {}'.format(centena,ncentena))
if dezena > 0:
    print('{} {}'.format(dezena,ndezena))
if unidade > 0:
    print('{} {}'.format(unidade,nunidade))
