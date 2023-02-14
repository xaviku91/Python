### Operadores aritméticos ###

a = 4
b = 2
suma = a + b
resta = a - b
multi = a * b
div = a / b
exponente = a ** b
divmod = a % b
div_baja = a // b

print(suma)
print(resta) 
print(multi)
print(div)
print(exponente)
print(divmod) # Muestra el resto de la división (0 o 1)
print(div_baja) # Muestra el resultado de la división pero sin decimales (redondea hacia abajo)

print(type(div)) # Muestra el tipo de dato de la variable , en este caso de "div"

### Operadores de asignación ###

a = 4 # Asigna el valor 4 a la variable "a"
a += 2 # Suma 2 a la variable "a" y lo asigna a la misma variable
print(a)

a -= 2 # Resta 2 a la variable "a" y lo asigna a la misma variable
print(a)

a *= 2 # Multiplica por 2 a la variable "a" y lo asigna a la misma variable
print(a)

a /= 2 # Divide entre 2 a la variable "a" y lo asigna a la misma variable
print(a)

a %= 2 # Divide entre 2 a la variable "a" y asigna el resto a la misma variable
print(a)

a //= 2 # Divide entre 2 a la variable "a" y asigna el resultado sin decimales a la misma variable
print(a)

a **= 2 # Eleva a 2 la variable "a" y lo asigna a la misma variable
print(a)

### Operadores de comparación ###
# Devuelven un valor booleano (True o False)
a = 4
b = 2
a == b # == Comprueba si dos valores son iguales
a != b # != Comprueba si dos valores son diferentes
a > b # Comprueba si el valor de la izquierda es mayor que el de la derecha
a < b # Comprueba si el valor de la izquierda es menor que el de la derecha
a >= b # Comprueba si el valor de la izquierda es mayor o igual que el de la derecha
a <= b # Comprueba si el valor de la izquierda es menor o igual que el de la derecha

print("A es igual que B?", a == b)
print("A es diferente de B?", a != b)
print("A es mayor que B?", a > b)
print("A es menor que B?", a < b)
print("A es mayor o igual que B?", a >= b)
print("A es menor o igual que B?", a <= b)

# Otros ejemplos con strings
a = "Hola"
b = "Hola"
c = "hola"
print("A es igual a B? : ", a == b)
print("A es igual a C? : ", a == c)
print("A es diferente de C? : ", a != c)

### Operadores lógicos ###
# Devuelven un valor booleano (True o False)

a = True
b = False
a and b # and Devuelve True si los dos valores son True
a or b # or Devuelve True si al menos uno de los dos valores es True
not a # not Invierte el valor de la variable (True a False y viceversa)

print("A y B son true? ", a and b)
print("A o B son true? ", a or b)
print("A No es true? ", not a)
print("B No es true? ", not b)

### Operadores de identidad ###
# Devuelven un valor booleano (True o False)

a = 4
b = 2
a is b # is, Comprueba si dos variables son iguales
a is not b # is not, Comprueba si dos variables son diferentes (no son iguales)

print("A es igual a B? ", a is b)
print("A es diferente de B? ", a is not b)

### Operadores de pertenencia ###
# Devuelven un valor booleano (True o False)

a = "Hola"
b = "Hola mundo"
a in b # in, Comprueba si un valor está contenido en otro
a not in b # not in, Comprueba si un valor no está contenido en otro

print("A está en B? ", a in b)
print("A no está en B? ", a not in b)
print("B está en A? ", b in a)
print("B no está en A? ", b not in a)

### Operadores de bits ###
# Devuelven un valor entero

a = 4
b = 2

# AND, Devuelve 1 si los dos bits son 1, de lo contrario devuelve 0
result = a & b 
print("Resultado de la operación AND:", result)

# OR, Devuelve 1 si al menos uno de los dos bits es 1, de lo contrario devuelve 0
result = a | b
print("Resultado de la operación OR:", result)

# NOT, Invierte los bits
result = ~a
print("Resultado de la operación NOT:", result)

# XOR, Devuelve 1 si los dos bits son diferentes
result = a ^ b
print("Resultado de la operación XOR:", result)

# Desplazamiento a la izquierda, Desplaza los bits de la variable a la izquierda tantas veces como indique el valor de la variable de la derecha
result = a << b
print("Resultado de la operación de desplazamiento a la izquierda:", result)

# Desplazamiento a la derecha, Desplaza los bits de la variable a la derecha tantas veces como indique el valor de la variable de la derecha
result = a >> b
print("Resultado de la operación de desplazamiento a la derecha:", result)

# Operadores de incremento y decremento
a = 4
a += 1 # Incrementa en 1 la variable "a"
print(a)

a -= 1 # Decrementa en 1 la variable "a"
print(a)