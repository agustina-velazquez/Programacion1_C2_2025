enteros = [1,52,4,63,5,7,12,7,9,12]

numero = int(input("¿Qué numero desea buscar?: "))

encontrado = False

for i in range(len(enteros)):
    if enteros[i] == numero:
        print(f"El número buscado se encontró en la posición {i}")
        encontrado = True
        break

if encontrado == False:
    print("El número no se encuentra en el array")
        


        
