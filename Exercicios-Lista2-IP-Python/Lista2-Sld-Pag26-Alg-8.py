"""Algoritmo que lê a idade de uma pessoa expressa em dias e mostra expressa em
anos, meses e dias."""


IDD= 6570
AQ = IDD / 365
AR = IDD % 365
MQ = AR / 30
DIAS = AR % 30
print('Anos:',(int(AQ)),'\n''Meses:',(int(MQ)),'\n''Dias:',(int(DIAS)))
