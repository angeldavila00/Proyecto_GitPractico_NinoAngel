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
        