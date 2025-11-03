lista_alumnos = [""]*10
lista_libros = [0]*10
lista_comentarios = [""]*10

#---VALIDACIONES---

def validar_texto(texto:str, mensaje)->str:
    while texto == "":
        texto = input(mensaje)
    
    return texto

def validar_numero(numero:int)->int:
    while numero < 1 or numero > 20:
        print("La cantidad de libros leídos debe estar entre 1 y 20.")
        numero = int(input("Ingrese cantidad de libros leídos: "))
    
    return numero

#---FUNCIONES---

def ingresar_datos(personas:list, libros:list, comentarios:list):
    for i in range(len(personas)):
        nombre = validar_texto(input("Ingrese su nombre completo: "), "No puede estar vacío. Ingrese su nombre nuevamente: ")
        cantidad_libros = validar_numero(int(input("Ingrese la cantidad de libros leídos: ")))
        opinion = validar_texto(input("¿Qué le parecieron los libros?: "), "Debe escribir algo. Ingrese su comentario: ")

        personas[i] = nombre
        libros[i] = cantidad_libros
        comentarios[i] = opinion

        seguir = input("¿Desea ingresar otro alummo?(s/n): ").lower()

        if seguir != "s":
            print("No se ingresaran mas datos.")
            break

    return personas, libros, comentarios, 

def mostrar_datos(personas:list, libros:list, comentarios:list)->None:
    for i in range(len(personas)):
        if personas[i] != "":
            print(f"Alumno/a {i+1}.")
            print(f"Nombre completo: {personas[i]}")
            print(f"Cantidad de libros leídos: {libros[i]}")
            print(f"Comentario acerca de los libros leídos: {comentarios[i]}")

        else:
            break

def calcular_promedio(libros:list)->float:
    suma = 0
    for i in range(len(libros)):
        if libros[i] != 0:
            suma += libros[i]
        else:
            promedio = suma / i
            return promedio
    
def ordenar_libros(personas:list, libros:list, comentarios:list):
    tam = len(libros)

    for i in range(tam - 1):
        intercambio = False
        for j in range(tam - i - 1):
            if libros[j] < libros[j + 1]:

                personas[j], personas[j + 1] = personas[j+1], personas[j]
                libros[j], libros[j + 1] = libros[j + 1], libros[j]
                comentarios[j], comentarios[j+1] = comentarios[j+1], comentarios[j]
                
                intercambio = True

        if intercambio == False:
            break
    return personas, libros, comentarios

#---MENÚ---

menu = True

while menu ==  True:
    print("--MENÚ DE OPCIONES--")
    print("1. Ingresar datos de los alumnos.")
    print("2. Mostrar hábitos de lectura.")
    print("3. Ordenar alumnos por cantidad de libros leídos.")
    print("4. Salir.")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print("Comencemos a cargar alumnos y alumnas:")
        ingresar_datos(lista_alumnos, lista_libros, lista_comentarios)
    elif opcion == 2:
        mostrar_datos(lista_alumnos, lista_libros, lista_comentarios)
        promedio = calcular_promedio(lista_libros)
        print(f"Promedio de libros leídos por los alumnos ingresados: {promedio}")
    elif opcion == 3:
        print("Alumnos ordenados según la cantidad de libros que leyeron(de mayor a menor): ")
        ordenar_libros(lista_alumnos, lista_libros, lista_comentarios)
        print(f"Alumnos/as: {lista_alumnos}")
        print(f"Libros leídos: {lista_libros}")
        print(f"Comentarios: {lista_comentarios}")
    elif opcion == 4:
        print("Hasta luego.")
        break
    else:
        print(input("Ingrese una opción válida(1-4): "))



    



