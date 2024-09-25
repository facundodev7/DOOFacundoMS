schema = "Nombre,Apellido,Edad,Email"
row = "Emiliano,Billi,42,emiliano@gmail.com"

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
        
o = Str2Dic(schema)
d = o.converter(row)
print(d)
