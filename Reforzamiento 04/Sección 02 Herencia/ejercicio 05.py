class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"Figura geométrica: {self.nombre}")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        if base <= 0 or altura <= 0:
            raise ValueError("Las dimensiones deben ser mayores a cero.")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    PI = 3.1416

    def __init__(self, radio):
        super().__init__("Círculo")
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a cero.")
        self.radio = radio

    def calcular_area(self):
        return self.PI * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * self.PI * self.radio

print("--- FIGURAS GEOMÉTRICAS ---")
figuras = [
    Rectangulo(5.0, 3.0),
    Rectangulo(7.5, 4.2),
    Circulo(3.0),
    Circulo(5.5)
]

for f in figuras:
    f.mostrar_nombre()
    if isinstance(f, Rectangulo):
        print(f"Dimensiones -> Base: {f.base:.2f}, Altura: {f.altura:.2f}")
    elif isinstance(f, Circulo):
        print(f"Dimensiones -> Radio: {f.radio:.2f}")
    print(f"Área: {f.calcular_area():.2f}")
    print(f"Perímetro: {f.calcular_perimetro():.2f}\n")