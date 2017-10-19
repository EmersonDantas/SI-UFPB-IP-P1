from tkinter import *
from functools import partial
from bibliotecaConvBases import *

janela = Tk()    

#janela['background'] = 'black'

janela.title('Conversor de bases numéricas')

#GUIA input

guia = Label(janela, font = ('Arial', 10, 'bold'), text = 'Digite o número e clique na base desejada:',  fg = 'black')
guia.place(x = 30, y = 1)

#Input
entrada = Entry(janela, bd = 10, width = 27, fg = 'blue' , bg = 'grey')
entrada.place(x = 44, y = 29)

#resultado
lbres = Label(janela, font = ('Palatino Linotype', 15), text = 'Resultado:',fg = 'black')
lbres.place(x = 43, y = 190)
resultado = Label(janela, font = ('Arial Black', 10, 'bold'), text = ' ', fg = 'blue')
resultado.place(x = 43, y = 220)

#Decimal
botao1 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Decimal', fg = 'black', bg = 'grey')
botao1['command'] = partial(binarioToDecimal, entrada, resultado)
botao1.place(x = 44, y = 70)

#Binário
botao2 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Binário', fg = 'black', bg = 'grey')
botao2['command'] = partial(decimalToBinario, entrada, resultado)
botao2.place(x = 44, y = 100)

#Octal
botao3 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Octal', fg = 'black', bg = 'grey')
botao3['command'] = partial(decimalToBinario, entrada, resultado)
botao3.place(x = 44, y = 130)

#Hexadecimal
botao4 = Button(janela, font = ('Arial', 10, 'bold'), width = 30, text = 'Hexadecimal', fg = 'black', bg = 'grey')
botao4['command'] = partial(decimalToBinario, entrada, resultado)

botao4.place(x = 44, y = 160)

#MAIN
#dev = Label(janela, font = ('Palatino Linotype', 6), bg = 'red', text = 'Desenvolvido por: Emerson Dantas. GitHub: emersondantas Email: emerson.ruan@dce.ufpb.br')
#dev.place(x = 1, y = 260)
janela.geometry('343x270')
janela.mainloop()
