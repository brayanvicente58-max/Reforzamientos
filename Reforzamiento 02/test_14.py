estudiantes = ['Ana', 'Pedro', 'Luis', 'María', 'Carlos']
print("Lista original:", estudiantes)

estudiante_buscado = "Luis"
print("Estudiante buscado:", estudiante_buscado)

if estudiante_buscado in estudiantes:
    estudiantes.remove(estudiante_buscado)
    print("Resultado: Estudiante eliminado correctamente.")
else:
    estudiantes.append(estudiante_buscado)
    print("Resultado: Estudiante no encontrado, agregado al final.")

nuevo_estudiante = "Rosa"
estudiantes.insert(1, nuevo_estudiante)
print("Nuevo estudiante insertado:", nuevo_estudiante)

print("Lista actualizada:", estudiantes)
print("Cantidad de estudiantes:", len(estudiantes))