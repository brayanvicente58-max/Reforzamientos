# Función para calcular el total vendido
def calcular_total(ventas: list) -> float:
    return sum(ventas)

# Función para calcular el promedio diario
def calcular_promedio(ventas: list) -> float:
    return sum(ventas) / len(ventas)

# Funciones para venta máxima y días que superaron el promedio
def obtener_maxima_venta(ventas: list) -> float:
    return max(ventas)

def contar_dias_superan_promedio(ventas: list) -> int:
    prom = calcular_promedio(ventas)
    dias = 0
    for venta in ventas:
        if venta > prom:
            dias += 1
    return dias

# Datos de prueba
ventas_semana = [210, 145, 310, 290, 180, 400, 250]

# Mostrar resultados con descripciones
total = calcular_total(ventas_semana)
promedio = calcular_promedio(ventas_semana)
maxima = obtener_maxima_venta(ventas_semana)
dias_top = contar_dias_superan_promedio(ventas_semana)

print("--- Resumen de Ventas Semanales ---")
print(f"Total vendido: S/ {total:.2f} (Suma acumulada de los 7 días)")
print(f"Promedio diario: S/ {promedio:.2f} (Monto estimado de ventas por día)")
print(f"Venta máxima: S/ {maxima:.2f} (El pico más alto registrado en un día)")
print(f"Días sobre el promedio: {dias_top} días (Días con desempeño superior a la media)")