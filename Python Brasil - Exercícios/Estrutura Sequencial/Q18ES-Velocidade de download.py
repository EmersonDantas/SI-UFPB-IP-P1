tamanho = float(input('Digite o tamanho de arquivo em Mb:\n'))
velocidade = float(input('Digite a velocidade do link em Mbps:\n'))
tempo = tamanho / velocidade
print('O download será feito em {0:.2f} minutos.'.format(tempo))
