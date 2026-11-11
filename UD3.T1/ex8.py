contraseña = input("Ingresa tu contraseña: ")

p = (
    "Contrasinal segura" if len(contraseña) >= 8 and not " " in contraseña
    else "Erro: demasiado curta" if len(contraseña) < 8
    else "Erro: non pode conter espazos"
)

print(p)