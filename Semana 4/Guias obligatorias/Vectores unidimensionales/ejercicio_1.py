array = [1]*5

for i in range (len(array)):
    array[i] = int(input(f"Ingrese un entero para la posicion {i}: "))
    
for i in range(len(array)):
    print(f"El elemento en la posicoion {i} es: {array[i]}")

