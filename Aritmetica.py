class Aritmetica:
    """
    Clase aritmetica para realizar las operaciones de sumar, restar, etc
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2


a1 = Aritmetica(5, 3)
print(f'Suma: {a1.sumar()}')
print(f'Resta: {a1.restar()}')
print(f'Multiplicación: {a1.multiplicar()}')
print(f'División: {a1.dividir():.2f}')

print("-----")

a2 = Aritmetica(8, 6)
print(f'Suma: {a2.sumar()}')
print(f'Resta: {a2.restar()}')
print(f'Multiplicación: {a2.multiplicar()}')
print(f'División: {a2.dividir():.2f}')
