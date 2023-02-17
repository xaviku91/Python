### Condicionales ###
# En Python, las condiciones se evalúan como True o False.


# Ejemplo 1: edad mayor o menor.

# Pedir al usuario su edad:
'''edad = int(input("¿Cuántos años tienes? ")) 


if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
'''


# Ejemplo 2: Contraseña escrita igual o distinta.
'''contraseña_usuario = int(input("Escribe tu contraseña: ")) 
contraseña_almacenada = contraseña_usuario

print("Tu contraseña ha sido guardada correctamente.")
contraseña_usuario = int(input("Repite tu contraseña: ")) 

print("Vamos a comprobar si has escrito bien tu contraseña.")
if contraseña_almacenada == contraseña_usuario:
    print("Tu contraseña es correcta.")
else:
    print("La contraseña introducida no coincide.")
'''  
# Ahora realizamos el mismo ejercicio anterior, pero cuando la contraseña no coincide, se le pide al usuario que vuelva a escribirla hasta que coincida con un bucle for. Hasta un máximo de 3 errores, si es asi, sale un mensaje la contraseña es incorrecta y se cierra el programa.
'''contraseña_usuario = int(input("Escribe tu contraseña: "))
contraseña_almacenada = contraseña_usuario

print("Tu contraseña ha sido guardada correctamente.")

for i in range(3):
    contraseña_usuario = int(input("Repite tu contraseña: "))
    if contraseña_almacenada == contraseña_usuario:
        print("Tu contraseña es correcta.")
        break
    else:
        print("La contraseña introducida no coincide.")
        if i == 2:
            print("Has superado el número máximo de intentos.")
            print("La contraseña introducida es incorrecta, inténtalo más tarde.")
            break
'''
# Ejemplo 3: Retención de impuestos. Preguntar al usuario cuantos ingresos mensuales tiene y mostrar un mensaje con el porcentaje de retención de impuestos que le corresponde.
ingreso_mensual = int(input("¿Cuál es tu ingreso mensual? "))

if ingreso_mensual > 2000:
    print(f"Tu ingreso mensual tiene un 20% de retención de impuestos.")
elif ingreso_mensual > 1000:
    print(f"Tu ingreso mensual tiene un 10% de retención de impuestos.")
else:
    print(f"Tu ingreso mensual tiene un 5% de retención de impuestos.")

# El f antes del comentario, significa que queremos imprimir un % en la consola, ya que el % es un carácter especial en Python.

# Realizamos el mismo ejercicio pero mostrando las cantidades después del porcentaje de retención de impuestos.
ingreso_mensual = int(input("¿Cuál es tu ingreso mensual? "))

if ingreso_mensual > 2000:
    print(f"Tu ingreso mensual tiene un 20% de retención de impuestos, es decir, ", ingreso_mensual * 0.2, "€.")
elif ingreso_mensual > 1000:
    print(f"Tu ingreso mensual tiene un 10% de retención de impuestos, es decir, ", ingreso_mensual * 0.1, "€.")
else:
    print(f"Tu ingreso mensual tiene un 5% de retención de impuestos, es decir, ", ingreso_mensual * 0.05, "€.")


