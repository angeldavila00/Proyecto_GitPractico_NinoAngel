def recorrerIngredientes(menu,lugar):
    lugar -=1
    for i in range (len(menu[lugar]["ingredientes"])):
        print("=================")
        print("======================")
        print("==== Empanada #",i+1," ==")
        print("Ingrediente:",menu[lugar]["ingredientes"][i]["nombreIngre"])
        print("Disponibilidad:", menu[lugar]["ingredientes"][i]["disponible"])



def datos(menu,opcionId):
        print("===========================")
        print(" empanada numero", opcionId)
        print("=======================")
        print("Id", menu[opcionId-1]["id"])
        print("Nombre:",menu[opcionId-1]["nombre"])
        print("Precio:",menu[opcionId-1]["precio"])
        recorrerIngredientes(menu,opcionId)
        