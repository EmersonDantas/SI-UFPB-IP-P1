num = int(input('Digite um número:\n'))
centena = num//100
dezena = (num%100)//10
unidade = (num%100)%10
if centena > 1:
    ncentena = 'centenas'
    print('{} {}'.format(centena,ncentena))
else:
    ncentena = 'centena'
    print('{} {}'.format(centena,ncentena))
if dezena > 1:
    ndezena = 'dezenas'
    print('{} {}'.format(dezena,ndezena))
else:
    ndezena = 'dezena'
    print('{} {}'.format(dezena,ndezena))
if unidade > 1:
    nunidade = 'unidades'
    print('{} {}'.format(unidade,nunidade))
else:
    nunidade = 'unidade'
    print('{} {}'.format(unidade,nunidade))
