A = 80000
B = 200000
anos = 0
while A < B:
    A *= 1.03
    B *= 1.015
    anos += 1
print('{} anos necessários para o país A se igualhe ou ultrapasse o país B.'.format(anos))
