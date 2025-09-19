def operaciones(num1:float, num2:float)->None:
    print(f"La suma entre los números es: {num1 + num2}")
    print(f"La resta entre los números es: {num1 - num2}")
    print(f"La multiplicación entre los números es: {num1 * num2}")

numero_1 = float(input("Ingrese un número: "))
numero_2 = float(input("Ingrese otro número: "))

operaciones(numero_1, numero_2)