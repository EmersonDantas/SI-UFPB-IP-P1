from tkinter import *
from functools import partial
from bibliotecaConversor import *

janela = Tk()    

janela['background'] = 'black'

janela.title('Conversor de bases numéricas')

#GUIA input

guia = Label(janela, text = 'Digite o número e clique na base desejada:',  bg = 'black',fg = 'white')
guia.place(x = 1, y = 1)



#Input
entrada = Entry(janela, bd = 10, fg = 'blue' , bg = 'grey')
entrada.place(x = 25, y = 25)

#resultado
resultado = Label(janela, text = '', bg = 'black', fg = 'blue')
resultado.place(x = 300, y = 150)

#Decimal
botao1 = Button(janela, width = 19, text = 'Decimal', fg = 'green', bg = 'black')
botao1['command'] = partial(binarioFlutuanteDecimal, entrada, resultado)
botao1.place(x = 25, y = 70)

#Binário
botao2 = Button(janela, width = 19, text = 'Binário', fg = 'green', bg = 'black')
botao2['command'] = partial(decimalFlutuanteBinario, entrada, resultado)
botao2.place(x = 25, y = 100)

#Hexadecimal
botao3 = Button(janela, width = 19, text = 'Hexadecimal', fg = 'green', bg = 'black')
botao3['command'] = partial(binarioFlutuanteDecimal, entrada, resultado)
botao3.place(x = 25, y = 130)

#Octal
botao4 = Button(janela, width = 19, text = 'Octal', fg = 'green', bg = 'black')
botao4['command'] = partial(binarioFlutuanteDecimal, entrada, resultado)
botao4.place(x = 25, y = 160)

#MAIN

janela.geometry('350x200')
janela.mainloop()
