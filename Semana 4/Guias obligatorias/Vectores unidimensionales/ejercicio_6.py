array =  [1]*7

for i in range(len(array)):
    array[i] = int(input(f"Ingrese un entero para la posición {i}: "))

maximo = array[0]
posicion = 0

for i in range(1,len(array)):
   
    if array[i] > maximo:
        maximo = array[i]
        posicion = i


print(f"El valor más alto en el array es el número {maximo}")
print(f"Se encuentra en la posición {posicion}")