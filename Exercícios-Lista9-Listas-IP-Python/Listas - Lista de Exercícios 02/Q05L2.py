animais = []
for i in range(100):
    nome = str(input('Qual o nome do animal:\n'))
    idade = int(input('Qual a idade do animal:\n'))
    tipo = str.lower(input('Qual o tipo do animal:\n'))
    animais.append([nome,idade,tipo])
print(animais)