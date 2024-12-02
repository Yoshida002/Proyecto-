import math

def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# Ejemplo de uso
print("Ingrese las coordenadas del primer punto (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Ingrese las coordenadas del segundo punto (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = calcular_distancia(x1, y1, x2, y2)
print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es {distancia:.2f}")
