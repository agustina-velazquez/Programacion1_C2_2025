def area_triangulo(base, altura)->float:
    area = (base * altura) / 2
    return area

base = float(input("Base del triangulo: "))
altura = float(input("Altura del triangulo: "))

print(f"El área del triángulo es: {area_triangulo(base, altura)}")