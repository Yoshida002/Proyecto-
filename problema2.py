# Programa para calcular el promedio de 4 calificaciones de diferentes materias

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def obtener_datos():
    materias = []
    calificaciones = []
    for i in range(1, 5):
        materia = input(f"Introduce el nombre de la materia {i}: ")
        materias.append(materia)
        while True:
            try:
                calificacion = float(input(f"Introduce la calificación para {materia}: "))
                calificaciones.append(calificacion)
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
    return materias, calificaciones

def main():
    materias, calificaciones = obtener_datos()
    promedio = calcular_promedio(calificaciones)
    print(f"El promedio de las calificaciones para las materias {', '.join(materias)} es: {promedio}")

if __name__ == "__main__":
    main()
