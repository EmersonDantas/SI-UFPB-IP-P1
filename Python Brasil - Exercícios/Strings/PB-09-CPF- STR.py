cpf = str(input('Digite o CPF no formato xxx.xxx.xxx-xx:\n'))
test = cpf.replace('.','')
test = test.replace('-','')
if test.isdigit() and len(cpf) == 14 and len(test) == 11 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    print('{} é um CPF válido.'.format(cpf))
else:
    print('{} NÃO é um CPF válido.'.format(cpf))
