fibonacci = int(input('Qual nº:'))
ultimo = 0
penultimo = 1
for a in range (fibonacci):
    penultimo += ultimo
    ultimo = penultimo - ultimo
    print(ultimo)
