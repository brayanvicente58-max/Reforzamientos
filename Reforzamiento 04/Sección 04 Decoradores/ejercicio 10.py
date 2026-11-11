def decorador_multiplicacion(func):
    def envoltura(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return envoltura

@decorador_multiplicacion
def multiplicar_seis(a, b, c, d=1, e=1, f=1):
    return a * b * c * d * e * f

print("--- PRUEBAS DE DECORADOR DE MULTIPLICACIÓN ---")
# 3 ejecuciones con valores distintos
print("\nEjecución 1:")
res1 = multiplicar_seis(2, 3, 4, d=2, e=1, f=1)
print(f"Resultado: {res1}")

print("\nEjecución 2:")
res2 = multiplicar_seis(1, 1, 1, d=5, e=5, f=2)
print(f"Resultado: {res2}")

print("\nEjecución 3:")
res3 = multiplicar_seis(3, 3, 2, d=2, e=2, f=2)
print(f"Resultado: {res3}")