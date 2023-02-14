# Formula Cuadrática🧮

a = int(input("Inserta A: "))
b = int(input("Inserta B: "))
c = int(input("Inserta C: "))

raiz1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
raiz2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(raiz1)
print(raiz2)