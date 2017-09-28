
revistas = []
livro = []
perguntas = ['Qual a editora:','Qual o titulo:','Qual é o preço:','Quantos exemplares vendeu:']
continuar = 'kkk eae men'
quantiG = 0
maior = 0
soma = 0
cont = 0
while continuar != 'fim':
    print('-_-_-_-_-_-ADICIONANDO LIVROS-_-_-_-_-_-\nPara parar digite FIM na primeira pergunta.')
    for p in range(len(perguntas)):
        if p != 2 and p != 3:
            livro.append(str(input(perguntas[p])))
        else:
            livro.append(float(input(perguntas[p])))
        if str.lower(livro[0]) == 'fim':
            continuar = 'fim'
            break
            
    revistas.append(livro)
    livro = []
    print('-_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_-\n\n\n')
    if continuar == 'fim':
            del revistas[-1]

for index in revistas:
    if str.lower(index[0]) == 'globo':
        quantiG += 1
        
for index in revistas:
    temp = index[3]
    if temp > maior:
        maior = index[3]
        nomeMaior = index[1]
    if temp > 100:
        cont += 1
        soma += index[2]

print('Quantidade de revistas da editora globo: {};\n'
      'Titulo da revista mais vendida: {};\n'
      'Valor médio das revistas com mais de 100 exemplares vendidos: R${:.2f}'
      .format(quantiG,nomeMaior,soma/cont))
        
