revistas = []
livro = []
perguntas = ['Qual a editora:','Qual o titulo:','Qual é o preço:']
continuar = 'kkk eae men'
quantiG = 0
maior = 0
soma = 0
cont = 0
while continuar != 'fim':
    print('ADICIONANDO LIVROS\nPara parar digite FIM na primeira pergunta.')
    for p in range(len(perguntas)):
        if p != 2 and p != 3:
            entrada = str(input(perguntas[p]))
            livro.append(entrada)
        else:
            livro.append(float(input(perguntas[p])))
        if str.lower(livro[0]) == 'fim':
            continuar = 'fim'
            break
    livro.append(0)
    revistas.append(livro)
    livro = []
    if continuar == 'fim':
            del revistas[-1]

for index in revistas: #Quantidade de revistas da editora
    if str.lower(index[0]) == 'globo':
        quantiG += 1

for i in range(len(revistas)): #Titulos iguais, quantidades de venda
    for a in range(len(revistas)):
        if revistas[i][1] == revistas[a][1]:
            revistas[i][3] += 1

maior = revistas[0][3]
nomeMaior = revistas[0][1]
maisde100 = 0
contM100 = 0
for e in range(len(revistas)): #Titulo mais vendido
    if revistas[e][3] > maior:
        maior = revistas[e][3]
        nomeMaior = revistas[e][1]
    if revistas[e][3] > 100: #Valor médio dos titulos com mais de 100 vendas
        maisde100 += revistas[e][2]
        contM100 += 1

print('Quantidade de revistas da editora globo: {};\n'
      'Titulo da revista mais vendida: {};\n'.format(quantiG,nomeMaior))
if maisde100 > 0:
    print('Valor médio das revistas com mais de 100 exemplares vendidos: R${:.2f}'.format(maisde100/contM100))