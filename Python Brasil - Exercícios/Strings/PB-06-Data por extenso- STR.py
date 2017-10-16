calendario = [['janeiro',31],['fevereiro',28],['março',31],['abril',30],['maio',31],['junho',30],['julho',31],['agosto',31],['setembro',30],['outubro',31],['novembro',30],['dezembro',31]]

data = str(input('Digite a data no formato DD/MM/AAAA:\n'))
verifica = data.replace('/','')
dia, mes, ano = int(data[0:2]), int(data[3:5]), int(data[6:])

if mes <= 12:
    diaMax = calendario[mes-1][1]
    
else:
    diaMax = 50

if len(data) == 10 and verifica.isdigit() and  dia <= diaMax and mes <= 12 and ano >= 0:
    print('Você nasceu em {} de {} de {}.'.format(dia,calendario[mes-1][0],ano))
       
else:
    print('Data inválida!')
