class Alumno:
    # Atributos inicializados en el constructor
    def __init__(self, nombre: str, edad: int, nota_final: float):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    # Métodos de información y condición académica (¡Aquí agregamos 'self'!)
    def obtener_condicion(self) -> str:
        if self.nota_final >= 11:
            return "Aprobado"
        return "Desaprobado"

    def mostrar_datos(self):
        print(f"Estudiante: {self.nombre} | Edad: {self.edad} | Nota: {self.nota_final} | Condición: {self.obtener_condicion()}")


# Instanciación y recorrido de lista de alumnos
alumnos_grupo = [
    Alumno("Gabriel", 21, 14.5),
    Alumno("Valeria", 19, 8.0),
    Alumno("Javier", 22, 11.0)
]

print("--- REGISTRO ACADÉMICO ---")
for alumno in alumnos_grupo:
    alumno.mostrar_datos()