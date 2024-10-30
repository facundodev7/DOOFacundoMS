import os
os.system('cls')
from Str2Dic import Str2Dic
from Documento import Documento

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
    
'''
test = Coleccion("hola")

test.importarColeccion("C:\\Users\\facun\\Escritorio\\datos_personales.csv")

print(test)

print(test.buscar_documento(1))
'''

test = Coleccion('test')

print(test.documentos.get(1))