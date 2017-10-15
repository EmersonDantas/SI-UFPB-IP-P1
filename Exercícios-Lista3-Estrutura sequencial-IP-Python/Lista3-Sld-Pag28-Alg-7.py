"""Algoritmo que lê a idade de uma pessoa expressa em anos, meses e dias e mostra
expressa apenas em dias."""
#Emerson Dantas S.I IP-P1
#02/08/2017 14:35
print('Digite sua idade:')
A= int(input('Ano:'))
B= int(input('Mês:'))
C= int(input('Dia:'))
DiasA = A * 365
DiasB = B * 30
print('Sua idade em dias:', DiasA + DiasB + C)
