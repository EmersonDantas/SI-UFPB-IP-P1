import bibliotecaCorreios
precoTotal = 0
sedexCont = 0
pesoTotal = 0
arrecadado = 0
for i in range(50):
    item = str(input('Digite o tipo de item (pacote ou documento):\n'))
    if bibliotecaCorreios.validaTipoItem(item):

        peso = float(input('Digite o peso, em Kg, do {} (somente números):\n'.format(item)))

        if bibliotecaCorreios.validaPeso(peso):

            gramas = bibliotecaCorreios.convertePeso(peso)
            pesoTotal += gramas
            precoTotal = bibliotecaCorreios.calculaCustoItem(gramas, item)
            embalagem = str(input('Qual o tipo de embalagem (pequena, média ou grande):\n'))

            if bibliotecaCorreios.validaEmbalagem(embalagem):

                precoTotal += bibliotecaCorreios.calculaCustoEmbalagem(embalagem)
                entrega = str(input('Qual o modo de entrega (normal, sedex ou sedex10):\n'))

                if bibliotecaCorreios.validaEntrega(entrega):
                    if str.lower(entrega) == 'sedex':
                        sedexCont += 1
                    precoTotal += bibliotecaCorreios.calculaCustoEntrega(entrega)

                    print('Total a pagar: R${}\n\n'.format(precoTotal))
                    arrecadado += precoTotal
                    precoTotal = 0
                else:
                    print('Modo de entrega inválido!')
            else:
                print('Embalagem inválida!')
        else:
            print('Peso inválido!')
    else:
        print('Item inválido!')

print('Total arrecadado: R${:.2f}\n'
      'Quantidade de envios por SEDEX: {}\n'
      'Soma do peso total dos itens enviados: {}g' \
      .format(arrecadado,sedexCont,pesoTotal))
