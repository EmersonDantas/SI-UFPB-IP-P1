# UFPB IV - SI
# Emerson Dantas - MATRICULA: 20170050755
# emerson.ruan@dce.ufpb.br
# github.com/emersondantas
# coding: utf-8
# outubro/2017

erroInput = 'Entrada inválida!'

def DecimalToBinario(entrada, resultado):
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
            resultado['text'] = ('Binário: {}'.format(binAntes[::-1] + '.' + binDepois))

        else:
            resultado['text'] = ('Binário: {}'.format(binAntes[::-1]))
            
    else:
        resultado['text'] = erroInput

def BinarioToDecimal(entrada, resultado):
    entrada = entrada.get()
    verificaNum = entrada.replace('.', '')
    decAntes, decDepois = '', ''
    soma = 0

    if '.' in entrada:
        antes, depois = entrada.split('.')

    else:
        antes = entrada

    for valor in verificaNum:
        if valor != '1' and valor != '0':
            verifica = False
            break
        
        else:
            verifica = True

    if verificaNum.isdigit() and verifica:
        for a, valor in enumerate(antes[::-1]):
            soma += int(valor) * 2 ** a

        decAntes = soma
        soma = 0

        if '.' in entrada:
            for b, valor in enumerate(depois):
                soma += int(valor) * 0.5 ** (b + 1)

            decDepois = soma

        if '.' in entrada:
            resultado['text'] = ('Decimal: {}.{}'.format(decAntes, str(decDepois)[2:]))

        else:
            resultado['text'] = ('Decimal: {}'.format(decAntes))
            
    else:
        resultado['text'] = erroInput

def OctalToDecimal(entrada, resultado):
    entrada = entrada.get()
    soma = 0
    octalValor = '01234567'

    if len(entrada) == 0:
        verifica = False 

    for a in entrada:
        if a not in octalValor:  
            verifica = False
            break
        
        else:
            verifica = True

    if verifica:
        for b, num in enumerate(entrada[::-1]):
            soma += int(num) * 8 ** b

        resultado['text'] = ('Decimal: {}' .format(soma))
        
    else:  
        resultado['text'] = erroInput

def DecimalToOctal(entrada,resultado):
    entrada = entrada.get()
    octal = ''

    if entrada.isdigit(): 
        entrada = int(entrada)
        
        while entrada != 0:
            octal += str(entrada % 8)
            entrada = entrada // 8

        resultado['text'] = 'Octal: {}' .format(octal[::-1])
        
    else:
        resultado['text'] = erroInput

def HexadecimalToDecimal(entrada, resultado):
    entrada = entrada.get()
    hexadecimalList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    verifica = True
    soma = 0
    diferenca = 0

    if len(entrada) == 0:
        verifica = False 

    for e in entrada:
        for v in hexadecimalList:
            if e != v:
                diferenca += 1

            if diferenca >= 16:
                verifica = False
                break
            
        diferenca = 0
            
    if verifica:
        for a,num in enumerate(entrada[::-1]):
            for b,valor in enumerate(hexadecimalList):
                if num == valor:
                    soma += int(b) * 16 ** int(a)

        resultado['text'] = ('Decimal: {}' .format(soma))
        
    else:
        resultado['text'] = erroInput

def decimalToHexadecimal(entrada, resultado):
    entrada = entrada.get()
    hexa = ''
    hexadecimalList = ['A', 'B', 'C', 'D', 'E', 'F']

    if entrada.isdigit():
        while entrada != 0:
            entrada = int(entrada)
            resto = entrada % 16
            entrada = entrada // 16
            
            if  resto >= 10:
                indiceLetra = resto - 10
                hexa += hexadecimalList[indiceLetra]
                
            else:
                hexa += str(resto)

        resultado['text'] = ('Hexadecimal: {}' .format(hexa[::-1]))  

    else:
        resultado['text'] = erroInput
