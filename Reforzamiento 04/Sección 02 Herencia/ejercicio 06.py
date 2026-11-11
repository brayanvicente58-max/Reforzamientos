class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo_final(self):
        return self.sueldo_base

    def mostrar_datos(self, modalidad):
        print(f"Empleado: {self.nombre} | Modalidad: {modalidad} | Sueldo Base: S/ {self.sueldo_base:.2f} | Sueldo Final: S/ {self.calcular_sueldo_final():.2f}")

class EmpleadoTiempoCompleto(Empleado):
    def calcular_sueldo_final(self):
        # Bonificación del 15%
        return self.sueldo_base * 1.15

    def mostrar(self):
        super().mostrar_datos("Tiempo Completo")

class EmpleadoMedioTiempo(Empleado):
    def calcular_sueldo_final(self):
        # Bonificación del 5%
        return self.sueldo_base * 1.05

    def mostrar(self):
        super().mostrar_datos("Medio Tiempo")

print("--- CÁLCULO DE BONIFICACIONES ---")
equipo = [
    EmpleadoTiempoCompleto("Carlos Ruiz", 4000.0),
    EmpleadoTiempoCompleto("Lucía Méndez", 5200.0),
    EmpleadoMedioTiempo("Pedro Salas", 1800.0),
    EmpleadoMedioTiempo("Sofía Vargas", 2100.0)
]

for emp in equipo:
    emp.mostrar()