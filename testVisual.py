import os
os.system('cls')



class Test(object):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self):
        r = self.valor1 + self.valor2
        return r
    
    def restar(self):
        r = int(self.valor1) - int(self.valor2)
        return r
    
    def __str__(self):
        return "Hola"