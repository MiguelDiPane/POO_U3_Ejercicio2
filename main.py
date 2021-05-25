import csv
from claseManejaSabores import ManejaSabores
from claseManejaHelados import ManejaHelados
from claseMenu import Menu

if __name__ == '__main__':
    sabores = ManejaSabores()
    helados = ManejaHelados()

    archivo = open('sabores.csv')
    reader = csv.reader(archivo,delimiter=';')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
        else:
            sabores.addSabor(fila[0],fila[1],fila[2])      
    archivo.close() 
    
    menu = Menu()
    menu.define_menu('HELADERIA EL CONITO',['[1] - Registrar venta','[2] - Mostrar 5 mas vendidos','[3] - Estimar total de gramos vendidos','[4] - Sabores vendidos segun tipo de helado','[0] - Salir'])
    menu.showMenu()
    op = menu.selectOption()
    while op != 0:
        sabores.showSabores()
        print('TIPOS DE HELADO: 100gr - 150gr - 250gr - 500gr - 1000gr\n')
        #Registro venta de helado
        if op == 1:
            #Selecciono tipo de helado
            tipo = input('Elija tipo de helado: ')
            #Registro helado
            newHelado = helados.registrarHelado(tipo)
            #Agrego sabores
            if newHelado != None:
                num = input('Elija numero de sabor (0 para terminar): ')
                while num != '0':
                    miSabor = sabores.selectSabor(num)
                    if miSabor != None:
                        newHelado.addSabor(miSabor)
                    num = input('Elija numero de sabor (0 para terminar): ')
            input('Presione ENTER para continuar...')
        
        #Muestro 5 sabores mas vendidos
        elif op == 2:
            saboresVendidos = helados.getAllSabores()
            sabores.getMaxVentas(saboresVendidos)
            input('Presione ENTER para continuar...')

        #Ingresar numero de sabor y estimar el total de gramos vendidos
        elif op == 3:
            numero = input('Ingrese numero de sabor: ')
            sabor = sabores.selectSabor(numero)
            helados.getTotalGramos(sabor)           
            input('Presione ENTER para continuar...')

        elif op == 4:
            tipo = input('Ingrese tipo de helado: ')
            helados.showSaboresSegunTipo(tipo)
            input('Presione ENTER para continuar...')
        
        menu.showMenu()
        op = menu.selectOption()
        


    
