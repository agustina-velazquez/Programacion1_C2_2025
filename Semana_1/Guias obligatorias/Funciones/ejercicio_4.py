def buscar_mayor(a, b, c):
    if a > b and a > c: 
        mayor = a
        if b > c:
            medio = b
            menor = c
        else:
            medio = c
            menor = b
    elif b > a and b > c:
        mayor = b
        if a > c:
            medio = a 
            menor = c
        else: 
            medio = c
            menor = a
    else:
        mayor = c
        if b > a:
            medio = b
            menor = a
        else:
            medio = a
            menor = b
    
    return menor, medio, mayor

a = float(input("Ingrese un número: "))

b = float(input("Ingrese un número: "))

c = float(input("Ingrese un número: "))

print(buscar_mayor(a, b ,c))
