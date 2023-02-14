### Clases - Classes ###

# Una clase es un molde para crear objetos
class MiPersona:
  pass

print(MiPersona)
print(MiPersona())

# Podemos crear una clase con atributos
class PersonaUno:
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

# Imprimir un atributo de la clase "Persona" en este caso el nombre
mi_persona_uno = PersonaUno("Juan", "Pérez", 35)
print(mi_persona_uno.nombre)

# Imprimir los atributos de la clase "Persona"
print(f"Nombre: {mi_persona_uno.nombre}, Apellido: {mi_persona_uno.apellido}, Edad: {mi_persona_uno.edad}")

# Tambien podríamos crear los argumentos nosotros directamente en la clase
class Otra_Persona:
  def __init__(self):
    self.nombre = "Xavi"
    self.apellido = "Quesada"
nueva_persona = Otra_Persona()
print(nueva_persona.nombre)

# Podemos crear una clase con métodos
class persona_nueva:
  def __init__(self, nombre, apellido):
    self.completo = f" Te llamas {nombre} y tú apellido es {apellido}"
person_new = persona_nueva("Xavi", "Quesada")
print(person_new.completo)

# Crear una clase con métodos y atributos y llamarlos desde el objeto creado
class Persona:
  def __init__(self, nombre, apellido):
    self.full_name = f"{nombre} {apellido}"
  def caminar(self):
    print(f"{self.full_name}, está caminando")
  def dormir(self):
    print(f"{self.full_name}, está durmiendo")

mi_persona = Persona("Bob", "Esponja")
mi_persona.caminar()
mi_persona.dormir()

# Podemos cambiar el valor de un atributo
mi_persona.full_name = "Leo Messi"
mi_persona.caminar()

# Podemos crear lo mismo incluyendo el alias de la clase
class Persona_alias:
  def __init__(self, nombre, apellido, alias = "sin alias"):
    self.nombre_completo = f"{nombre} {apellido} ({alias})"
  def caminar(self):
    print(f"{self.nombre_completo}, está caminando")
  def dormir(self):
    print(f"{self.nombre_completo}, está durmiendo")
    
la_persona = Persona_alias("Petter", "Parker", "Spiderman")
print(la_persona.nombre_completo)
la_persona.caminar()
# Cambiar el valor del alias
la_persona = Persona_alias("Petter", "Parker")
print(la_persona.nombre_completo)

# Podemos crear una clase con atributos privados
class Persona_privada: 
  def __init__(self, nombre, apellido): # Propiedad publica
    self.__nombre_completo = f"{nombre} {apellido}" # Propiedad privada
  def caminar(self):
    print(f"{self.__nombre_completo}, está caminando")
  def dormir(self):
    print(f"{self.__nombre_completo}, está durmiendo")
Person_private = Persona_privada("Carlos", "Diaz")
Person_private.caminar()

print(Person_private.__nombre_completo) # Esto no funciona porque es un atributo privado