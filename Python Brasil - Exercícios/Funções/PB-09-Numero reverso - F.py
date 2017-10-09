def funcao09(n):
    if n.isdigit():
        return n[::-1]

n = str(input('Digite um número inteiro:\n'))
print(funcao09(n))
