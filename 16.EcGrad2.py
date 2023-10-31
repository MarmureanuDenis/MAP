import math

# Pentru ax^2+bx+c=0
a = float(input("Introduceți coeficientul a: "))
b = float(input("Introduceți coeficientul b: "))
c = float(input("Introduceți coeficientul c: "))

# Calculăm discriminantul
D = b**2 - 4*a*c

# Verificăm valorile discriminantului
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Ecuația are două rădăcini reale distincte: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x1 = -b / (2*a)
    print(f"Ecuația are o rădăcină reală dublă: x1 = {x1}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(D)) / (2*a)
    print(f"Ecuația are două rădăcini complexe conjugate: x1 = {real_part} + {imaginary_part}i și x2 = {real_part} - {imaginary_part}i")
