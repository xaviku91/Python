### List Comprehesion ###
# Listas por comprensión
# Es una forma de crear listas de forma rápida y sencilla

# Como se crea una lista de forma tradicional
mi_lista_original = [0, 1, 2, 3, 4, 5, 6, 7]
print(mi_lista_original)

# Como se crea una lista por comprensión con range
mi_rango = range(8)
print(list(mi_rango))

# Como se crea una lista por comprensión con range
mi_lista = [i for i in range(8)]
print(mi_lista)

# Como se crea una lista por comprensión con range y sumando 1
mi_lista = [i + 1 for i in range(8)]
print(mi_lista)

# Como se crea una lista por comprensión con range y multiplicando por 2
mi_lista = [i * 2 for i in range(8)]
print(mi_lista)

# Como se crea una lista por comprensión con range y multiplicando por si mismo
mi_lista = [i * i for i in range(8)]
print(mi_lista)

# Como se crea una lista por comprensión con range y multiplicando por si mismo y sumando 1
mi_lista = [i * i + 1 for i in range(8)]
print(mi_lista)

# Como se crea una lista y se le aplica una función
def sum_five(number):
    return number + 5

mi_lista = [sum_five(i) for i in range(8)]
print(mi_lista)