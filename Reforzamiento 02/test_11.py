estudiantes = []

cantidad_estudiantes = 4

estudiante_1 = "Lucía"
estudiante_2 = "Mateo"
estudiante_3 = "Valentina"
estudiante_4 = "Carlos"

estudiantes.append(estudiante_1)
estudiantes.append(estudiante_2)
estudiantes.append(estudiante_3)
estudiantes.append(estudiante_4)

print("Estudiantes: ",estudiantes)

total_estudiantes = len(estudiantes)
print("total de estudiantes registrados: ",total_estudiantes)

if total_estudiantes == cantidad_estudiantes:
    print("¿Coincide con la cantidad prevista?: Si")
else:
    print("La cantidad de estudiantes no coincide.")

print("Primer estudiante: "f"{estudiantes[0]}")
print("Último estudiante: "f"{estudiantes[-1]}")
print("Orden invertido: "f"{estudiantes[::-1]}")
