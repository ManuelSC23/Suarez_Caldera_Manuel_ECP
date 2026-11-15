color = input("Introduce unha cor: ")

color = color.lower()

match color:
    case "vermello":
        print("Parar")
    case "amarelo":
        print("Precaución")
    case "verde":
        print("Pasar")
    case "azul":
        print("Erro")
    case "Verde":
        print("Pasar")
    case _:
        print("Erro")
   