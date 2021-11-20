class Aritmetica:
    """
    Clase aritmetica para realizar las operaciones de sumar, restar, etc
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2


a1 = Aritmetica(5, 3)
a2 = Aritmetica(2, 1)
a3 = Aritmetica(0, 0)

print(a1.sumar())
print(a2.sumar())
print(a3.sumar())
