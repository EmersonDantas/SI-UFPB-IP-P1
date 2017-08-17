'''correção retirando else da linha 4 e acrescentando elif na linha 5(do pdf).'''
altura = float (input())
if (altura <= 1.40):
    print("Estatura Baixa")
elif (altura < 1.65):
    print("Estatura Mediana")
else:
    print("Estatura Alta")