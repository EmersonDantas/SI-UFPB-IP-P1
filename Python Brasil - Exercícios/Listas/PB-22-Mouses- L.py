identificacao = 1
defeitos = ['necessita da esfera','necessita de limpeza','necessita troca do cabo ou conector','quebrado ou inutilizado']
situacao = [0,0,0,0]
cont = 0
while identificacao != 0:
    identificacao = int(input('Digite um número para identificar o mouse:\n'))
    if identificacao != 0:
        defeito = int(input('Qual o defeito do mouse Nº{}:\n'
                              '1-necessita da esfera;\n'
                              '2-necessita de limpeza;\n'
                              '3-necessita troca do cabo ou conector;\n'
                              '4-quebrado ou inutilizado.\n'.format(identificacao)))
    if defeito >= 1 and defeito <= 4:
        situacao[defeito-1] += 1
        cont += 1
    else:
        print('Defeito inválido')
        
print('Quantidade de mouses: {}\n'
      'Situação - Quantidade - Percentual'.format(cont))
for i in range(len(defeitos)):
          print('{}-{} - {} - {:.0f}%'
                .format(i+1,defeitos[i],situacao[i],situacao[i]*100/sum(situacao)))