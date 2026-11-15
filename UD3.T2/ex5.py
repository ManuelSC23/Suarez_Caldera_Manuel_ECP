frase = input("Introduce unha frase: ")
lista = [palabra.lower() for palabra in frase.split()]

match lista:
    case ["ola"]:
        print("Saúdos")
    case ["ver", marca]:
        print(f"Buscando {marca.capitalize()}")
    case _:
        print("Non entendo")