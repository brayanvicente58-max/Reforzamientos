usuario_1 = []
usuario_2 = []

usuario_1.append("Luis")
usuario_1.append("Gamarra")
usuario_1.append(25)
usuario_1.append("Ingeniero")

usuario_2.append("Ana")
usuario_2.append("Torres")
usuario_2.append(23)
usuario_2.append("Contadora")

print(f"Usuario 1: {usuario_1}")
print(f"Usuario 2: {usuario_2}")

suma_edades = usuario_1[2] + usuario_2[2]
print("Suma de edades:", suma_edades)

lista_concatenada = usuario_1 + usuario_2
print("Lista concatenada:", lista_concatenada)

print("Lista en orden inverso:", lista_concatenada[::-1])

lista_final = [usuario_1[0], usuario_1[1], usuario_1[3], usuario_2[0], usuario_2[2], "Analista de Datos"]

print("Lista final modificada:", lista_final)
print("Cantidad final de elementos:", len(lista_final))