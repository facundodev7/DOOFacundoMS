import os
os.system('cls')

from tkinter import *

class Cuadrado(object):
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def sumarClaseCuadrado(self):
        app.ent3.insert(0,int(self.valor1)+int(self.valor2))
    
    def cambiarvalor(self, v1):
        self.valor1 = v1


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Testeo")
        self.geometry("800x600")

        self.ent1 = Entry(self, font=("Arial", 14))
        self.ent1.place(x=10,y=10, width=50, height=50)
        self.ent2 = Entry(self, font=("Arial", 14))
        self.ent2.place(x=10,y=70, width=50, height=50)
        self.ent3 = Entry(self, font=("Arial", 14))
        self.ent3.place(x=10,y=130, width=50, height=50)
        self.bt1 = Button(self, text="Sumar", command=c.sumarClaseCuadrado)
        self.bt1.place(x=100, y=50, width=50, height=50)
        self.bt2 = Button(self, text="Calcular", command=lambda:c.cambiarvalor(self.ent1.get()))
        self.bt2.place(x=100, y=150, width=50, height=50)

c = Cuadrado(2,2)

def crear():
    global c
    c = Cuadrado(app.ent1.get(),app.ent2.get())

app = App()



app.mainloop()




