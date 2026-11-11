from calculos import calcular_raiz, calcular_cuadrado, calcular_cubo

entradas = ["16", "-5", "abc", "9"]

print("--- OPERACIONES MATEMÁTICAS ---")
for entrada in entradas:
    print(f"\nEntrada evaluada: '{entrada}'")
    try:
        numero = float(entrada)
        if numero < 0:
            raise ValueError("El número debe ser mayor o igual a cero para operar raíces.")

        print(f"Número válido: {numero}")
        print(f"Raíz cuadrada: {calcular_raiz(numero):.2f}")
        print(f"Cuadrado: {calcular_cuadrado(numero):.2f}")
        print(f"Cubo: {calcular_cubo(numero):.2f}")

    except ValueError as e:
        print(f"Error en la entrada: {e}")