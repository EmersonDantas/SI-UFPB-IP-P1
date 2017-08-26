aux = 'sim'
while aux == 'sim':
    cont = 1
    num1 = int(input('Digite um número:'))
    while cont < 2:
        aux = 'não'
        cont += 1
        num2 = int(input('Digite um número:'))
        if num1 > 0 and num2 > 0:
            res1 = num1 + num2
            res2 = num1 * num2
            print('A soma de {num1} + {num2} foi igual a {res1}\nO produto de {num1} * {num2} foi igual a {res2}'.format(
                num1=num1, num2=num2, res1=res1, res2=res2))
        else:
            res = (num1 + num2) // cont
            print('A média inteira é igual a {0}'.format(res))
    ne = str.lower(input('Gostaria de fazer uma nova execução: SIM ou NÃO?'))
    if ne == 'sim':
        aux = 'sim'
    elif ne == 'não':
        aux = 'não'
    else:
        print('Comando inválido!')