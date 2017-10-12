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

