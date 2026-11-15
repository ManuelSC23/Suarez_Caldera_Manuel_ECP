try:
    numero = int(input("Introduce un número enteiro: "))

    match numero:
        case n if n < 0:
            print("Negativo")
        case 0:
            print("Cero")
        case n if 0 < n <= 10:
            print("Unidade")
        case n if 11 <= n <= 99:
            print("Decena")
        case n if n > 99:
            print("Centena")
            
except (ValueError, TypeError):
    print("Erro")