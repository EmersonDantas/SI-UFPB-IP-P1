num = int(input("Digite um número para obter a tabuada:"))
cont = 1
while cont <= 10:
    res = num*cont
    print('{0} x {1} = {2}'.format(num, cont, res))
    cont += 1