gh = float(input('Quanto você ganha por hora: '))
nhtm= float(input('Número de horas trabalhadas no mês: '))
salarioTotal = gh * nhtm
ir = salarioTotal * 0.11
inss = salarioTotal * 0.08
sindi = salarioTotal * 0.05
salarioLiquido = salarioTotal - (inss + sindi + ir)
print('Salário bruto: R${0}\nINSS: R${1}\nSindicato: R${2}\nSalário liquido: R${3}'
      .format(salarioTotal,inss,sindi,salarioLiquido))
