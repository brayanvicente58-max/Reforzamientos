# Definición de listas para productos y sus respectivas cantidades
productos = ["Pan", "Mantequilla", "Jamón", "Queso", "Yogurt"]
cantidades = [10, 2, 15, 1, 4]

# Mostrar cada producto junto con su cantidad
print("--- Productos registrados ---")
total_unidades = 0
for i in range(len(productos)):
    print(f"{productos[i]}: {cantidades[i]} unidades")
    total_unidades += cantidades[i]

# Mostrar total de unidades registradas
print(f"\nTotal de unidades disponibles: {total_unidades}")

# Identificar productos con menos de 5 unidades o notificar si no hay
print("\n--- Productos con menos de 5 unidades ---")
productos_bajo_stock = []

for i in range(len(productos)):
    if cantidades[i] < 5:
        productos_bajo_stock.append((productos[i], cantidades[i]))
        print(f"- {productos[i]}: {cantidades[i]} unidades")

if not productos_bajo_stock:
    print("Ningún producto tiene stock bajo.")