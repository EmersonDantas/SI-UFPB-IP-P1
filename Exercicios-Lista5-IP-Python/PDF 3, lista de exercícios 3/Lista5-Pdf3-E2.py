#EMERSON DANTAS S.I IP-P1
pgasolina = 2.53
petanol = 2.09
pdiesel = 1.92
tipo = str.lower(input('Diga o tipo de combustível:'))
quantmoney = float(input('Quantos reais de {tipo} deseja:'.format(tipo=tipo)))
if tipo == 'gasolina':
    quantcomb = quantmoney / pgasolina
    promo = 'Não ganhou uma troca de óleo gratis!'
elif tipo == 'etanol':
    quantcomb = quantmoney / petanol
    if quantcomb >= 30:
        promo = 'Ganhou uma troca de óleo gratis!'
    else:
       promo = 'Não ganhou uma troca de óleo gratis!'
elif tipo == 'diesel':
    quantcomb = quantmoney / pdiesel
    promo = 'Não ganhou uma troca de óleo gratis!'
else:
    print('Combustivel inválido!')
    exit()
print('Total litros: {lt:.2f}l\n{pr}'.format(lt=quantcomb, pr=promo))