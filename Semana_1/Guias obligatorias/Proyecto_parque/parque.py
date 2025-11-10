

def mostrar_atracciones():
    print("Menú de atracciones:")
    print("1. Montaña rusa")
    print("2. Casa del terror")
    print("3. Carrusel")

def puede_subir(edad, atraccion):
    if atraccion == "Montaña rusa" and edad < 12:
        return False
    if atraccion == "Casa del terror" and edad < 6:
        return False
    
    return True
    
def calcular_precio(atraccion):
    if atraccion == "Montaña rusa":
        precio = 1500
    elif atraccion == "Casa del terror":
        precio = 1200
    elif atraccion == "Carrusel":
        precio = 800

    return precio

def registrar_visita():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    cantidad_atracciones = int(input("Cuántas atracciones desea usar?: "))
    atracciones_elegidas = []
    atracciones_permitidas = []
    total = 0

    for i in range(cantidad_atracciones):
        atraccion = input("Ingrese atracción que desea usar: ")
        atracciones_elegidas+= [atraccion]
        if puede_subir(edad, atraccion):
            atracciones_permitidas += [atraccion]

    for atraccion in atracciones_permitidas:
        total += calcular_precio(atraccion)

    return nombre, edad, atracciones_elegidas, atracciones_permitidas, total

def mostrar_resumen(nombre, edad, elegidas, permitidas, total):
    print(f"Nombre del visitante: {nombre}")
    print(f"Edad: {edad}")
    print(f"Las atracciones que eligio son: {elegidas}")
    print(f"Las atracciones a las que puede subirse son: {permitidas}")
    print(f"El monto total a pagar por las atracciones es: ${total}")


    




     





