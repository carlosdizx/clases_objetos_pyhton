class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Carlos', 'Díaz', 23)
print(f'Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
persona2 = Persona('Ernesto', 'Basante', 32)
print(f'Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

print("-------Modificando los datos-------")
persona1.nombre = "Carlos Ernesto"
persona1.apellido = "Díaz Basante"
persona1.edad = "Veintitres años"
persona2.nombre = "Ernesto Carlos"
persona2.apellido = "Basante Díaz"
persona2.edad = 23
print(f'Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
print(f'Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
