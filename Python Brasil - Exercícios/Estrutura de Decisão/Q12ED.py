valor = float(input('Quanto você ganha por horas:\n'))
horas = int(input('Quantas horas você trabalha por mês:\n'))
salariobruto = valor * horas

if salariobruto <= 900:
    fgts = salariobruto * 0.11
    sindi = salariobruto * 0.03
    inss = salariobruto * 0.1
    
elif salariobruto > 900 and salariobruto <= 1500:
    fgts = salariobruto * 0.11
    sindi = salariobruto * 0.03
    inss = salariobruto * 0.1
    ir = salariobruto * 0.05
    
elif salariobruto > 1500 and salariobruto <= 2500:
    fgts = salariobruto * 0.11
    sindi = salariobruto * 0.03
    inss = salariobruto * 0.1
    ir = salariobruto * 0.1
    
else:
    fgts = salariobruto * 0.11
    sindi = salariobruto * 0.03
    inss = salariobruto * 0.1
    ir = salariobruto * 0.2
fgts = salariobruto * 0.11
desctotal = inss + ir
salarioliquido = salariobruto - desctotal
print('Salário Bruto:                 : R$  {:.2f}\n'
        '(-) IR                          : R$  {:.2f}\n' 
        '(-) INSS                        : R$  {:.2f}\n'
        'FGTS                            : R$  {:.2f}\n'
        'Total de descontos              : R$  {:.2f}\n'
        'Salário Liquido                 : R$  {:.2f}\n'
      .format(salariobruto, ir, inss, fgts, desctotal, salarioliquido))
