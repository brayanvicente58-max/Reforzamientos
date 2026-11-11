# Diccionario de estudiantes y notas
notas = {"Carlos": 15, "Elena": 9, "Sofia": 19, "Mateo": 7, "Lucía": 13}

print("--- Estudiantes registrados ---")
for estudiante, nota in notas.items():
    print(f"{estudiante}: {nota}")

# Identificar aprobados (nota >= 11) y desaprobados
aprobados = []
desaprobados_count = 0
suma_notas = 0
nota_maxima = -1
estudiante_top = ""

for estudiante, nota in notas.items():
    suma_notas += nota

    if nota >= 11:
        aprobados.append(estudiante)
    else:
        desaprobados_count += 1

    if nota > nota_maxima:
        nota_maxima = nota
        estudiante_top = estudiante

# Cálculos de promedio y nota más alta
promedio = suma_notas / len(notas)

print(f"\nEstudiantes aprobados: {', '.join(aprobados)}")
print(f"Promedio general: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima} ({estudiante_top})")
# Cantidad de desaprobados
print(f"Estudiantes desaprobados: {desaprobados_count}")