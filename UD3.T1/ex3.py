def permisosParciales(permisos):
    mensaje = "No tiene permisos"
    
    if any(p is True for p in permisos):
        mensaje = "Tiene permisos parciales"
            
    return mensaje

def permisosTotales(permisos):
    mensaje = "El usuario no tiene permiso totales"

    if all(p is True for p in permisos):
        mensaje = "El usuario tiene permiso totales"

    return mensaje

permisos = [True, True, False, True]

print(permisosParciales(permisos))
print(permisosTotales(permisos))

