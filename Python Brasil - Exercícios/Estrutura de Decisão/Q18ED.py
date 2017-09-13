data = input('Digite a data no formato DD/MM/AAAA, SEM '"/"':\n')

vv = len(data)#Verificando se a data foi inserida sem barras.
sonum = data.isdigit()#Verificando se existem somente números.

if vv == 8 and sonum:
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:8])

    if dia <= 31 and dia >= 1 and mes >= 1 and mes <= 12 and ano >= 1: #Analizador
        data = True
    else:
        data = False
        print('Data inválida!')
        
    if data:
        print('A data digitada é válida.')
else:
    print('Valores errados!')




