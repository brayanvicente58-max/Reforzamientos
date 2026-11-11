departamentos = ['Lima', 'Cusco', 'Arequipa', 'Piura', 'Ica', 'Puno']

print("Lista original:", departamentos)

depto_a_buscar = "Piura"
print("Departamento a reemplazar:", depto_a_buscar)
nuevo_depto = "Tacna"
print("Nuevo departamento:", nuevo_depto)
if depto_a_buscar in departamentos:
    indice = departamentos.index(depto_a_buscar)
    departamentos[indice] = nuevo_depto
else:
    print(f"El departamento '{depto_a_buscar}' no fue encontrado.")

print("Lista actualizada:", departamentos)
print("Cantidad de departamentos:", len(departamentos))