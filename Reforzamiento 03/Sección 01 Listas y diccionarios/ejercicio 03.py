# Definición de precios y carrito de compras
precios = {"Monitor": 450, "Teclado": 80, "MousePad": 25, "Cámara": 150}
carrito = ["Monitor", "MousePad", "Impresora", "Teclado"]  # "Impresora" no existe

subtotal = 0.0
print("--- Productos seleccionados ---")

# Recorrer lista, verificar existencia y calcular subtotal
for producto in carrito:
    if producto in precios:
        precio = precios[producto]
        subtotal += precio
        print(f"{producto}: S/ {precio:.2f}")
    else:
        print(f"[ADVERTENCIA] El producto '{producto}' no está registrado en la tienda.")

# Aplicar descuento de 10% si supera S/ 200
descuento = 0.0
if subtotal > 200:
    descuento = subtotal * 0.10

total_a_pagar = subtotal - descuento

# Impresión de resultados
print(f"\nSubtotal: S/ {subtotal:.2f}")
print(f"Descuento (10%): S/ {descuento:.2f}")
print(f"Total a pagar: S/ {total_a_pagar:.2f}")