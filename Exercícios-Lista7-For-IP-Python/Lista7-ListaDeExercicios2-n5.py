pessoas = 500
opexe, opbom, opreg, opruim = 0, 0, 0, 0
bomIdadeTot = 0
maisIdosa = 0
quantiIdadeM30Ex = 0
medIdadeBom = 0
for filme in range(pessoas):
    idade = int(input('Qual a sua idade:\n'))
    opniao = str.lower(input('Qual a sua opnião sobre o filme; exelente, bom, regular ou ruin:\n'))
    if idade > maisIdosa:
        maisIdosa = idade
    if opniao == 'exelente':
        opexe += 1
        if idade > 30:
            quantiIdadeM30Ex += 1
    elif opniao == 'bom':
        opbom += 1
        bomIdadeTot += idade
        medIdadeBom = bomIdadeTot / opbom
    elif opniao == 'regular':
        opreg += 1
    elif opniao == 'ruim':
        opruim += 1
print('Média de idade Bom -> {mib:.0f}\n'
      'Quantidade respostas Ruim/Regular -> {qrrr}\n'
      'Pessoas acima de 30 Exelente -> {pa30e}\n'
      'Maior idade -> {mi}'
      .format(mib=medIdadeBom, qrrr=opreg + opruim, pa30e=quantiIdadeM30Ex, mi=maisIdosa))