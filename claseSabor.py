class Sabor:
    __numero = 0
    __nombre = ''
    __descripcion = ''

    def __init__(self,numero=0,nombre='',desc=''):
        self.__numero = numero
        self.__nombre = nombre
        self.__descripcion = desc
    def __str__(self):
        cadena = '{0!s:3}{1:24}'.format(self.__numero,self.__nombre)
        return cadena
    def getNum(self):
        return self.__numero