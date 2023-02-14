import random

# Se cargan las palabras desde el archivo palabras.py
from palabras import words

# Se carga la representación visual de las vidas desde el archivo ahorcado_visual
from ahorcado_visual import vidas_visual_dict

# Se selecciona una palabra al azar
palabra = random.choice(words)

# Se inicializa la variable "vidas"
vidas = 6

# Se inicializa la variable "adivinadas" como una lista de guiones bajos
adivinadas = ["_" for letra in palabra]

# Se inicializa la variable "letras_incorrectas" como una lista vacía
letras_incorrectas = []

# Bucle principal del juego
while "_" in adivinadas and vidas > 0:
    # Se imprimen las letras adivinadas y las letras incorrectas
    print(" ".join(adivinadas))
    print("Letras incorrectas: ", letras_incorrectas)
    print(vidas_visual_dict[vidas])

    # Se solicita al usuario que adivine una letra
    adivinanza = input("Adivina una letra: ").lower()

    # Se verifica si la letra ha sido adivinada correctamente
    if adivinanza in palabra:
        # Se actualizan las letras adivinadas
        for i in range(len(palabra)):
            if palabra[i] == adivinanza:
                adivinadas[i] = adivinanza
    else:
        # Se decrementa la cantidad de vidas restantes
        vidas -= 1
        letras_incorrectas.append(adivinanza)

# Se verifica si el usuario ganó o perdió
if "_" not in adivinadas:
    print("Felicidades, ganaste! La palabra era: ", palabra)
else:
    print("Lo siento, perdiste. La palabra era: ", palabra)