def validar_nombre(nombre:str)->str:
    while nombre == "":
        print("nombre no puede estar en blanco. Ingrese un dato válido")
        nombre = input("Ingrese nombre y apellido completo: ")

    return nombre

def validar_puntuacion(puntuacion:int)->int:
    while 0 > puntuacion or puntuacion > 10:
        puntuacion = int(input("La puntuación debe estar entre 1 y 10. Ingrese su puntuación nuevamente: "))

    return puntuacion

def validar_comentario(comentario:str)->str:
    while comentario == "":
        print("El comentario no puede estar en blanco. Ingrese un dato válido")
        comentario = input("Ingrese su comentario: ")

    return comentario

