### Tuplas ###

#Definir tupla:
mi_tupla = tuple()
mi_otra_tupla = ()

mi_tupla = (31, 1.64, "Xavi", "Quesada", "Quesada")
mi_otra_tupla = (35, 60, 25) 
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])
#print(mi_tupla[4]) IndexError
#print(mi_tupla[-5]) IndexError

print(mi_tupla.count("Quesada")) #Cuenta 2 porque hay 2
print(mi_tupla.count("Xaviku")) #No encuentra ninguno porque no hay
print(mi_tupla.index("Xavi")) #Indica la posicion en este caso la 2
print(mi_tupla.index("Quesada")) #Indica la posicion 3 porque se queda con el primero que encuentra

#No deja cambiar ni insertar variables, como si podíamos en las listas.
#mi_tupla[1] = 1.70
#print(mi_tupla)
#mi_tupla[5] = "Sabadell"

#Sumar o juntar tuplas 
mi_sum_tupla = mi_tupla + mi_otra_tupla
print(mi_sum_tupla)
print(mi_sum_tupla[3]) #Buscar el elemento 3
print(mi_sum_tupla[3:6]) #Buscar del elemento 3 al 6 (sin tener en cuenta el 6 sino muestra el 3,4 y 5)

#Cambiar de tupla a lista (Seria util para cambiar un valor)
mi_tupla = list(mi_tupla)
print(type(mi_tupla))
mi_tupla[4] = "Sabadell"
mi_tupla.insert(1, "Azul")
mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))

#Borrar tuplas
#del mi_tupla
#print(mi_tupla) #Nos lanza error (NameError: name 'mi_tupla' is not defined)
#del mi_tupla[2] #Tampoco podemos borrar 1 elemento de la tupla asi como si podíamos en las listas