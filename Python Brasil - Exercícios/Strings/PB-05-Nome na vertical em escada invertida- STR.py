nome = str(input('Digite uma string, pode ser seu nome:\n'))
for i in range(len(nome)):
    print(nome[:len(nome)-i:])
