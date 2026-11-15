import ast

entrada = input("Introduce un diccionario: ")

# Se a entrada está totalmente baleira ou son só espazos
if not entrada.strip():
    print("Baleira")
else:
    try:
        # Usamos ast.literal_eval que é máis seguro que eval
        diccionario = ast.literal_eval(entrada)
    except (ValueError, SyntaxError):
        diccionario = {}

if isinstance(diccionario, dict) and "status" in diccionario and "data" in diccionario:
    status = diccionario["status"]
    data = diccionario["data"]

    if status == 200 and isinstance(data, list) and len(data) > 0:
        match len(data):
            case 0:
                print("Baleira")
            case 1:
                print(f"Rango: {data[0]} a {data[0]}")
            case _:
                print(f"Rango: {data[0]} a {data[-1]}")
    else:
        print("Erro")
else:
    print("Erro")
