"""Algoritmo que lê a idade de uma pessoa expressa em dias e mostra expressa em
anos, meses e dias."""
#Emerson Dantas S.I IP-P1
#02/08/2017 14:50

print('Digite sua idade em dias:')
IDD= int(input('Idade:'))
AQ = IDD / 365
AR = IDD % 365
MQ = AR / 30
DIAS = AR % 30
print('Anos:',(int(AQ)),'\n''Meses:',(int(MQ)),'\n''Dias:',(int(DIAS)))
