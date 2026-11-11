float_1 = 35.4
float_2 = 43.2
fahrenheit_1 = (float_1 * 9 / 5) + 32
fahrenheit_2 = (float_2 * 9 / 5) + 32
kelvin_1 = float_1 + 273.15
kelvin_2 = float_2 + 273.15
diferencia_temperaturas = float_2 - float_1
print("Temperatura 1: {}°C".format(float_1))
print("Fahrenheit: {}°F".format(fahrenheit_1))
print("Kelvin: {}°K".format(f"{kelvin_1:.2f}"))
print("Temperatura 2: {}°C".format(float_2))
print("Fahrenheit: {}°F".format(fahrenheit_2))
print("Kelvin: {}°K".format(f"{kelvin_2:.2f}"))