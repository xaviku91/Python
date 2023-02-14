### Ejercicios ###

# 1. Crea un programa que pida al usuario dos números y muestre por pantalla la suma, resta, multiplicación, división, división entera y potencia.

print("\n Ejercicio 1 \n")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print("La suma de los dos números es: ", num1 + num2)
print("La resta de los dos números es: ", num1 - num2)
print("La multiplicación de los dos números es: ", num1 * num2)
print("La división de los dos números es: ", num1 / num2)
print("La división entera de los dos números es: ", num1 // num2)
print("La potencia de los dos números es: ", num1 ** num2)

# 2. Crea un programa que pida al usuario dos números y un signo, si el signo es "+" se mostrará la suma de los dos números, si el signo es "-" se mostrará la resta de los dos números, si el signo es "*" se mostrará la multiplicación de los dos números y si el signo es "/" se mostrará la división de los dos números.

print("\n Ejercicio 2 \n")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
signo = input("Introduce el signo: ")
if signo == "+":
    print("La suma de los dos números es: ", num1 + num2)
elif signo == "-":
    print("La resta de los dos números es: ", num1 - num2)
elif signo == "*":
    print("La multiplicación de los dos números es: ", num1 * num2)
elif signo == "/":
    print("La división de los dos números es: ", num1 / num2)
else:
    print("El signo introducido no es válido")

# 3. Igual que antes pero, además en este ejercicio, además, si el usuario introduce un 0 como segundo número, el programa nos dará un error.

print("\n Ejercicio 3 \n")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
signo = input("Introduce el signo: ")
if signo == "+":
    print("La suma de los dos números es: ", num1 + num2)
elif signo == "-":
    print("La resta de los dos números es: ", num1 - num2)
elif signo == "*":
    print("La multiplicación de los dos números es: ", num1 * num2)
elif signo == "/":
    if num2 == 0:
        print("Error, no se puede dividir entre 0")
    else:
        print("La división de los dos números es: ", num1 / num2)
else:
    print("El signo introducido no es válido")

# 4. Crea un programa que pida al usuario un número entero y diga si es par o impar.

print("\n Ejercicio 4 \n")

num = int(input("Introduce un número entero: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
# 5. Crea un programa que pida al usuario un número entero y diga si es positivo o negativo.

print("\n Ejercicio 5 \n")

num = int(input("Introduce un número entero: "))
if num >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")
    
# 6. Crea un programa que pida al usuario un número entero y diga si es múltiplo de 5.

print("\n Ejercicio 6 \n")

num = int(input("Introduce un número entero: "))
if num % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 5")