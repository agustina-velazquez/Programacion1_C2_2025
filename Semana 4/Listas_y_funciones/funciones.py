#opcion 1. Cargar titulos y ejemplares

def cargar_titulos_y_ejemplares(lista_1: list, lista_2: list) -> list:
    seguir_agregando = "Si"
    while seguir_agregando == "Si":
        for i in range(len(lista_1)):
            titulo = input("Ingrese título del libro: ")
            ejemplar = int(input("Ingrese copias disponibles: "))

            lista_1[i] = titulo
            lista_2[i] = ejemplar

            seguir_agregando = input("Desea seguir ingresando libros? Si/No: ")

    return lista_1, lista_2

#opcion 2. Mostrar catalogo completo

def mostrar_catalogo(lista_1: list, lista_2: list)->None:
    for i in range(len(lista_1)):
        print(f"{lista_1[i]} -> {lista_2[i]} copias.")
        
#opcion 3. Consultar disponibilidad

def consultar_disponibilidad(lista_1: list, lista_2: list)->None:
    titulo = input("¿Qué título desea buscar?: ")

    for i in range(len(lista_1)):
        if lista_1[i] == titulo:
            print(f"{titulo} tiene {lista_2[i]} copias")
            break

#opcion 4. Listar titulos agotados

def mostrar_titulos_agotados(lista_1: list, lista_2: list)->None:
    for i in range(len(lista_1)):
        if lista_2[i] == 0:
            if lista_1[i] == "" :
                continue
            else:
                print(f"{lista_1[i]} está agotado.")
        else:
            continue

#opcion 5. Agregar un titulo nuevo

def agregar_stock(lista_1: list, lista_2: list)-> list:

       
    for i in range(len(lista_1)):
        if lista_1[i] != " ":
            continue
        elif lista_1[i] == " ":
            nuevo_libro = input("Ingrese el título del libro: ")
            lista_1[i] = nuevo_libro
            ejemplares = int(input("Número de jemplares del nuevo libro: "))
            lista_2[i] = ejemplares
            break

    return lista_1, lista_2
        
#opcion 6. Actualizar ejemplares. Permtir al usuario modificar el número de ejemplares de un lbro existente.

def actualizar_ejemplares(lista_1:list, lista_2:list)->list:
    titulo = input("Libro a modificar numero de ejemplares: ")
    for i in range(len(lista_1)):
        if lista_1[i] == titulo:
            ejemplares = int(input("Nuevo número de ejemplares: "))
            lista_2[i] = ejemplares
            break
    return lista_2
        