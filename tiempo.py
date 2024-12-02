def calcular_segundos_en_dias(dias):
    # Un día tiene 86400 segundos (24 horas * 60 minutos * 60 segundos)
    segundos_por_dia = 86400
    segundos_totales = dias * segundos_por_dia
    return segundos_totales

# Ejemplo de uso
dias = int(input("Ingrese el número de días: "))
segundos = calcular_segundos_en_dias(dias)
print(f"En {dias} días hay {segundos} segundos.")
