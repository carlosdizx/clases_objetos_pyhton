class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        return f'{self.nombre} {self.apellido} {self.edad}'


persona1 = Persona('Carlos', 'Díaz', 23)
persona2 = Persona('Ernesto', 'Basante', 32)

print(f'Persona 1: {persona1.mostrar_detalle()}')
print(f'Persona 2: {persona2.mostrar_detalle()}')
