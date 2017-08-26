cont = 0
res = 0
idadeCrianca = int(input('Digite a idade da criança:'))
while idadeCrianca >= 3 and idadeCrianca <= 6:
    cont += 1
    idadeCrianca = int(input('Digite a idade da criança ou digite 0 para parar e obter o resultado:'))
print('A quantidade de crianças que serão vacinadas é {0}'.format(cont))