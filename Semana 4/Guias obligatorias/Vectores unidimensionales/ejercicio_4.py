enteros = [1] * 8

for i in range(len(enteros)):
    enteros[i] = int(input(f"Ingrese un entero para la posición {i}: "))

mayores = 0 

for i in range(len(enteros)):
    if enteros[i] > 100:
        mayores += 1

print(f"Hay {mayores} enteros mayores a 100")