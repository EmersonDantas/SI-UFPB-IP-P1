def calculaCondominio(nome,dias):
    nome = str.lower(nome)
    pduna = 300
    pcha = 450
    ppet = 220
    if nome == 'duna':
        multa = (dias*0.02)*pduna
        alug = pduna
        
    elif nome == 'chateau':
        multa = (dias*0.04)*pcha
        alug = pcha

    elif nome == 'petit':
        multa = (dias*0.03)*ppet
        alug = ppet
    return [multa,alug]

continuar = 'sim'
while continuar == 'sim':
    nome = str(input('Digite o nome do condomínio:\n'))
    dias = int(input('Digite a quantidade de dias de atraso no pagamento do condomínio {}:\n'.format(nome)))
    multa = calculaCondominio(nome,dias)[0]
    alug =  calculaCondominio(nome,dias)[1]
    print('A multa por ter atrasado {} dias no pagamento do condomínio {} é R${:.2f}\nO valor total a ser pago é R${:.2f}'.format(dias,nome,multa,multa+alug))
    continuar = str.lower(input('Deseja continuar? sim ou não:\n'))
