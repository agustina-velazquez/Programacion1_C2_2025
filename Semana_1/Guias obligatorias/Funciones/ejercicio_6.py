def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

minutos = int(input("Ingrese los minutos a convertir: "))

horas, minutos_restantes = convertir_minutos(minutos)

print(f"Equivale a {horas} horas y {minutos_restantes} minutos.")