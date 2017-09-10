tamanho = int(input('Qual o tamanho da área a ser pintada, em metros quadrados: '))
litros = tamanho // 6

#Latas
quantilatas = litros//18
resto = litros % 18
if resto > 0:
    quantilatas += 1


#Galões
quantigaloes = litros//3.6 
resto = litros % 3.6
if resto > 0:
    quantigaloes += 1


#Mesclado
quantigaloesmix = 0
litros = (tamanho // 6) * 1.1
quantilatasmix = litros // 18
resto = litros % 18

if resto > 0:
    quantilatasmix += 1
    temp = resto // 3.6
    if temp > 0:
        quantigaloesmix += 1
    
print('Você deverá comprar {0:.0f} lata(s), pagando R${1:.2f}\nOu\n'.format(quantilatas, quantilatas*80))
print('Você deverá comprar {0:.0f} galão(ões), pagando R${1:.2f}\nOu\n'.format(quantigaloes, quantigaloes*25))
print('Você deverá comprar {0:.0f} lata(s) e {1:.0f} galão(ões), pagando R${2:.2f}'.format(quantilatasmix, quantigaloesmix, (quantilatasmix*80) + (quantigaloesmix*25)))
