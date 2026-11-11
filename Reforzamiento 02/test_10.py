float_1 = 40.6
float_2 = 5.5
int_1 = int(float_1)
int_2 = int(float_2)
print("Primer valor decimal: ",float_1)
print("Segundo valor decimal: ",float_2)
print("Priner entero: ",int_1)
print("Segundo entero: ",int_2)
residuo = int_1 % int_2
if residuo == 0:
    print("¿El primer número es múltiplo del segundo?: Sí")
else:
    print("¿El primer número es múltiplo del segundo?: No")
cociente = int_1 // int_2
print("Residuo: ",residuo)
print("Cociente: ",cociente)