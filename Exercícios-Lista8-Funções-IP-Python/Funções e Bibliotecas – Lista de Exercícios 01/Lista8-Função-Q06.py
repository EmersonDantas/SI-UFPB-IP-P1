import bibliotecaLista1

maiorNum = -9**999
for i in range (2):
    num1 = float(input('Digite o primeiro número:\n'))
    num2 = float(input('Digite o segundo número:\n'))
    maior = bibliotecaLista1.calculaMaior(num1, num2)
    if maior > maiorNum:
        maiorNum = maior
print(maiorNum)