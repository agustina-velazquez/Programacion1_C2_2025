personas = [""]*10
puntuaciones = [0]*10
comentarios = [""]*10

#----VALIDACIONES----

def validar_nombre(nombre:str)->str:
    while nombre == "":
        print("nombre no puede estar en blanco. Ingrese un dato válido")
        nombre = input("Ingrese nombre y apellido completo: ")

    return nombre

def validar_puntuacion(puntuacion:int)->int:
    while (puntuacion < 1 or puntuacion > 10):
        puntuacion = int(input("La puntuación debe estar entre 1 y 10. Ingrese su puntuación nuevamente: "))

    return puntuacion

def validar_comentario(comentario:str)->str:
    while comentario == "":
        print("El comentario no puede estar en blanco. Ingrese un dato válido")
        comentario = input("Ingrese su comentario: ")

    return comentario

#---FUNCIONES---

def ingresar_datos(nombres:list, puntuaciones:list, comentarios:list)->list:
    
    seguir_ingresando = "s"

    for i in range(len(nombres)):

        if seguir_ingresando == "s":

            nombre_completo = input("Ingrese su nombre completo: ")
            validar_nombre(nombre_completo)
            puntuacion = int(input("Ingrese su puntuación: "))
            validar_puntuacion(puntuacion)
            comentario = input("Ingrese su comentario: ")
            validar_comentario(comentario)

            nombres[i] = nombre_completo
            puntuaciones[i] = puntuacion
            comentarios[i] = comentario

            seguir_ingresando = input("¿Desea ingresar otro participante? (s/n): ")
        else:
            break

    return nombres, puntuaciones, comentarios

def mostrar_datos(nombres:list, puntuaciones:list, comentarios:list)->None:
    for i in range(len(nombres)):
        if nombres[i] != "": 
            print(f"Participante {i+1}:")
            print(f"Nombre y apellido: {nombres[i]} ")
            print(f"Puntuación: {puntuaciones[i]}")
            print(f"Comentario: {comentarios[i]}")
        
        else:
            break

def calcular_promedio(puntuaciones:list)->float:
    suma = 0
    promedio = 0

    for i in range(len(puntuaciones)):
        if puntuaciones[i] != 0:
            suma += puntuaciones[i]
        else: 
            promedio += (suma / i)
            return promedio
        
def bubble_sort_mejorado(puntuaciones:list, nombres: list, comentarios: list)->list:
    tam = len(puntuaciones)

    for i in range(tam - 1):
        intercambio = False
        for j in range(tam - i - 1):
            if puntuaciones[j] > puntuaciones[j + 1]:
                puntuaciones[j], puntuaciones[j + 1] = puntuaciones[j + 1], puntuaciones[j]
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
                comentarios[j], comentarios[j+1] = comentarios[j+1], comentarios[j]
                intercambio = True
        
        if intercambio == False:
            break
    return nombres, puntuaciones, comentarios


#---MENÚ---


while True:

    print("---Menú Encuesta de Satisfacción---")
    print("1. Ingresar datos de los participantes.")
    print("2. Mostrar participantes y promedio.")
    print("3. Ordenar partcipantes por puntuación.")
    print("4. Salir.")

    opcion = int(input("Seleccione una opción(1-4): "))

    if opcion == 1:
        ingresar_datos(personas, puntuaciones, comentarios)
    elif opcion == 2:
        mostrar_datos(personas, puntuaciones, comentarios)
        promedio = calcular_promedio(puntuaciones)
        print(f"Promedio de las puntuaciones: {promedio}")
    elif opcion == 3:
        print("Participantes ordenados de menor a mayor segun su puntuación: ")
        personas, puntuaciones, comentarios = bubble_sort_mejorado(personas, puntuaciones, comentarios)
        print(personas)
        print(puntuaciones)
        print(comentarios)
    elif opcion == 4:
        break
    else:
        print("Opción inválida. Intente nuevamente.")

