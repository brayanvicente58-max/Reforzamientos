class Trabajador:
    def __init__(self, nombre, sueldo, meses_antiguedad):
        self.nombre = nombre
        self.sueldo = sueldo
        self.meses_antiguedad = meses_antiguedad


def evaluar_prestamo(trabajador, monto_solicitado):
    try:
        if not isinstance(monto_solicitado, (int, float)) or monto_solicitado <= 0:
            raise ValueError("El monto solicitado debe ser un número positivo.")

        # Regla: Préstamo máximo de hasta 3 veces el sueldo y mínimo 6 meses de antigüedad
        if trabajador.meses_antiguedad < 6:
            raise Exception("El trabajador no cumple con el tiempo mínimo de antigüedad (6 meses).")

        if monto_solicitado > (trabajador.sueldo * 3):
            raise Exception("El monto excede el límite máximo permitido (3 veces el sueldo).")

        print(f"¡Préstamo aprobado para {trabajador.nombre} por S/ {monto_solicitado:.2f}!")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Préstamo denegado: {e}")


print("--- SISTEMA DE PRÉSTAMOS ---")
t1 = Trabajador("Ana Gómez", 3000.0, 12)
evaluar_prestamo(t1, 5000.0)  # Válido
evaluar_prestamo(t1, 15000.0)  # Excede límite
evaluar_prestamo(t1, -200)  # Valor negativo