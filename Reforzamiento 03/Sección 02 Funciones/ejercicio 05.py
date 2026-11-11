# Función para eliminar la primera aparición sin modificar la lista original
def eliminar_primer_valor(lista_original: list, valor: int) -> list:
    nueva_lista = lista_original.copy()
    if valor in nueva_lista:
        nueva_lista.remove(valor)
    return nueva_lista

# Lista inicial
numeros = [5, 12, 25, 12, 40]

# Pruebas con un valor existente y uno inexistente
val_existente = 12
val_inexistente = 99

resultado_1 = eliminar_primer_valor(numeros, val_existente)
resultado_2 = eliminar_primer_valor(numeros, val_inexistente)

print(f"Lista original: {numeros}")
print(f"\nPrueba 1 (Eliminar {val_existente}): {resultado_1}")
print(f"Prueba 2 (Eliminar {val_inexistente}): {resultado_2}")
print(f"Comprobación de la lista original intacta: {numeros}")