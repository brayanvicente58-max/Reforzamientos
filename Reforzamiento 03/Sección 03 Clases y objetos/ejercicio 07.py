class Circulo:
    PI = 3.1416

    # Constructor
    def __init__(self, radio: float):
        self.radio = radio

    # Métodos con validación del radio
    def calcular_area(self):
        if not isinstance(self.radio, (int, float)) or self.radio <= 0:
            return "Error: El radio debe ser un valor numérico positivo mayor que cero."
        return self.PI * (self.radio ** 2)

    def calcular_perimetro(self):
        if not isinstance(self.radio, (int, float)) or self.radio <= 0:
            return "Error: El radio debe ser un valor numérico positivo mayor que cero."
        return 2 * self.PI * self.radio


# Instanciación de al menos tres objetos con radios diferentes
c1 = Circulo(4)
c2 = Circulo(7.5)
c3 = Circulo(-2)  # Objeto de prueba para validación

objetos_circulo = [c1, c2, c3]

print("--- RESULTADOS CÍRCULO ---")
for idx, c in enumerate(objetos_circulo, 1):
    print(f"\nCírculo {idx} (Radio: {c.radio}):")
    area = c.calcular_area()
    perimetro = c.calcular_perimetro()

    if isinstance(area, float):
        print(f"- Área: {area:.4f}")
        print(f"- Perímetro: {perimetro:.4f}")
    else:
        print(f"- {area}")