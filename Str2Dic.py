schema = "Nombre,Apellido,Edad,Email,Telefono"
row = "Emiliano,Billi,42,emiliano@gmail.com,1122334455"

class SchemaError(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(message)

class Str2Dic(object):
    def __init__(self, schemaStr, separator=","):
        self.schema = schemaStr.split(separator)
        self.separator = separator

    def converter(self, row):
        temp = row.split(self.separator)
        if len(temp) == len(self.schema):
            i = 0
            d = {}
            while i < len(temp):
                d[self.schema[i]] = temp[i]
                i = i + 1
            return d
        else:
            raise SchemaError("Error en los campos de la fila")
        
o = Str2Dic(row)
try:
    d = o.converter(row)
except AttributeError:
    print('Parametro no permitido')
except SchemaError:
    print("Error de Schema")
