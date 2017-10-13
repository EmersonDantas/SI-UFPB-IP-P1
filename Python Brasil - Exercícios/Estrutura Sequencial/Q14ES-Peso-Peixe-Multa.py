multa = 0
excedente = 0
peso = float(input('Digite o peso do peixe: '))
if peso > 50:
    excedente = peso - 50
    multa = excedente * 4
print('Excedente: {0}kg\nMulta: R${1:.2f}'.format(excedente,multa))
