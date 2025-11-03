def verificar_acceso(edad)->bool:
    if edad >= 18:
        return True
    else:
        return False
    
edad = int(input("Ingrese su edad: "))

if verificar_acceso(edad):
    print("Es mayor de edad.")
else: 
    print("Es menor de edad.")