num = int(input('Digite um número para fatorar:'))
res = 1
for i in range(num,1,-1):
    res *= i
print('{}! = {}'.format(num,res))
