#EMERSON DANTAS S.I IP-P1
pag = float(input('Informe o valor a pagar:'))
meiopag = str.lower(input('Informe o meio de pagamento.\nDinheiro, cartão ou cheque:'))
if meiopag == 'dinheiro':
    if pag >= 100:
        pagfinal = pag - (pag*0.1)
    else:
        pagfinal = pag
elif meiopag == 'cheque':
    pagfinal = pag
elif meiopag == 'cartão':
    douc = str.lower(input('Deseja pagar por débito ou crédito?'))
    if douc == 'crédito':
        parcelas = int(input('Digite em quantas parcelas você quer dividir sua compra no cartão, sendo no máximo 3 parcelas.:'))
        if parcelas > 3:
            print('Número de parcelas superou o limite!')
            exit()
        else:
            rescart = pag / parcelas
            print('Você pagará {p} parcelas de R${rc:.2f}, totalizando R${tt}'.format(p=parcelas, rc=rescart, tt = pag))
            exit()
    elif douc == 'débito':
        pagfinal = pag
    elif douc != 'débito' and douc != 'crédito':
        print('Escolha inválida! Escolha entre débito ou crédito.\nVerifique a escrita ao enviar!')
        exit()
elif meiopag != 'dinheiro' and meiopag != 'cheque' and meiopag != 'cartão':
    print('Meio de pagamento inválido!\nVerifique a escrita e tente novamente.')
    exit()
print('Você deverá pagar R${pf:.2f}'.format(pf=pagfinal))