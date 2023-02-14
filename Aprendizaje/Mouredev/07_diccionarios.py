### Diccionarios ###

#Definir Diccionarios:
mi_dict = dict()
mi_otro_dict = {}

print(type(mi_dict))
print(type(mi_otro_dict))

mi_otro_dict = {"Nombre":"Xavi","Apellido":"Quesada","Edad":31,1:"Python"}

mi_dict = {
  "Nombre":"Xavi",
  "Apellido":"Quesada",
  "Edad":31,
  "Lenguajes": {"Python","Swift","Kotlin"},
  1: 1.64
}

print(mi_otro_dict)
print(mi_dict)
print(len(mi_otro_dict))
print(len(mi_dict))
print(mi_dict["Nombre"])

#Cambiar un dato
mi_dict["Nombre"]="Pedro"
print(mi_dict["Nombre"])
print(mi_dict[1])

#Añadir nuevos elementos al diccionario
mi_dict["Calle"]="Calle Xaviku"
print(mi_dict)

#Eliminar elemento 
del mi_dict["Calle"]
print(mi_dict)

#Buscar si un elemento esta en el diccionario
#Solo busca la clave no el valor.
print("Xavi" in mi_dict) #False
print("Xaviku" in mi_dict) #False
print("Nombre" in mi_otro_dict) #True

#Muestra los items dentro del diccionario
print(mi_dict.items())
#Muestra las claves del diccionario
print(mi_dict.keys())
#Muestra los valores del diccionario
print(mi_dict.values())
print(mi_dict.fromkeys(("Nombre",1)))

#Crear un diccionario nuevo sin valores. Hay diferentes maneras de hacerlas y obtener el mismo resultado, puedes crear, clonar y obtener los valores.
mi_nuevo_dict = dict.fromkeys(("Nombre",1, "Ciudad"))
print(mi_nuevo_dict)

mi_dict = ["Nombre", 1, "Ciudad"]
mi_nuevo_dict = dict.fromkeys(mi_dict)
print(mi_nuevo_dict)

mi_nuevo_dict = dict.fromkeys(mi_dict)
print(mi_nuevo_dict)

#Así añade el dato a todos los valores
mi_nuevo_dict = dict.fromkeys(mi_dict,"Xavi")
print(mi_nuevo_dict)

#Trasformar a lista, tupla y set
print(list(mi_nuevo_dict))
print(tuple(mi_nuevo_dict))
print(set(mi_nuevo_dict))

#Ver los valores de toda la lista
mi_values = mi_nuevo_dict.values()
print(type(mi_values))
print(list(mi_nuevo_dict.values()))