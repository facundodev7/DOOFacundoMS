import os
os.system('cls')
from Str2Dic import Str2Dic
from Documento import Documento
from Coleccion import Coleccion

with open("C:\\Users\\facun\\Escritorio\\datos_personales.csv", "rt") as file:
    schema = file.readline().replace("\n", "")
    parser = Str2Dic(schema)
    incremental = 0
    nuevaCole = Coleccion("nuevaColeccion")
    
    for line in file:
        nuevo = Documento(incremental, parser.converter(line.strip()))  # Crea un nuevo Documento
        nuevaCole.addDocumento(nuevo)
        incremental += 1