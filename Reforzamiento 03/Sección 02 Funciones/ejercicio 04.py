# Función para calcular la suma de los dígitos de un número entero positivo
def sumar_digitos(numero: int) -> int:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

# Análisis de dos números predefinidos
num1 = 742
num2 = 135

suma_num1 = sumar_digitos(num1)
suma_num2 = sumar_digitos(num2)

print(f"Número 1: {num1} | Suma de dígitos: {suma_num1}")
print(f"Número 2: {num2} | Suma de dígitos: {suma_num2}")

# Comparación de sumas
if suma_num1 > suma_num2:
    print(f"El número {num1} tiene la mayor suma de dígitos.")
elif suma_num2 > suma_num1:
    print(f"El número {num2} tiene la mayor suma de dígitos.")
else:
    print("Existe un empate en la suma de dígitos.")

# Verificar cuáles tienen una suma de dígitos menor que 10
print("\n--- Evaluación (Suma menor a 10) ---")
if suma_num1 < 10:
    print(f"- {num1} tiene una suma menor a 10 ({suma_num1})")
if suma_num2 < 10:
    print(f"- {num2} tiene una suma menor a 10 ({suma_num2})")
if suma_num1 >= 10 and suma_num2 >= 10:
    print("Ninguno de los dos números tiene una suma de dígitos menor a 10.")