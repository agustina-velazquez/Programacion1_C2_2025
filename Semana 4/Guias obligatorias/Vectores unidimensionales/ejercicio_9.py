enteros = [1]*10

for i in range(len(enteros)):
    enteros[i] = int(input(f"Ingrese un entero para la posición {i}: "))

for i in range(len(enteros)):
    if enteros[i] % 2 == 0:
        enteros[i] = 0

print(enteros)