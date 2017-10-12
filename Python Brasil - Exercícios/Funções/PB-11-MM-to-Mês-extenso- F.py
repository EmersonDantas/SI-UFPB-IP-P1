calendario = [['janeiro',31],['fevereiro',28],['março',31],['abril',30],['maio',31],['junho',30],['julho',31],['agosto',31],['setembro',30],['outubro',31],['novembro',30],['dezembro',31]]

def verificaData(dia,mes,ano):
        lista = []
        if mes >= 1 and mes <= 12:
                if dia > 1 and dia <= calendario[mes-1][1] and ano > 0:
                        return [dia,calendario[mes-1][0],ano]
                else:
                       return ['null','null','null'] 
        
        else:
                return ['null','null','null']
						
dia = int(input('Digite o dia:\n'))
mes = int(input('Digite o mês:\n'))
ano = int(input('Digite o ano:\n'))

lista = verificaData(dia,mes,ano)
print('{} de {} de {}'.format(lista[0],lista[1],lista[2]))
