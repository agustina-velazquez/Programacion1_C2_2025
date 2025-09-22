#Ejercicio 1: Registro de Temperaturas
#Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios (mañana, tarde y noche).
#Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#   El promedio de temperatura de cada día.
#    El promedio general de toda la semana.


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]
horarios = ["Mañana", "Tarde", "Noche"]

mat = [[0,0,0], #Lunes
       [0,0,0], #Martes
       [0,0,0], #Miercoles
       [0,0,0], #Jueves
       [0,0,0], #Viernes
       [0,0,0], #Sabado
       [0,0,0] #Domingo
       ]

def cargar_matriz(mat,filas,columnas)->None:
    for i in range(filas):
        for j in range(columnas):
            mat[i][j] = int(input(f"Ingrese la temperatura del dia {dias[i]} por la {horarios[j]}: "))

def mostrar_matriz(mat)->None:
    for i in range(len(mat)):
        print(f"Dia {dias[i]}")
        for j in range(len(mat[0])):
            print(f"{horarios[j]}: {mat[i][j]} grados")


def calcular_promedio(mat):

    promedios = [0]*7
    
    for i in range(len(mat)):
        suma = 0

        for j in range(len(mat[0])):
            suma += mat[i][j]

        promedios[i] = suma / 3

    return promedios


cargar_matriz(mat, 7, 3)
mostrar_matriz(mat)

promedios_por_dia = calcular_promedio(mat)

for i in range(len(promedios_por_dia)):
    print(f"El promedio de la temperatura del dia {dias[i]} es: {promedios_por_dia[i]}")

def calcular_promedio_semanal(promedios)->float:
    suma = 0
    for i in range(len(promedios)):
        suma +=  promedios[i]
    promedio_semanal = suma /7

    return promedio_semanal

promedio_semanal = calcular_promedio_semanal(promedios_por_dia)

print(f"El promedio general de toda la semana es: {promedio_semanal}")
