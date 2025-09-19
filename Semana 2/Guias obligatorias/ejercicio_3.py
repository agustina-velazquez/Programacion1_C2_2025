def area_triangulo(base:float, altura:float)->float:
    area = (base * altura)/2
    return area

base = float(input("Base: "))
altura = float(input("Altura: "))

area = area_triangulo(base, altura)
print(f"El área del triangulo es: {area}")