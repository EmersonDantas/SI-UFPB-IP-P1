fatorial1 = int(input('Digite um número para fatorar:'))
res = 1
for i in range(fatorial1,1,-1):
    res *= i
print('{f}! = {r}'.format(r=res,f=fatorial1))
