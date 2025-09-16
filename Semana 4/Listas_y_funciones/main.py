from funciones import *


titulos = [" "] * 20
ejemplares = [0] * 20 

print(titulos)
print(ejemplares)

menu = True

while menu == True:
    print("Menú de opciones:")
    print("Opción 1. Cargar titulos y ejemplares.")
    print("Opción 2. Mostrar catalogo completo.")
    print("Opcion 3. Consultar disponibilidad.")
    print("Opción 4. Listar títulos agotados.")
    print("Opción 5. Agregar un nuevo título.")
    print("Opción 6. Actualizar ejemplares(prestamos/devolución).")
    print("Opcion 7. Salir.")

    opcion = int(input("Ingrese su opcion: "))

    match opcion:
        case 1:
            print("Opción 1. Cargar títulos y ejemplares.")
            titulos, ejemplares = cargar_titulos_y_ejemplares(titulos, ejemplares)
            print(f"Lista de títulos: {titulos}")
            print(f"Lista de ejemplares: {ejemplares}")
                    
        case 2:
            print("Opción 2. Mostrar catálogo completo.")
            print("Catálogo:")
            mostrar_catalogo(titulos, ejemplares)
              
        case 3: 
            print("Opción 3. Consultar disponbilidad.")
            consultar_disponibilidad(titulos, ejemplares)
                    
        case 4:
            print("Opción 4. Listar títulos agotados.")
            mostrar_titulos_agotados(titulos, ejemplares)

        case 5:
            print("Opción 5. Agregar un nuevo título.")
            titulos, ejemplares = agregar_stock(titulos, ejemplares)
                   
        case 6:
            print("Opción 6. Actualizar ejemplares(prestamos/devolución).")
            ejemplares = actualizar_ejemplares(titulos, ejemplares)      
        case 7: 
            menu = False