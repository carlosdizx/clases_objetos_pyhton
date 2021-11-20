class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        return f'{self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}'


persona1 = Persona('Carlos', 'Díaz', 23, '3163930876', 'B+', 'Guapo', m='Manzana', p='Pera')
persona2 = Persona('Ernesto', 'Basante', 32)

print(f'Persona 1: {persona1.mostrar_detalle()}')
print(f'Persona 2: {persona2.mostrar_detalle()}')
