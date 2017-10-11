n = int(input('Digite um número:\n'))
def funcao01(n):
    for i in range(1,n+1):
        for a in range(1,i+1):
            print(a,end='')
        print()
funcao01(n)
