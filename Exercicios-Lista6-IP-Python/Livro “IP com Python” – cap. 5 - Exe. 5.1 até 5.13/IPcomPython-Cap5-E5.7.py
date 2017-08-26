num = int(input("Digite um número para obter a tabuada:"))
ini = int(input('Digite um inicio:'))
fim = int(input('Digite um fim:'))
cont = 1
while cont < fim:
    cont += 1
    if cont >= ini:
        res = num*cont
        print('{0} x {1} = {2}'.format(num, cont, res))
