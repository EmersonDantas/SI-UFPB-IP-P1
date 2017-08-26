dividendo = int(input('Digite o dividendo:'))
divisor = int(input('Digite o divisor:'))
quociente = 0
cont = dividendo
while cont >= divisor:
    cont -= divisor
    quociente += 1
resto = cont
print('{0} / {1} = \nquociente = {2}\nresto = {3}'.format(dividendo, divisor, quociente, resto))