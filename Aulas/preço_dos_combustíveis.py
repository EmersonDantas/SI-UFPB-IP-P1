pgasolina=2.78
petanol=2.29
pdiesel=2.23
tipo = str.lower(input('Diga o tipo de combustível:'))
quantcomb = float(input('Quantos litros do combustível:'))
if tipo=='gasolina':
    preco = pgasolina*quantcomb
elif tipo=='etanol':
    preco = petanol*quantcomb
elif tipo=='diesel':
    preco = pdiesel*quantcomb
else:
    print('Combustivel inválido!')
    exit()
if quantcomb>=30:
    PROMO='Parabéns! Você ganhou uma troca de óleo gratis!'
else: PROMO='Você não ganhou a troca de óleo gratis. :('

print('Total a pagar: %.2f. %s'%(preco,PROMO))
