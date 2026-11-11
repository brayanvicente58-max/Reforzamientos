def division_segura(a, b):
    # Realiza la división segura entre dos valores
    return a / b

# Pruebas múltiples para asegurar que el programa continúe tras cada error
pruebas = [("10", "2"), ("10", "0"), ("diez", "2")]

print("--- PRUEBAS DE DIVISIÓN SEGURA ---")
for val1, val2 in pruebas:
    print(f"\nIntentando dividir: {val1} entre {val2}")
    try:
        # Conversión protegida por manejo de excepciones
        num1 = float(val1)
        num2 = float(val2)
        resultado = division_segura(num1, num2)
        print(f"Resultado exitoso: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")
    finally:
        print("Operación finalizada.")