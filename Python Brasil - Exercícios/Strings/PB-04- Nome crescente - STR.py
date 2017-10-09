entrada = str(input('Digite uma string:\n'))
for i in range(len(entrada)):
    print(entrada[:i+1:])