n = str(input('Digite um número entre 1 e 99:\n'))
numeros = ['um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catoze','quinze','dezesseis','dezessete','dezoito','dezenove']
decimais = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

if len(n) == 1 or int(n[0]) == 1:
    print(numeros[int(n)-1])
     
else:
    print('{} e {}'.format(decimais[int(n[0])-2],numeros[int(n[1])-1]))
