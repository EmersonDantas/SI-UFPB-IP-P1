def converter24to12(horas,minutos):
    if horas < 12 and horas >= 0 and minutos >= 0 and minutos <=60:
        if horas == 0:
            return [12,'AM',minutos]
        else:
            return [horas, 'AM',minutos]
    elif horas >= 12 and horas <= 23 and minutos >= 0 and minutos <=60:
        if horas == 12:
            return [12,'PM',minutos]
        return [horas-12,'PM',minutos]
    else:
        return 'NULL'

continuar = 'sim'
while continuar != 'não':
    horas = int(input('Digite a hora:\n'))
    minutos = int(input('Digite os minutos:\n'))
    h12ampm = converter24to12(horas,minutos)
    h12 = h12ampm[0]
    ampm = h12ampm[1]
    minutos = h12ampm[2]
    print('{}:{} notado em 12h é: {}:{} {}.'.format(horas,minutos,h12,minutos,ampm))
    continuar = str.lower(input('Continuar, Sim ou Não:\n'))
