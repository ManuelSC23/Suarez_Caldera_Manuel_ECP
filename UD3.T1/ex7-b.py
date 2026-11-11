import calendar

año = int(input("Ingresa el año: "))

if calendar.isleap(año):
   print("El año es bisiesto")
else:
    print("El año no es bisiesto")