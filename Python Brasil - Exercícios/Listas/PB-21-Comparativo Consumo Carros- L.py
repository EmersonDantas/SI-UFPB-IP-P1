carrosEconsumo = [['fusca',7],['gol',10],['uno',12.5],['vectra',9],['Peugeout',14.5]]

'''for i in range(5):
    print('Veículo {}'.format(i+1))
    carro = str(input('Digite o modelo do seu carro:\n'))
    consumo = float(input('Digite o consumo do {}:\n'.format(carro)))
    print()
    carrosEconsumo.append([carro,consumo])'''
    
for i,carro in enumerate(carrosEconsumo):
    print('{} - {}     -  {}  -  {:.1f} litros  -  R${:.2f}'.format(i+1,carro[0],carro[1],1000/carro[1],1000/carro[1]*2.25))
carrosEconsumo.sort(key=lambda lista: lista[1])
print('O menor consumo é do {}.'.format(carrosEconsumo[-1][0]))
