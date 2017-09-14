tamanho = int(input('Qual o tamanho da área a ser pintada, em metros quadrados: '))
litros = tamanho // 6
if litros == 1:
    totallatasA = 1
    totalgaloesA = 1
else:
    totallatasA = litros // 18
    totalgaloesA = litros // 3.6
    litrosfolga = litros * 1.10
    totallatasB = litrosfolga // 18
    resto = litrosfolga % 18
    totalgaloesB = resto // 3.6
print('Total somente com {0:.0f} latas: R${1:.2f}\n'
      'Total somente com {2:.0f} galões: R${3:.2f}, Ou\n'
      '{4:.0f} latas e {5:.0f} galões, totalizando R${6:.2f}.'
      .format(totallatasA,totallatasA*80,totalgaloesA,totalgaloesA*25,
              totallatasB,totalgaloesB,(totallatasB*80) + (totalgaloesB*25)))
    
