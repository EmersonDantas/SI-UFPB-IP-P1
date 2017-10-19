# UFPB IV - SI
# Emerson Dantas - MATRICULA: 20170050755
# emerson.ruan@dce.ufpb.br
# github.com/emersondantas
# coding: utf-8

hexadecimalList = ['A','B','C','D','E','F']
                   
def decimalToBinario(entrada, resultado):
	entrada = entrada.get()
	verificaNum = entrada.replace('.', '')
	binAntes = ''
	binDepois = ''
	bits = 0

	if verificaNum.isdigit() and int(verificaNum) >= 0:
		if '.' in entrada:    
			antes, depois = entrada.split('.')
			antes, depois = int(antes), float('0.' + depois)
                    
		else:
			antes = int(entrada)

		while antes != 0:
			binAntes += str(antes % 2)
			antes = antes // 2

		if '.' in entrada:
			while str(depois)[2:] != '0' and bits != 8:
				depois = float(depois)
				depois = depois * 2
				binDepois += str(depois)[0]

				if str(depois)[0] == '1':
					depois = '0.' + str(depois)[2:]
	            
				bits += 1

		if '.' in entrada:
			resultado['text'] = ('Binário: {}'.format(binAntes + '.' + binDepois))

		else:
			resultado['text'] = ('Binário: {}'.format(binAntes))
	else:
		resultado['text'] = 'Entrada inválida!'

def binarioToDecimal(entrada, resultado):
	entrada = entrada.get()
	verificaNum = entrada.replace('.', '')
	decAntes, decDepois = '',''
	soma = 0

	if '.' in entrada:
		antes, depois = entrada.split('.')

	else:
		antes = entrada

	for valor in verificaNum:
		if valor != '1' and valor != '0':
			verifica = False
		else:
			verifica = True


	if verificaNum.isdigit() and verifica:

		for a,valor in enumerate(antes):
			soma += int(valor) * 2 ** a

		decAntes = soma
		soma = 0

		if '.' in entrada:
			for b,valor in enumerate(depois):
				soma += int(valor) * 0.5 ** (b + 1)

			decDepois = soma

		if '.' in entrada:
			resultado['text'] = ('Decimal: {}.{}' .format(decAntes, str(decDepois)[2:]))

		else:
			resultado['text'] = ('Decimal: {}' .format(decAntes))
	else:
		resultado['text'] = 'Entrada inválida!'




    

'''
def octal(entrada, resultado):
    entrada = int(entrada.get())
    resultado['text'] = oct(entrada)

def hexadecimal(entrada, resultado):
    entrada = int(entrada.get())
    resultado['text'] = hex(entrada)'''
