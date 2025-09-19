array_1 = [0]*5
array_2 = [0]*5

for i in range(len(array_1)):
    array_1[i] = int(input(f"Ingrese un entero para la posición {i} del array 1: "))

for i in range(len(array_2)):
    array_2[i] = int(input(f"Ingrese un entero para la posición {i} del array 2: "))

iguales = True

for i in range(5):
    if array_1[i] != array_2[i]:
        iguales = False
        print("Ambos arrays no son iguales.")
        break
    
if iguales == True:
    print("Los arrays son iguales.")