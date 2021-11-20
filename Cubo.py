class Cubo:
    def __init__(self, ancho, alto, largo):
        self.ancho = ancho
        self.alto = alto
        self.largo = largo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.largo


ancho = float(input("Ancho del cubo: "))
alto = float(input("Alto del cubo: "))
largo = float(input("Largo del cubo: "))

cubo_1 = Cubo(ancho, alto, largo)
print(cubo_1.calcular_volumen())
