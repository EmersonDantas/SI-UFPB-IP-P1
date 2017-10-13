import bibliotecaFly
precoTr = 0
contF = 0
for i in range(80):
    destino = str.lower(input('Qual o destino:\nNatal(Diurno),Fortaleza(Noturno) ou Recife(Diurno,Noturno):\n'))
    turno = str.lower(input('Qual o turno:\n'))
    if bibliotecaFly.validaDadosVoo(destino,turno):
        preco = bibliotecaFly.calculaValorVoo(destino,turno)
        print('Valor da passagem para: {}, no turno: {}.\nR${}'.format(destino,turno,preco))
        if destino == 'recife':
            precoTr += preco
        if destino == 'fortaleza':
            contF += 1
    else:
        print('Destino ou turno inválido!')
print('Valor total pago por passagens para Recife: R${}\nQuantidade de passagens vendidas para Fortaleza:{}'.format(precoTr,contF))