cordenada = input("Introduce x e y (separados por espazo): ")
x = int(cordenada.split()[0])
y = int(cordenada.split()[1])

match (x, y):
    case (0,0):
        print("Orixe")
    case (0, _):
        print("Eixo Y")
    case (_, 0):
        print("Eixo X")
    case _:
        print("Cuadrante")