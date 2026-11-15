datos = input("Introduce unha lista: ")
lista = eval(datos)

match len(lista):
    case 0:
        print("Baleira")
    case 1:
        print("Un")
    case 2:
        print("Dous")
    case _: 
        print("Moitos")
