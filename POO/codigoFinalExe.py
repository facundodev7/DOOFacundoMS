import os
os.system('cls')

from tkinter import *
from Coleccion import *
from Documento import *
from Str2Dic import *

#Aca creo la Clase App, que hereda de Tk, que es la clase que importe para usar las ventanas
class App(Tk):
    def __init__(self):
        super().__init__()
        #El titulo de la ventana
        self.title('Bdd')
        #La anchura y altura de la ventana
        self.geometry('1280x720')
        #Los Label son un objeto, de tipo Label, que tiene argumentos, como font y text que es su contenido
        self.label1 = Label(self, font=('Arial',14), text='Base de datos')
        #Hasta donde se, todo lo que creamos tiene su metodo place, para decirle donde se posiciona en la ventana
        self.label1.place(x=10,y=10)

        self.label2 = Label(self, font=('Arial',14), text='')
        self.label2.place(x=10,y=250)

        self.label3 = Label(self, font=('Arial',14), text='')
        self.label3.place(x=10,y=300)

        self.entry1 = Entry(self, font=('Arial',14))
        self.entry1.place(x=10, y=50)
        #Esto es un objeto de tipo Boton, tambien tiene texto, font, pero lo interesante es su command
        #el argumento command, usa una funcion, y el argumento command=lambda:() me permite usar funciones, pero con argumentos, el command solo no permite argumentos
        self.boton1 = Button(self, text='Obtener documento en coleccion',font=('Arial',12), command=lambda:[self.obtenerDocumentoTexto()])
        self.boton1.place(x=10,y=165)

        self.boton2 = Button(self, text='crear coleccion',font=('Arial',12), command=lambda:[bdd.crearColeccion(self.entry1.get()), self.coleccionCreadaTexto(self.entry1.get())])
        self.boton2.place(x=10,y=85)

        self.boton3 = Button(self, text='importar csv',font=('Arial',12), command=self.campoParaImportar)
        self.boton3.place(x=10,y=125)

        self.boton4 = Button(self, text='Eliminar documento',font=('Arial',12), command=lambda:self.eliminarDocumento(self.entry1.get(), self.entryImportar2.get()))
        self.boton4.place(x=10,y=205)

        self.boton6 = Button(self, text='Print Doc',font=('Arial',12), command=lambda:self.obtener(self.entry1.get()))
        self.boton6.place(x=10,y=500)

        #Todo este bloque de Labels, es para crear labels vacios, que despues seran rellenados con texto una vez que se consulte el documento
        self.label2.config(text='')
        self.labelDocumento2 = Label(self, font=('Arial',14), text='')
        self.labelDocumento2.place(x=210,y=250)
        self.labelDocumento3 = Label(self, font=('Arial',14), text='')
        self.labelDocumento3.place(x=410,y=250)
        self.labelDocumento4 = Label(self, font=('Arial',14), text='')
        self.labelDocumento4.place(x=610,y=250)
        self.labelDocumento5 = Label(self, font=('Arial',14), text='')
        self.labelDocumento5.place(x=610,y=315)
        self.labelDocumentoNombre = Label(self, font=('Arial',14), text='')
        self.labelDocumentoNombre.place(x=10,y=275)
        self.labelDocumentoApellido = Label(self, font=('Arial',14), text='')
        self.labelDocumentoApellido.place(x=210,y=275)
        self.labelDocumentoEdad = Label(self, font=('Arial',14), text='')
        self.labelDocumentoEdad.place(x=410,y=275)
        self.labelDocumentoEmail = Label(self, font=('Arial',14), text='')
        self.labelDocumentoEmail.place(x=610,y=275)
        self.labelDocumentoTelefono = Label(self, font=('Arial',14), text='')
        self.labelDocumentoTelefono.place(x=610,y=350)

    #Una funcion para indicar que la coleccion X fue creada
    def coleccionCreadaTexto(self, texto):
        if self.label2.config(text=bdd.colecciones.get(texto, None)) == texto:
            self.label2.config(text=(f'La coleccion { texto }, ya existe'))
        else:
            self.label2.config(text=(f'Coleccion "{ texto }" creada'))

    #Una funcion para indicar que la colaccion X fue borrada
    def coleccionBorradaTexto(self, texto):
        self.label2.config(text=(f'Coleccion "{ texto }" borrada'))

    #Esta funcion muestra la coleccion y cuantos documentos tiene
    def cambiarValor(self):
        self.label3.config(text=(f"Base de datos documental con {len(bdd.colecciones)} colecciones"))

    def obtener(self, nombre):
        bdd.crearColeccion(nombre)
        self.label3.config(text=bdd.colecciones.get(nombre, None))

    #la funcion de este bloque es, crear los campos para importar, pero solo se muestran una vez que se le da click a importar
    def campoParaImportar(self):
        self.entryImportar = Entry(self, font=('Arial',14))
        self.entryImportar.place(x=400, y=50)
        self.botondeImportar = Button(self, text='importar',font=('Arial',12), command=lambda:[self.importarTest(self.entryImportar.get(), self.entryImportar2.get()), self.textodeImportar()])
        self.botondeImportar.place(x=400,y=90)
        self.labelImportar1 = Label(self, font=('Arial',14), text='Ingrese la ruta del csv')
        self.labelImportar1.place(x=400,y=10)
        self.labelImportar2 = Label(self, font=('Arial',14), text='')
        self.labelImportar2.place(x=400,y=175)
        self.labelImportar3 = Label(self, font=('Arial',14), text='Ingrese el nombre de la coleccion')
        self.labelImportar3.place(x=700,y=10)
        self.entryImportar2 = Entry(self, font=('Arial',14))
        self.entryImportar2.place(x=700, y=50)

    #Funcion que indica el exito en la importacion de documentos
    def textodeImportar(self):
        self.labelImportar2.config(text='Documentos Importados')

    #Un test para ver si funciona el import
    def importarTest(self, userinput, nombre):
        coleccion = bdd.obtenerColeccion(nombre)
        if coleccion:
            coleccion.importarColeccion(userinput)
            self.textodeImportar()
        else:
            self.labelImportar2.config(text=f'Colección {nombre} no encontrada.')

    #Esta funcion limpia los campos del documento, cambiando el valor del texto a '' para que este vacio
    def limpiarDocumento(self):
        self.label2.config(text='')
        self.label3.config(text='')
        self.labelDocumento2.config(text='')
        self.labelDocumento3.config(text='')
        self.labelDocumento4.config(text='')
        self.labelDocumento5.config(text='')
        self.labelDocumentoNombre.config(text='')
        self.labelDocumentoApellido.config(text='')
        self.labelDocumentoEdad.config(text='')
        self.labelDocumentoEmail.config(text='')
        self.labelDocumentoTelefono.config(text='')

    #Esta funcion obtiene el documento, con un try, para cuando no se obtenga el documento, por ser borrado por ejemplo, se indique tal caso
    def obtenerDocumentoTexto(self):
        nombre = self.entryImportar2.get()
        coleccion = bdd.obtenerColeccion(nombre)
        try:
            self.label3.config(text='')
            numero = int(self.entry1.get())
            self.label2.config(text='Nombre')
            self.labelDocumento2.config(text='Apellido')
            self.labelDocumento3.config(text='Edad')
            self.labelDocumento4.config(text='Email')
            self.labelDocumento5.config(text='Telefono')
            self.labelDocumentoNombre.config(text=(coleccion.documentos[numero].contenido['Nombre']))
            self.labelDocumentoApellido.config(text=(coleccion.documentos[numero].contenido['Apellido']))
            self.labelDocumentoEdad.config(text=(coleccion.documentos[numero].contenido['Edad']))
            self.labelDocumentoEmail.config(text=(coleccion.documentos[numero].contenido['Email']))
            self.labelDocumentoTelefono.config(text=(coleccion.documentos[numero].contenido['Telefono']))
        except KeyError:
            self.limpiarDocumento()
            self.label3.config(text='El documento con id: {} no existe'.format(numero))

    #Funcion para eliminar documento
    def eliminarDocumento(self, id, nombre):
        self.limpiarDocumento()
        numero = int(id)
        coleccion = bdd.obtenerColeccion(nombre)
        coleccion.deleteDocumento(numero)
        textoAImprimir = 'Documento de id: {} eliminado'.format(numero) 
        self.label3.config(text=textoAImprimir)

    #El codigo de la clase BaseDeDatos, lo puse aca dentro en la etapa de testeo
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

    #El codigo de la clase Coleccion, lo puse aca dentro en la etapa de testeo
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

#Creo una objeto de Tipo app, para despues darle el comando mainloop, que hace que la ventana corra  
app = App()

#Esto para llamar metodos de la clase BaseDeDatos
bdd = BaseDeDatos()

app.mainloop()