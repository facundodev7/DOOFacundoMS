import os
os.system('cls')

from Coleccion import *
from Documento import *
from Str2Dic import *

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
            