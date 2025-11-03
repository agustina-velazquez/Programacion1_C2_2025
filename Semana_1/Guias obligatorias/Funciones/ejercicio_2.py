def operaciones(num1:int, num2:int)->int:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    return suma, resta, multiplicacion

a =  int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

print(operaciones(a,b))