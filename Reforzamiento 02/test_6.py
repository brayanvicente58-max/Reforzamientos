nombre_cliente = "jhair"
apellido_cliente = "huamani"
cliente = nombre_cliente + " " + apellido_cliente
print(cliente.title())
producto = "papel higiénico"
print("Producto: {}".format(producto.title()))
precio_unitario = 3.50
print("Precio unitario: S/.{}".format(precio_unitario))
cantidad_adquirida = 40
print("Cantidad: {}".format(cantidad_adquirida))
var_1 = precio_unitario * cantidad_adquirida
var_2 = var_1 * (10 / 100)
if precio_unitario > 3:
    print("Descuento (10%): {}".format(f"{var_2:.2f}"))
else:
    print("No se aplica descuento")
var_4 = var_1 - var_2
print("Sub total: S/.{}".format(var_1))
print("Total a pagar: S/.{}".format(var_4))