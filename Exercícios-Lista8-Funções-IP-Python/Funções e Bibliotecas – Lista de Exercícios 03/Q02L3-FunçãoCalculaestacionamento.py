def calculaEstacionamento(tipo,horas,minutos):
    tipo = str.lower(tipo)

    if tipo == 'carro':
        if horas > 5:
            pagar = (horas - 5)*2 + 3

            if minutos > 0:
                pagar += 2
            
        else:
            pagar = 3

        return pagar
    
    if tipo == 'moto':
        if horas > 5:
            pagar = ((horas - 5)*2 + 3)
            
            if minutos > 0:
                pagar += 2
                
        else:
            pagar = 3

        return pagar/2

continuar = 'sim'
while continuar == 'sim':
    tipo = str(input('Digite se seu veículo é um carro ou uma moto:\n'))
    horas = int(input('Digite quantas horas seu veículo passou no estacionamento:\n'))
    minutos = int(input('Digite quantos minutos seu veículo passou no estacionamento:\n'))
    print('Valor a ser pago: R${:.2f}'.format(calculaEstacionamento(tipo,horas,minutos)))
    continuar = str.lower(input('\n\nDeseja continuar? sim ou não:\n'))
            
