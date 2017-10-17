from tkinter import *
from functools import partial
from bibliotecaConversor import *

        
janela = Tk()
#nome da janela



#Input
entrada = Entry(janela, bd = 10)
entrada.place(x = 25, y = 25)

#resultado
resultado = Label(janela, text = '', fg='blue')
resultado.place(x = 300, y = 150)

#Decimal
botao1 = Button(janela, width = 19, text = 'Decimal', fg = 'green')
botao1['command'] = partial(binarioFlutuanteDecimal, entrada)
botao1.place(x = 25, y = 70)

#Binário
botao2 = Button(janela, width = 19, text = 'Binário', fg = 'green')
botao2['command'] = partial(binarioFlutuanteDecimal, entrada)
botao2.place(x = 25, y = 100)

#Hexadecimal
botao3 = Button(janela, width = 19, text = 'Hexadecimal', fg = 'green')
botao3['command'] = partial(binarioFlutuanteDecimal, entrada)
botao3.place(x = 25, y = 130)

#Octal
botao4 = Button(janela, width = 19, text = 'Octal', fg = 'green')
botao4['command'] = partial(binarioFlutuanteDecimal, entrada)
botao4.place(x = 25, y = 160)


janela.geometry('350x200')
janela.mainloop()
