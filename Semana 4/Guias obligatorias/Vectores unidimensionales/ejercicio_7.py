enteros =  [1]*7

for i in range(len(enteros)):
    enteros[i] = int(input(f"Ingrese un entero para la posición {i}: "))

for i in range(len(enteros)-1, -1, -1):
    print(enteros[i])

