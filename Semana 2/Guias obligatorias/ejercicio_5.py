def es_par(numero:int)->bool:
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Ingrese un número: "))

print(es_par(numero))