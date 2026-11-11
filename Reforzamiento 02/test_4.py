notas = [13.5, 15.3, 17.2, 14.8, 11.9]
print("Notas: ", notas)
var_1 = sum(notas)
print("Suma de notas: {}".format(var_1))
var_2 = sum(notas) / len(notas)
print("El promedio es: {}".format(f"{var_2:.2f}"))
var_3 = max(notas)
var_4 = min(notas)
var_5 = var_3 - var_4
print("La diferencia entre la nota mayor y menor es de: {}".format(f"{var_5:.2f}"))
if var_2 > 11:
    print("Estado: APROBADO")
else:
    print("Estado: DESPROBADO")
