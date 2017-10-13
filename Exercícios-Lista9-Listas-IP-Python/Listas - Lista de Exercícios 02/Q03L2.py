Funcionarios = [["Paulo", "Roberta", ["Ciro",5], ["Bianca", 3]], [ "Natália", "Júlio", ["Benjamin",10]],["Judite", "Israel",[ "Giovana",8], ["Mariana",4]], ["Yuri", "Andressa", [ "Nicolas",1], ["Miguel", 3],[ "Catarina", 3]]]
novaLista = []
for i in Funcionarios:
    x = i[1]
    y = len(x)
    for w in i[2:]:
        if (w[1] < 4):
            novaLista.append([y,len(w[0])])
print(novaLista)
for i in range(len(novaLista)):
    if (novaLista[i][0] < novaLista[i][1]):
        novaLista[i] = 2*novaLista[i][0]
    else:
        novaLista[i] = 2*novaLista[i][1]
print(novaLista)