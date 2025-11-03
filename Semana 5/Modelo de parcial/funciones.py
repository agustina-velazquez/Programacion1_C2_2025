from validaciones import *


def ingresar_datos(nombres:list, puntuaciones:list, comentarios:list)->list:
    
    for i in range(len(nombres)):
        seguir_ingresando = "s"

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
            print(f"Participante {i}:")
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


            




    

        













        
