from tkinter import *
from tkinter import ttk
from valores import *

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")


label = Frame(janela, width=235,height=50)
label.grid(row=0, column=0)
label.config(bg=cor_azul)

frame_corpo = Frame(janela, width=235,height=268,bg=cor_cinza)
frame_corpo.grid(row=1, column=0)



b_1 = Button(janela, text="C", width=11, height=2)
b_1.place(x=0,y=0)
b_2 = Button(janela, text="%", width=11, height=2)
b_2.place(x=116,y=0)


janela.mainloop()