nombre = "juan gonzales"
peso = 75
estatura = 1.72
IMC = peso / (estatura ** 2)
print("Nombre: {}".format(nombre.title()))
print("Peso: {} kg".format(peso))
print("Estatura: {} m".format(estatura))
print("IMC calculado: {}".format(f"{IMC:.2f}"))
if IMC < 18.5:
    print("Clasificación: Bajo peso")
if 18.5 < IMC < 25:
    print("Clasificación: Peso normal")
if 25 < IMC < 30:
    print("Clasificación: Sobrepeso")
if 30 < IMC:
    print("Clasificación: Obesidad")