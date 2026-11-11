resultado = True

while resultado:
    try:
        edad = int(input("Ingresa tu edad: "))
        resultado = False
    except ValueError:
        print("Idades incorrectas")

p = (
    0 if edad < 5
    else 5 if edad >= 5 and edad <= 17
    else 10 if edad >= 18 and edad <= 64
    else 7
)

print(p)