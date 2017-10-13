voto = 1
jose,joao,tiririca,foratemer,nulo,branco = 0,0,0,0,0,0
cont = 0

#A votação terminara quando o voto for igual a 0

while voto != 0:
    voto = int(input('Qual cadidato deseja votar:\n'
                     '1 = Jose;\n'
                     '2 = João;\n'
                     '3 = Tiririca;\n'
                     '4 = Fora Temer;\n'
                     '5 = Voto Nulo Nulo;\n'
                     '6 = Voto em Branco.\n'
                     'Digite o número correspondente ao seu candidato:'))
    if voto == 1:
        jose += 1
    elif voto == 2:
        joao += 1
    elif voto == 3:
        tiririca += 1
    elif voto == 4:
        foratemer +=1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        print('Voto inválido!')
    cont += 1
    
porcentonulo = (nulo / cont) * 100
porcentobranco = (branco / cont) * 100

print('{} pessoas votaram em Jose;\n'
      '{} pessoas votaram em João;\n'
      '{} pessoas votaram em Tiririca;\n'
      '{} pessoas votaram Fora Temer;\n'
      '{} pessoas votaram Nulo;\n'
      '{} pessoas votaram Branco;\n'
      '{:.2f}% de votos nulos em relação ao número de votos;\n'
      '{:.2f}% de votos brancos em relação ao número de votos.\n'
      .format(jose,joao,tiririca,foratemer,nulo,branco,porcentonulo,porcentobranco))
