###Variables###

nombre = "Xavi"
bienvenida = "Hola " + nombre + " bienvenido!"
print(bienvenida)

a = 1
b = 2
resultado = a + b
print(resultado)

# Variables 
nombre = True
bienvenida = f"Hola {nombre} como estas"
del nombre # Borrar nombre no afecta al print de bienvenida siguiente ya que la variable existe antes de borrar nombre
print(bienvenida)

print("Hola" in bienvenida) # True porque si existe en bienvenida
print("Adiós" in bienvenida) # False porque no existe en bienvenida
