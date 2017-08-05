#EMERSON DANTAS S.I-IP-P1
DiasUsados=int(input('Digite a quantidade de dias de uso do carro:'))
Kmrodados=float(input('Digite a quantidade de Km rodados:'))
precoD=DiasUsados*60
precoK=Kmrodados*0.15
precototal=precoD+precoK
print('Você deverá pagar R$%2.2f pelo aluguel do carro.'%(precototal))