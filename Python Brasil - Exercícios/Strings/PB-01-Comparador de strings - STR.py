entrada0 = str(input('Digite uma string:\n'))
entrada1 = str(input('Digite outra string:\n'))
tamanho0 = len(entrada0)
tamanho1 = len(entrada1)
resT = 'null'
resI = 'null'

if tamanho0 == tamanho1:
    resT = 'iguais'
    
else:
    resT = 'diferentes'

if entrada0 == entrada1:
    resI = 'igual'
    
else:
    resI = 'diferente'
    
print('Tamanho de "{}": {}\n'
      'Tamanho de "{}": {}\n'
      'As duas strings são de tamanhos {}.\n'
      'As duas strings possuem conteúdo {}.\n'
      .format(entrada0, tamanho0, entrada1, tamanho1, resT, resI))

    
            
