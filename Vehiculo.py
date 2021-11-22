class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: {self._color} {self._ruedas}'


class Coche(Vehiculo):
    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Coche:{self._velocidad}'


class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Bicicleta:{self._tipo}'


vehiculo = Vehiculo('azul', 3)
coche = Coche('120Km/H', 'Verde', 4)
bicicleta = Bicicleta('urbana', 'Roja', 2)

print(vehiculo)
print(coche)
print(bicicleta)
