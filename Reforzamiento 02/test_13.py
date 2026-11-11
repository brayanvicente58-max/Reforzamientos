numeros = []

valores = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
for valor in valores:
    numeros.append(valor)

suma_total = sum(numeros)

promedio = suma_total / len(numeros)

mayor = max(numeros)
menor = min(numeros)

pares = 0
impares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números registrados:", numeros)
print("Suma total:", suma_total)
print(f"Promedio: {promedio:.2f}")
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)