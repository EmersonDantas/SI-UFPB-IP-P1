'''nome = 'kkk eae men'
lista = list(nome)
print('#'.join(lista))'''

N = int(input())
for i in range(N):
    soma = 0
    V = (input())
    for a in range(len(V)):
        if V[a] == '1':
            soma += 2

        elif V[a] == '2' or V[a] == '3' or V[a] == '5':
            soma += 5

        elif V[a] == '4':
            soma += 4

        elif V[a] == '6' or V[a] == '9' or V[a] == '0':
            soma += 6

        elif V[a] == '7':
            soma += 3

        elif V[a] == '8':
            soma += 7

    print(soma,' leds')
