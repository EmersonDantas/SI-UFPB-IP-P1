#EMERSON DANTAS S.I IP-P1
velocidade = int(input('Qual a velocidade do veículo:'))
if velocidade > 80:
    print('Você foi multado em R${m} por excesso de velocidade.'.format(m=((velocidade-80)*5)))
else:
    print('Você está dirigindo dentro da velocidade permitida.')