animais = []
pesquisa = []
for i in range(4):
    nome = str(input('Qual o nome do animal:\n'))
    idade = int(input('Qual a idade do animal:\n'))
    tipo = str.lower(input('Qual o tipo do animal:\n'))
    animais.append([nome,idade,tipo])

tipo = str.lower(input('Qual o tipo de animal que deseja pesquisar:\n'))
for a in animais:
    if a[2] == tipo:
        pesquisa.append(a)
print(pesquisa)