maior = 0
menor = 10000
totaltemp = 0
cont = 0
continuar = 's'
while continuar == 'sim' or continuar == 's':
    temp = float(input('Digite uma temperatura:\n'))
    continuar = str.lower(input('Deseja continuar? Sim ou Não:'))
    cont += 1
    #Maior
    if temp > maior:
        maior = temp
    #Menor
    if temp < menor:
        menor = temp
    totaltemp += temp
media = totaltemp / cont
print('Maior temperatura: {}º\nMenor temperatura: {}º\n'
      'Média das temperaturas {:.0f}º'.format(maior,menor,media))
