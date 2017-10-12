import FuncaoVerificaEMesExtenso

data = str(input('Digite a data de nascimento no formato DD/MM/AAAA:\n'))
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:11])
lista = FuncaoVerificaEMesExtenso.verificaData(dia,mes,ano)
print('Você nasceu em {} de {} de {}.'.format(lista[0],lista[1],lista[2]))
