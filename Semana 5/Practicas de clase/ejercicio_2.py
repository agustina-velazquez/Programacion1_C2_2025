#Ejercicio 2: Puntajes de un Torneo
#En un torneo de programación hay 4 equipos que compiten en 5 rondas.
#Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#    El puntaje total de cada equipo.
#    Qué equipo obtuvo el mayor puntaje en total.

equipos = ["equipo 1", "equipo 2", "equipo 3", "equipo 4"]
rondas = [1, 2, 3, 4, 5]

puntajes = [[0,0,0,0,0], #equipo 1
            [0,0,0,0,0], #equipo 2
            [0,0,0,0,0], #equipo 3
            [0,0,0,0,0]  #equipo 4
            ]

def cargar_matriz(mat,filas,columnas)->None:
    for i in range(filas):
        print(f"Equipo {i+1}")
        for j in range(columnas):
            print(f"Ronda {j+1}")
            mat[i][j]= int(input(f"Ingrese el puntaje obtenido: "))

cargar_matriz(puntajes, 4,5)
