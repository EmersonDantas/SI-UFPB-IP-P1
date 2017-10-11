calendario = [['janeiro',31],['fevereiro',28],['março',31],['abril',30],['maio',31],['junho',30],['julho',31],['agosto',31],['setembro',30],['outubro',31],['novembro',30],['dezembro',31]]

def verificaData(mes):
	lista = []
	if mes >= 1 and mes <= 12:
		return calendario[mes-1][0]
						
dia = int(input('Digite o dia:\n'))
mes = int(input('Digite o mês:\n'))
ano = int(input('Digite o ano:\n'))

if dia >= 1 and mes >= 1 and mes <= 12 and ano >= 0:
	print('{} de {} de {}'.format(dia,verificaData(mes),ano))
