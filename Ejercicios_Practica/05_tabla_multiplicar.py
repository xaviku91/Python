# Pide al usuario un numero para multiplicarlo en la tabla de multiplicaciones.
numero = int(input("Ingrese un número: "))

print("Tabla de multiplicar en el for")
for i in range(0, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

# Este programa es lo mismo que realizar un for de 0 a 10, pero con un while
print("Tabla de multiplicar en el while")
numero = int(input("Ingrese un número: "))
b = 0
while b <= 10:
  resultado2 = numero * b
  print(numero, "x", b, "=", resultado2)
  b += 1