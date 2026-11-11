sueldo = 2500
if sueldo % 2 == 0:
    print("Clasificación: Número par")
else:
    print("Clasificación: Número impar")
bono = (12 / 100) * sueldo
print("El bono del 12% es de: {}".format(bono))
sueldo_total = sueldo + bono
print("El sueldo total es de: {}".format(sueldo_total))
var_4 = sueldo % 7
print("Residuo de dividir entre 7: {}".format(var_4))