def conteo_parametros(func):
    def envoltura(*args, **kwargs):
        total_args = len(args) + len(kwargs)
        print(f"[Decorador] Cantidad total de argumentos recibidos: {total_args}")

        # Validar que todos sean enteros estrictos (excluyendo booleanos)
        for arg in args:
            if not isinstance(arg, int) or isinstance(arg, bool):
                print("Solo se admiten números enteros. No se podrá realizar la suma")
                print("La función decoradora terminó de ejecutarse correctamente")
                return None

        for val in kwargs.values():
            if not isinstance(val, int) or isinstance(val, bool):
                print("Solo se admiten números enteros. No se podrá realizar la suma")
                print("La función decoradora terminó de ejecutarse correctamente")
                return None

        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado

    return envoltura


@conteo_parametros
def sumar_enteros(*args, **kwargs):
    suma = sum(args) + sum(kwargs.values())
    return suma


print("--- PRUEBAS DE CONTEO Y VALIDACIÓN ---")
print("\nPrueba 1: Solo posicionales válidos")
print(f"Suma: {sumar_enteros(10, 20, 30)}")

print("\nPrueba 2: Combinación de *args y **kwargs")
print(f"Suma: {sumar_enteros(5, 10, x=15, y=20)}")

print("\nPrueba 3: Caso con valor no válido (booleano/decimal)")
print(f"Suma: {sumar_enteros(5, 10, True)}")