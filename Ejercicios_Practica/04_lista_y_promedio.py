# Pide al usuario insertar 5 números y con ellos crea una lista de números y realiza la suma y promedio de ellos.

numeros = []
for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

suma = 0
for numero in numeros:
    suma += numero

promedio = suma / len(numeros)

print("La suma de los números es:", suma)
print("El promedio de los números es:", promedio)