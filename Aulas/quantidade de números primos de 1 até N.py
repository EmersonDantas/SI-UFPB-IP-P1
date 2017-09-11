numero = int(input('Digite um número:\n'))
cont = 0
primo = 0
for a in range(1,numero+1):
    for b in range(1,a+1):
        if a % b == 0:
            cont += 1
    if cont == 2:
        primo += 1
    cont = 0
print(primo)
