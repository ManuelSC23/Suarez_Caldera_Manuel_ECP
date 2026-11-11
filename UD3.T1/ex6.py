salario = int(input("Ingresa tu salario: "))
antiguedad = int(input("Ingresa tu antiguedad laboral: "))

p = (
    "Crédito APROBADO" if salario > 1500 and antiguedad >= 2
    else "Ingresos insuficientes" if salario <= 1500
    else "Antigüidade insuficiente"
)

print(p)