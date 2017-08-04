#EMERSON DANTAS S.I IP-P1
Dias=int(input('Digite Dias:'))
Horas=int(input('Digite Horas:'))
Minutos=int(input('Digite Minutos:'))
Segundos=int(input('Digite Segundos:'))
C1=(Dias*86400)
C1=(C1+(Horas*3600))
C1=(C1+(Minutos*60))
print('Convertido em segundos:',C1+Segundos)