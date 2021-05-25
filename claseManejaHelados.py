from claseSabor import Sabor
from claseHelado import Helado

class ManejaHelados:
    tipos = [100,150,250,500,1000]
    __helados = []

    def __init__(self):
        self.__helados = []
    
    #Registro un helado vendido
    def registrarHelado(self,tipo):
        tipo = self.validarTipo(tipo)
        resultado = None
        if tipo != None:
            newHelado = Helado(tipo)
            self.__helados.append(newHelado)
            #Retorno el helado para agregarle sabores
            resultado = newHelado 
        return resultado

    #Validar tipo de helado
    def validarTipo(self,tipo):
        valido = None
        try:
            tipo = int(tipo)
            if tipo in self.tipos:
                valido = tipo
            else:
                print('Tipo de helado incorrecto.')
        except ValueError:
            print('Tipo de helado incorrecto')
        return valido  
    
    #Muestro los 5 SABORES mas vendidos 
    def getAllSabores(self):
        sabores = []
        for helado in self.__helados:
            sabores.extend(helado.getSabores())
        return sabores

    #Obtengo total de gramos vendidos
    def getTotalGramos(self,miSabor):
        if isinstance(miSabor,Sabor):
            gramos = 0
            for helado in self.__helados:
                sabores = helado.getSabores()
                if miSabor in sabores:
                    gramos += helado.getGramos() / len(sabores)
            print('Gramos vendidos: {0:.2f}gr.'.format(gramos))   
        else:
            print('Debe ingresar un sabor')
        

    #Obtengo los sabores vendidos segun un tipo de helado
    def showSaboresSegunTipo(self,tipo):
        tipo = self.validarTipo(tipo)
        misSabores = []
        if tipo != None:
            #Encabezado
            header ='+' + '-'*50 + '+'
            print(header)
            print('|{0:^50}|'.format('SABORES VENDIDOS SEGUN TIPO DE HELADO'))
            print(header)
            print('| Tipo: {0:43}|'.format(str(tipo)))
            print(header)
            for helado in self.__helados:
                gramos = helado.getGramos()
                if tipo == gramos:
                    sabores = helado.getSabores()
                    for sabor in sabores:
                        if sabor not in misSabores:
                            misSabores.append(sabor)
            #Muestro los sabores
            for sabor in misSabores:
                print('| {0:49}|'.format(sabor.__str__())) 
            print(header)