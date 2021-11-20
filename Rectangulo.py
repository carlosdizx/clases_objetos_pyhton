class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = float(input("Ingresar la base del rectangulo: "))
altura = float(input("Ingresar la altura del rectangulo: "))

rec_1 = Rectangulo(base, altura)
print(rec_1.calcular_area())
