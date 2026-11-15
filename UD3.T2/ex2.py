codigo = int(input("Introduce un código HTTP: "))

match codigo:
    case codigo if codigo >= 100 and codigo <= 199:
        print("Info")
    case codigo if codigo >= 200 and codigo <= 299:
        print("Éxito")
    case codigo if codigo >= 300 and codigo <= 399:
        print("Redireccións")
    case codigo if codigo >= 400 and codigo <= 499:
        print("Erro Cliente")
    case codigo if codigo >= 500 and codigo <= 599:
        print("Erro Servidor")   
    case _:
        print("Descoñecido")
   