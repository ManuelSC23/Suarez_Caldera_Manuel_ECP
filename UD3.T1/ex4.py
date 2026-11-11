t = int(input("Ingresa la temperatura: "))

mensaje = (
    "Acendendo calefacción" if t < 10
    else "Temperatura ideal" if t <= 25
    else "Acendendo aire acondicionado"
)

print(mensaje)

# mensaje = ""

# match t:
#     case t if t < 10:
#         mensaje = "Acendendo calefacción"
#     case t if t >= 10 and t <= 25:
#         mensaje = "Temperatura ideal"
#     case _:
#         mensaje = "Acendendo aire acondicionado"