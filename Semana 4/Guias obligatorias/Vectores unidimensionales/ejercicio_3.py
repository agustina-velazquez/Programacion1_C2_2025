array_reales = [1.0]*6

for i in range (len(array_reales)):
    array_reales[i] = float(input(f"Ingrese un número real para la posicion {i}: "))

suma = 0

for i in range(len(array_reales)):
    suma += array_reales[i]

promedio = suma / len(array_reales)

print(f"El promedio de los valores del array reales es: {promedio}")
