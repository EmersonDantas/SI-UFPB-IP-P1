#EMERSON DANTAS S.I IP-P1
pag = float(input('Informe o valor a pagar:'))
meiopag = str.lower(input('Informe o meio de pagamento. Dinheiro ou cheque:'))
if meiopag == 'dinheiro':
    if pag >= 100:
        pagfinal = pag - (pag*0.1)
    else:
        pagfinal = pag
elif meiopag == 'cheque':
    pagfinal = pag
elif meiopag != 'dinheiro' and meiopag != 'cheque':
    print('Meio de pagamento inválido!\nVerifique a escrita e tente novamente.')
    exit()
print('Você deverá pagar R${pf:.2f}'.format(pf=pagfinal))