n = int(input('Digite um número:\n'))
def funcao01(n):
    for i in range(1,n+1):
        for a in range(1,i):
            print(a)
    return(i)
print(funcao01(n))
