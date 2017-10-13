numero = [ ]
for i in range(5):
    numero.append(i * 2)
    print(numero)
numero.insert(3,9)
print(numero)
numero.append(numero.index(4))
print(numero)
del numero[2]
print(numero)
x = len(numero) + 5
numero.append(x)
print(numero)
numero.sort()
print(numero)
numero.remove(2)
print(numero)