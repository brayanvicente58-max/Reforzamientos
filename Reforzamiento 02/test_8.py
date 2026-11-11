tipo_cambio = 3.75
monto_1 = 200
monto_2 = 340
monto_3 = 120
dolar_1 = monto_1 / tipo_cambio
dolar_2 = monto_2 / tipo_cambio
dolar_3 = monto_3 / tipo_cambio
suma = monto_1 + monto_2 + monto_3
dolar_4 = suma / tipo_cambio
print("Tipo de cambio : S/.{}".format(tipo_cambio))
print("Monto 1: S/.{} -> USD {}".format(monto_1, f"{dolar_1:.2f}"))
print("Monto 2: S/.{} -> USD {}".format(monto_2, f"{dolar_2:.2f}"))
print("Monto 3: S/.{} -> USD {}".format(monto_3, dolar_3))
print("Total en soles: S/.{}".format(suma))
print("Total en dolares: USD {}".format(dolar_4))