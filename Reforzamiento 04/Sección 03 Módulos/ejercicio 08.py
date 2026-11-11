from operaciones import generar_lista, ordenar_lista, obtener_mayor

print("--- ANÁLISIS DE NÚMEROS ALEATORIOS ---")
original = generar_lista()
ordenada = ordenar_lista(original)
mayor = obtener_mayor(original)

print(f"Lista original: {original}")
print(f"Lista ordenada: {ordenada}")
print(f"Número mayor: {mayor}")
print(f"Comprobación (lista original intacta): {original}")