from claseSabor import Sabor

class ManejaSabores:
    __sabores = []

    def __ini__(self):
        self.__sabores = []
    
    #Agrega un nuevo sabor a la lista
    def addSabor(self,numero,nombre,desc):
        try:
            numero = int(numero) 
            newSabor = Sabor(numero,nombre,desc)
            self.__sabores.append(newSabor)
        except ValueError:
            print('El numero de sabor debe ser un entero')
    
    #Devuelve el sabor seleccionado
    def selectSabor(self,numero):
        resultado = None
        try:
            numero = int(numero)
            i = 0
            esta = False
            while i < len(self.__sabores) and not esta:
                if self.__sabores[i].getNum() == numero:
                    esta = True
                else:
                    i +=1
            if esta:
                resultado = self.__sabores[i]
            else:
                print('Debe ingresar un numero de la lista')
        except ValueError:
            print('Error: Debe ingresar un numero de la lista')
        return resultado

    #Muestra la lista de helados disponibles de a 5 por fila
    def showSabores(self):
        header = '+' + '-'*140 + '+'
        print(header)
        print('|{:^140}|'.format('SABORES DISPONIBLES'))
        print(header)

        for sabor in self.__sabores:
            if sabor.getNum() % 5 == 0: #Si es divisible por 5 cambio de fila 
                print(' {0}'.format(sabor))
            else:
                print(' {0}'.format(sabor),end='')
        print(header)

    def getMaxVentas(self,saboresVendidos):
        #Inicializo contador
        contador = [0 for i in range(len(self.__sabores))]
        #Cuento cantidad de ocurrencias
        for sabor in saboresVendidos:
            numero = sabor.getNum()
            contador[numero-1] += 1
        
        #Encuentro 5 maximos
        header ='+' + '-'*38 + '+'
        print(header)
        print('|{:^38}|'.format('5 SABORES MAS VENDIDOS'))
        print(header)
        print('| {0:10}{1:3}{2:24}|'.format('Cantidad','N°','Nombre'))
        print(header)
        for i in range(5):
            maximo = max(contador)
            indiceMaximo = contador.index(maximo) #Indice del sabor maximo
            print('| {0!s:^10}{1}|'.format(maximo,self.__sabores[indiceMaximo]))
            contador[indiceMaximo] = -1 #coloco en -1 para buscar el siguiente maximo
        print(header)