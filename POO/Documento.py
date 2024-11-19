class Documento(object):
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}
    
    def obtenerValor(self, clave):
        return self.contenido.get(clave,None)

    def modificarValor(self,clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento id={self.id}, contenido={self.contenido}"