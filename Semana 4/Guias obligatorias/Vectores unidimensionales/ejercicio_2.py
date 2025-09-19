array = [1]*10

for i in range (len(array)):
    array[i] = int(input(f"Ingrese un entero para la posicion {i}: "))


suma = 0

for i in range(len(array)):
    suma += array[i]

print(f"La suma de sus elementos es: {suma}")

