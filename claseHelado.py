from claseSabor import Sabor #Es necesario importarlo?

class Helado:
    __gramos = 0 #Da el tipo de helado (100gr, 150gr,250gr,500gr,1000gr)
    __sabores = [] #de 1 a 4

    def __init__(self,gramos,sabor = None):
            self.__gramos = gramos
            self.__sabores = []
            if sabor != None:
                self.addSabor(sabor)

    def __str__(self):
        cadena = 'Tipo: {} Sabores: '.format(self.__gramos)
        for sabor in self.__sabores:
            cadena += '{}'.format(sabor)
        return cadena
    
    def getGramos(self):
        return self.__gramos

    def addSabor(self,miSabor):
        if isinstance(miSabor,Sabor):
            if len(self.__sabores) < 4:
                if miSabor not in self.__sabores:
                    self.__sabores.append(miSabor)
                else:
                    print('Ya agrego ese sabor.')
            else:
                print('Ya no puede agregar mas sabores')
        else:
            print('Error: Debe agregarse un sabor')
        print('Sabores {}/4'.format(len(self.__sabores)))

    #Retorna una lista con los sabores del helado
    def getSabores(self):
        return self.__sabores