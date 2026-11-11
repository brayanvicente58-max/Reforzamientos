from datetime import datetime


def calcular_antiguedad(fecha_ingreso_str):
    fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%d/%m/%Y")
    fecha_actual = datetime.now()

    # Calcular años completos de servicio
    anios = fecha_actual.year - fecha_ingreso.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day):
        anios -= 1
    return anios


def calcular_aumento(sueldo_actual, anios):
    if anios > 3:
        monto_aumento = sueldo_actual * 0.20
        porcentaje = "20%"
        sueldo_final = sueldo_actual + monto_aumento
    else:
        monto_aumento = 0.0
        porcentaje = "0%"
        sueldo_final = sueldo_actual
    return sueldo_final, monto_aumento, porcentaje


# Pruebas con fechas específicas
empleados_prueba = [
    ("Mario Pérez", 3500.0, "15/05/2018"),  # > 3 años
    ("Karla Gómez", 2800.0, "10/11/2024"),  # < 3 años
    ("Raúl Torres", 4500.0, "01/01/2020")  # > 3 años
]

print("--- CÁLCULO DE ANTIGÜEDAD Y AUMENTOS ---")
fecha_actual_str = datetime.now().strftime("%d/%m/%Y")

for nombre, sueldo, ingreso in empleados_prueba:
    antiguedad = calcular_antiguedad(ingreso)
    sueldo_final, monto_aumento, porc = calcular_aumento(sueldo, antiguedad)

    print(f"\nEmpleado: {nombre}")
    print(f"- Fecha de ingreso: {ingreso}")
    print(f"- Fecha actual: {fecha_actual_str}")
    print(f"- Años de antigüedad: {antiguedad} años")
    print(f"- Sueldo original: S/ {sueldo:.2f}")
    print(f"- Porcentaje aplicado: {porc}")
    print(f"- Monto del aumento: S/ {monto_aumento:.2f}")
    print(f"- Sueldo final: S/ {sueldo_final:.2f}")