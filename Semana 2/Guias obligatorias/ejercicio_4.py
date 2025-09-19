def buscar_mayor(a:int, b:int, c:int):
    if a >= b and a >= c:
        if b >= c:
            return a,b,c
        else:
            return a,c,b
    elif b >= a and b >= c:
        if a >= c:
            return b, a, c
        else:
            return b, c, a
    else:
        if a >= b:
            return c, a, b
        else:
            return c, b, a
        
numero_a = int(input("Ingrese un número: "))
numero_b = int(input("Ingrese un número: "))
numero_c = int(input("Ingrese un número: "))

mayor , medio , menor = buscar_mayor(numero_a, numero_b, numero_c)

print(f"Numeros ordenados de mayor a menor: {mayor} - {medio} - {menor}")
