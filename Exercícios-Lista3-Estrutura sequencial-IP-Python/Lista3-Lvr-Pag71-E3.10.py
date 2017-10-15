#EMERSON DANTAS S.I IP-P1
Salario_inicial=float(input('Digite seu salário atual:'))
Aumento=float(input('Digite o aumento:'))
Aumentosalarial=(Salario_inicial*Aumento/100)
Novo_salario=Salario_inicial+Aumentosalarial
print('Aumento de %2.2f reais!'%Aumentosalarial)
print('Seu novo salário é %2.2f reais!'%Novo_salario)