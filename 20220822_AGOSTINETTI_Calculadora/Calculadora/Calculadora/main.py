from ast import Lambda
from operator import length_hint
from re import A
from tkinter import *
from tkinter import ttk
from valores import *
from collections import Counter

# Telas ...
display = Tk()
display.title("Calculadora")
display.geometry("235x318")

style = ttk.Style(display)
style.theme_use("clam")
#Label...
label = Frame(display,width=300, height= 56, bg= cor_azul)
label.grid(row=1, column=0)

#Corpo...
corpo = Frame(display, width=300, height=340, bg = cor_branco)
corpo.grid(row=2, column=0)


#Funções de Calculo...
valores =' '
resultado = ''
def entrada(evento):
    global valores
    a = valores[-1]
    b = str(evento)
    print(a)
    if a == b and a =='+':
        b = ''

    valores = valores + b
    valor_texto.set(valores)
    

def limpar():
    global valores
    valores = ' '
    valor_texto.set(valores)

def calcular():
    global valores
    global resultado
    resultado = eval(valores)
    valor_texto.set(resultado)


valor_texto= StringVar()

#Propriedades da Label...


app_label = Label(label, textvariable= valor_texto,width=10, height=2, justify= CENTER, font=fonte_label, bg = cor_azul, fg= cor_branco_label  )
app_label.place(x=0,y=0)


#Botões...
b_1 = Button(corpo,command= lambda: limpar(), text="C", width=11, height=2,font=('Ivy 13 bold'))
b_1.place(x=0, y=0)
b_2 = Button(corpo,command = lambda: entrada('%'), text="%", width=5, height=2,font=('Ivy 13 bold'))
b_2.place(x=118, y=0)
b_3 = Button(corpo,command = lambda: entrada('/'), text="/", width=5, height=2,font=('Ivy 13 bold'))
b_3.place(x=177, y=0)

b_4 = Button(corpo,command = lambda: entrada('7'), text="7", width=5, height=2,font=('Ivy 13 bold'))
b_4.place(x=0, y=52)
b_5 = Button(corpo,command = lambda: entrada('8'), text="8", width=5, height=2,font=('Ivy 13 bold'))
b_5.place(x=59, y=52)
b_6 = Button(corpo,command = lambda: entrada('9'), text="9", width=5, height=2,font=('Ivy 13 bold'))
b_6.place(x=118, y=52)
b_7 = Button(corpo,command = lambda: entrada('*'), text="*", width=5, height=2,font=('Ivy 13 bold'))
b_7.place(x=177, y=52)

b_8 = Button(corpo,command = lambda: entrada('4'), text="4", width=5, height=2,font=('Ivy 13 bold'))
b_8.place(x=0, y=104)
b_9 = Button(corpo,command = lambda: entrada('5'), text="5", width=5, height=2,font=('Ivy 13 bold'))
b_9.place(x=59, y=104)
b_10 = Button(corpo, command = lambda: entrada('6'), text="6", width=5, height=2,font=('Ivy 13 bold'))
b_10.place(x=118, y=104)
b_11 = Button(corpo, command = lambda: entrada('-'), text="-", width=5, height=2,font=('Ivy 13 bold'))
b_11.place(x=177, y=104)

b_12 = Button(corpo, command = lambda: entrada('1'), text="1", width=5, height=2,font=('Ivy 13 bold'))
b_12.place(x=0, y=156)
b_13 = Button(corpo,command = lambda: entrada('2'), text="2", width=5, height=2,font=('Ivy 13 bold'))
b_13.place(x=59, y=156)
b_14 = Button(corpo,command = lambda: entrada('3'), text="3", width=5, height=2,font=('Ivy 13 bold'))
b_14.place(x=118, y=156)
b_15 = Button(corpo,command = lambda: entrada('+'), text="+", width=5, height=2,font=('Ivy 13 bold'))
b_15.place(x=177, y=156)

b_16 = Button(corpo, command = lambda: entrada('0'), text="0", width=11, height=2,font=('Ivy 13 bold'))
b_16.place(x=0, y=208)
b_17 = Button(corpo,command = lambda: entrada('.'), text=".", width=5, height=2,font=('Ivy 13 bold'))
b_17.place(x=118, y=208)
b_18 = Button(corpo,command= lambda: calcular(), text="=", width=5, height=2,font=('Ivy 13 bold'))
b_18.place(x=177, y=208)


display.mainloop()



