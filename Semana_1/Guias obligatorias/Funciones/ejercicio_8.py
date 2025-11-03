def calcular_edad(anio_nacimiento)->int:
    edad_actual =  2025 - anio_nacimiento

    return edad_actual

anio_nacimiento =  int(input("Ingrese su año de nacimiento: "))

print(f"Su edad actual es: {calcular_edad(anio_nacimiento)} años.")