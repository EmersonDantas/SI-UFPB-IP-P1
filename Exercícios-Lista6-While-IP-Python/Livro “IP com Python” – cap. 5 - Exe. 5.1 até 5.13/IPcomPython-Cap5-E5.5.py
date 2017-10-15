num = int(input('Digite um número:'))
cont = 1
aux = 0
while cont <= num:
    cont += 1
    if cont % 3 == 0 and aux != 10:
        aux += 1
        print(cont)