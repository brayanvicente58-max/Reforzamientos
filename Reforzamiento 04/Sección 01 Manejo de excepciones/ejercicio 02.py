numeros = [2, 6, 10, 4, 5, 23, 1]


def actualizar_elemento(lista, indice_str, valor_str):
    try:
        # Controlar ValueError si el índice no puede convertirse a entero
        indice = int(indice_str)

        # Controlar IndexError para índices fuera de rango o negativos
        if indice < 0 or indice >= len(lista):
            raise IndexError("El índice está fuera del rango válido de la lista.")

        # Validar que el nuevo valor sea estrictamente un entero (excluyendo booleanos)
        if not isinstance(valor_str, int) or isinstance(valor_str, bool):
            raise TypeError("El nuevo valor debe ser un número entero.")

        # Actualización válida
        lista[indice] = valor_str
        print(f"Lista actualizada con éxito: {lista}")

    except ValueError:
        print("Error: El índice ingresado debe ser un número entero válido.")
    except IndexError as e:
        print(f"Error (IndexError): {e}")
    except TypeError as e:
        print(f"Error (TypeError): {e}")


print("--- PRUEBAS DE ACTUALIZACIÓN DE LISTA ---")
# Actualización válida
print("\nPrueba 1: Válida")
actualizar_elemento(numeros, "2", 99)

# Índice inexistente
print("\nPrueba 2: Índice fuera de rango")
actualizar_elemento(numeros, "10", 50)

# Índice no numérico
print("\nPrueba 3: Índice no numérico")
actualizar_elemento(numeros, "abc", 15)

# Valor no válido (tipo incorrecto)
print("\nPrueba 4: Valor no entero")
actualizar_elemento(numeros, "1", "texto_no_entero")