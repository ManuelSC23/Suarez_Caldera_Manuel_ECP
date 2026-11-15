orde = input("Introduce unha orde: ")
ordeLimpia = orde.strip().lower()

match orde:
    case "start":
        print("Iniciando sistema...")
    case "stop":
            print("Detendo sistema...")
    case "axuda" | "help":
            print("Lista de comandos: start, stop, restart")
    case "restart":
            print("Reiniciando...")
    case _:
            print(f"Comando {ordeLimpia} non recoñecido")