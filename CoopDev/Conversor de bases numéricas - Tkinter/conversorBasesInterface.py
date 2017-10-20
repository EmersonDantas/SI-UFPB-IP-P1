# UFPB IV - SI
# Emerson Dantas - MATRICULA: 20170050755
# emerson.ruan@dce.ufpb.br
# github.com/emersondantas
# coding: utf-8
# outubro/2017

from tkinter import *
from functools import partial
from bibliotecaConvBases import *

janela = Tk()    

#janela['background'] = 'black'

janela.title('Conversor de bases numéricas')

#GUIA input

guia = Label(janela, font = ('Arial', 10, 'bold'), text = 'Digite o número e clique na base desejada:',  fg = 'black')
guia.place(x = 100, y = 1)

#Input
entrada = Entry(janela, bd = 10, width = 60, fg = 'blue' , bg = 'grey', text = 'Digite aqui:')
entrada.place(x = 100, y = 25)

#resultado
lbres = Label(janela, font = ('Palatino Linotype', 15), text = 'Resultado:',fg = 'black')
lbres.place(x = 43, y = 190)
resultado = Label(janela, font = ('Arial Black', 10, 'bold'), text = ' ', fg = 'blue')
resultado.place(x = 43, y = 220)

#Binario to decimal
botao1 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Binário para Decimal', fg = 'black', bg = 'grey')
botao1['command'] = partial(BinarioToDecimal, entrada, resultado)
botao1.place(x = 44, y = 70)

#Decimal para Binário
botao2 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Decimal para Binário', fg = 'black', bg = 'grey')
botao2['command'] = partial(DecimalToBinario, entrada, resultado)
botao2.place(x = 305, y = 70)

#Decimal para octal
botao3 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Decimal para Octal', fg = 'black', bg = 'grey')
botao3['command'] = partial(DecimalToOctal, entrada, resultado)
botao3.place(x = 305, y = 110)

#Octal para Decimal
botao3 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Octal para Decimal', fg = 'black', bg = 'grey')
botao3['command'] = partial(OctalToDecimal, entrada, resultado)
botao3.place(x = 44, y = 110)

#Hexadecimal para Decimal
botao4 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Hexadecimal para Decimal', fg = 'black', bg = 'grey')
botao4['command'] = partial(HexadecimalToDecimal, entrada, resultado)
botao4.place(x = 44, y = 150)

#Decimal para Hexadecimal
botao4 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Decimal para Hexadecimal', fg = 'black', bg = 'grey')
botao4['command'] = partial(decimalToHexadecimal, entrada, resultado)
botao4.place(x = 305, y = 150)

#MAIN
dev = Label(janela, font = ('Palatino Linotype', 10), bg = 'red', text = 'Desenvolvido por: Emerson Dantas. GitHub: emersondantas Email: emerson.ruan@dce.ufpb.br                ')
dev.place(x = 0, y = 250)
janela.geometry('600x270')
janela.mainloop()
