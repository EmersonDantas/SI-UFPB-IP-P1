#EMERSON DANTAS S.I IP-P1
distancia = float(input('Digite a distância à percorrer:'))
if distancia > 200:
    valor = 0.45
else:
    valor = 0.50
total = distancia*valor
print('A passagem custa R${t:.2f} para viajar {d}Km'.format(t=total,d=distancia))