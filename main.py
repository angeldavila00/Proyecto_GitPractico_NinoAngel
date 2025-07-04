## Inicio proyecto ##

from funciones import *
from funcionesjson import *

menu=abrirJSON()
booleanito = True

while (booleanito):
    menu= abrirJSON()
    ## INICIO DEL PROGRAMA
    print("===================================")
    print(" Bienvenidos a el simulador Empanadas Doña Pepa")
    print("==================================")
    print("1.Registrar una empanada")
    print("2.Actualizar empanada")
    print("3.Eliminar empanada")
    print("4.salir")
    opcion= int(input("Dime una opcion numerica: "))
    if (opcion==1):
        print("==================================")
        print("Registrar una empanada")
        print("==================================")
        nombre=input("Dime el nombre de la empanada: ")
        precio=int(input("Dime el precio de la empanada: "))
        cantEmpanada=int(input("Dime la cantidad de ingredientes de la empanada: "))
        diccionarioNuevo= {
            "id": (menu[len(menu)-1]["id"])+1,
            "nombre": nombre,
            "precio":precio,
            "ingredientes":[]
        }
        for i in range (cantEmpanada):
            nombreIngre=input("Dime los ingredientes: ")
            disponibilidad=int(input("Dime si ese ingrediente esta disponible para la empanada: \n 1.si \n 2.no: \n Dime una opcion numerica: "))
            if(disponibilidad==1):
                disponible=("si")
            else:
                disponible=("no")
            dateingredientes={
                "nombreIngre":nombreIngre,
                "disponibilidad":disponible
            }
            diccionarioNuevo["ingredientes"].append(dateingredientes)
            menu.append(diccionarioNuevo)
            guardarJSON(menu)

    if (opcion==2):
        print("==================================")
        print("Actualizar empanadas")
        print("==================================")
        opcionId=int(input("Dime el numero de ID que quieres actualizar: "))
        datos(menu,opcionId)
        temporalDatos=menu[opcionId-1]
        nombreTemporal=input("Dime el nombre que deseas: ")
        precioTemporal=int(input("Dime el precio: "))
        cantEmpanada=int(input("Cuantos ingredientes tiene: "))
        IngreTemporal=[]
        for i in range(cantEmpanada):
            nombreIngre=input("Dime los nombres de los ingredientes: ")
            disponibilidad=int(input("Dime si esta disponible el producto en opcion numerica \n 1. si \n  2. no: "))
            if (disponibilidad==1):
                diccionarioTemporal={
                    "nombre":nombreIngre,
                    "disponibilidad":"si"
                }
            else:
                diccionarioTemporal={
                    "nombre":nombreIngre,
                    "disponibilidad":"no"
                }
            IngreTemporal.append(diccionarioTemporal)
            diccionarioAgregar={
                "id": menu[opcionId-1]["id"],
                "nombre": nombreTemporal,
                "precio": precioTemporal,
                "ingredientes":IngreTemporal
            }
            menu[opcionId-1]=diccionarioAgregar
            guardarJSON(menu)
    if(opcion==3):
        print("==================================")
        print("Eliminar empanada")
        print("==================================")
        opcionId=int(input("Dime el numero de ID que quieres eliminar: "))
        datos(menu,opcionId)
        confirmar=int(input(f"Seguro deseas eliminar esta empanada con este mumero de {id}: 1.Si o 2. No \n Dime una opcion numerica:  "))
        if(confirmar==1):
            menu.pop(opcionId-1)
            guardarJSON(menu)
            print("La empanada fue eliminada exitosamente")
        else:
            print("No fue eliminado el producto")
    if(opcion==4):
        print("===================================")
        print("Gracias!! vuelve pronto")
        booleanito=False