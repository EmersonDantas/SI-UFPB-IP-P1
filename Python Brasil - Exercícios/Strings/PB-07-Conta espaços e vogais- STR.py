entrada = str(input('Digite uma string:\n'))
vogais = 0
espacos = 0
for i in entrada:
    if i in 'aeiou':
        vogais += 1
    if i == ' ':
        espacos += 1

print('Em "{}" há {} vogais e {} espaços.'.format(entrada,vogais,espacos))
