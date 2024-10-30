import os
os.system('cls')

from tkinter import *
from Coleccion import *
from Documento import *
from Str2Dic import *

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Bdd')
        self.geometry('1280x720')

        self.label1 = Label(self, font=('Arial',14), text='Base de datos')
        self.label1.place(x=10,y=10)

        self.label1 = Label(self, font=('Arial',14), text='')
        self.label1.place(x=10,y=250)

        self.entry1 = Entry(self, font=('Arial',14))
        self.entry1.place(x=10, y=50)

        self.boton1 = Button(self, text='obtener',font=('Arial',12), command=lambda:(self.obtener(self.entry1.get())))
        self.boton1.place(x=10,y=165)

        self.boton2 = Button(self, text='crear',font=('Arial',12), command=lambda:[bdd.crearColeccion(self.entry1.get()), self.coleccionCreadaTexto(self.entry1.get())])
        self.boton2.place(x=10,y=85)

        self.boton3 = Button(self, text='eliminar',font=('Arial',12), command=lambda:[bdd.eliminarColeccion(self.entry1.get()), self.coleccionBorradaTexto(self.entry1.get())])
        self.boton3.place(x=10,y=125)

        self.boton4 = Button(self, text='print',font=('Arial',12), command=self.cambiarValor)
        self.boton4.place(x=10,y=205)

        self.boton5 = Button(self, text='ir a colecciones',font=('Arial',12))
        self.boton5.place(x=10,y=500)

    def coleccionCreadaTexto(self, texto):
        if self.label1.config(text=bdd.colecciones.get(texto, None)) == texto:
            self.label1.config(text=(f'La coleccion { texto }, ya existe'))
        else:
            self.label1.config(text=(f'Coleccion "{ texto }" creada'))


    def coleccionBorradaTexto(self, texto):
        self.label1.config(text=(f'Coleccion "{ texto }" borrada'))

    def cambiarValor(self):
        self.label1.config(text=(f"Base de datos documental con {len(bdd.colecciones)} colecciones"))

    def borrarEntry1(self):
        self.entry1.delete(0,END)

    def obtener(self, nombre):
        self.label1.config(text=bdd.colecciones.get(nombre, None))

class BaseDeDatos(object):
    def __init__(self):
        self.colecciones = {}
    
    def crearColeccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
    
    def eliminarColeccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
    
    def obtenerColeccion(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones"

class Coleccion(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}

    def addDocumento(self, documento):
        self.documentos[documento.id] = documento

    def deleteDocumento(self, id_doc):
        if id_doc in self.documentos:
            del self.documentos[id_doc]
    
    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def importarColeccion(self, userInput):
        fileDirection = userInput
        
        with open (fileDirection, "rt") as file:
            schema = file.readline().replace("\n", "")
            parser = Str2Dic(schema)
            incremental = 0

            for line in file:
                nuevo = Documento(incremental, parser.converter(line.strip()))
                self.addDocumento(nuevo)
                incremental += 1
    
    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"
    

bdd = BaseDeDatos()
c = Coleccion('c')

app = App()

app.mainloop()