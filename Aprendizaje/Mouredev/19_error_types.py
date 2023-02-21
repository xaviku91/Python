### Error Types ###

# 1. Syntax Error (Error de sintaxis)
#print "Hola Mundo" #No se puede usar print sin paréntesis en python 3

# 2. Name Error (No existe la variable hola en el programa)
#print(hola) #No existe la variable hola en el programa

# 3. Type Error (No se puede sumar un string con un int)
#print("Hola" + 5) #No se puede sumar un string con un int

# 4. Index Error (No existe el índice 3 en la lista)
#mi_lista = [1, 2, 3]
#print(mi_lista[3]) #No existe el índice 3 en la lista

# 5. Key Error (No existe la clave edad en el diccionario)
#mi_diccionario = {"nombre": "Xavi", "apellido": "Quesada"}
#print(mi_diccionario["edad"]) #No existe la clave edad en el diccionario

# 6. Attribute Error (No se puede añadir elementos a una tupla)
#mi_tupla = (1, 2, 3)
#mi_tupla.append(4) #No se puede añadir elementos a una tupla

# 7. Value Error (No se puede convertir un string a int)
#int("Hola") #No se puede convertir un string a int

# 8. Zero Division Error (División entre 0)
#print(5 / 0) #No se puede dividir entre 0

# 9. Import Error   (No existe el módulo hola)
#import hola #No existe el módulo hola

# 10. Indentation Error (Error de indentación)
#if True:
#print("Hola") #Error de indentación

# 11. EOF Error (EOF indica que el intérprete de Python no pudo completar el análisis del código debido a una terminación prematura)
#print("Hola mundo!"

# 12. KeyboardInterrupt (Ctrl + C para salir de un bucle infinito)
#Ejemplo de KeyboardInterrupt:
#while True:
    #pass

# 13. Not Implemented Error
#def mi_funcion():
    #pass #Para indicar que no se ha implementado nada

# 14. AssertionError (Se utiliza para comprobar que una condición se cumple)
#Ejemplo:
#def suma(num1, num2):
    #assert num1 > 0 and num2 > 0, "Los números deben ser positivos"
    #return num1 + num2
#print(suma(5, -6))
#print(suma(5, 6))

# 15. Overflow Error (Error de desbordamiento)
# Cuando se intenta convertir un número demasiado grande a un tipo de dato numérico, se produce un error de desbordamiento. 
# Por ejemplo, si intentamos convertir
# 999 a un entero, Python nos dará un error de desbordamiento.
# Por ejemplo:
# >>> 999999 ** 999999  # 999999 elevado a 999999

# 16. Floating Point Error (Error de punto flotante)
# ocurre cuando se intenta realizar una operación con números de punto flotante que resulta en un valor indefinido, como la división por cero o el cálculo de una raíz cuadrada de un número negativo. 
# Este tipo de error también se conoce como un error de precisión.
# Ejemplo:
#x = 1.0 / 0.0
#print(x)

# 17. Unbound Local Error (Variable local no asignada)
# Se produce cuando se intenta acceder a una variable local en una función o método, pero no se ha asignado un valor a esa variable.
# Ejemplo:
#def mi_funcion():
    #print(x)
#mi_funcion()
