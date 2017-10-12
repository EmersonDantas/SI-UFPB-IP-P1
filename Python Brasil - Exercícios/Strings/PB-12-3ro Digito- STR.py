#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print('Valida e corrige número de telefone')
numero = str(input('Telefone:   '))

if len(numero.replace('-','')) == 7:
    numero = numero.replace('-','')
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    numero = '3' + numero
    print('Telefone corrigido sem formatação: {}\n'.format(numero))    
    print('Telefone corrigido com formatação: {}-{}'.format(numero[0:4],numero[4:8]))
          
    
elif len(numero.replace('-','')) == 8:
    print(numero)

else:
    print('Número inválido')
