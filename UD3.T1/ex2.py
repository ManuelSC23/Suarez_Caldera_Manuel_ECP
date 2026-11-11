producto = ("Portátil", 10, 599.99, "Almacén A", "Pasillo 3")

nombre, cantidad, precio, *ubicacion = producto

precio *= 1.1

if (p:= cantidad * precio) > 5000:
    print(p)
