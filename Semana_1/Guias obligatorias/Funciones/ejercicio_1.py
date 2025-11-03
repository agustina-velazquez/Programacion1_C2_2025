def saludar(nombre:str)->str:
    saludo = print(f"Hola {nombre}!!")
    return saludo

nombre = input("¿Cuál es tu nombre?: ")

saludar(nombre)