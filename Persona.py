class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Carlos', 'Díaz', 23)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print("-------")

persona2 = Persona('Ernesto', 'Basante', 32)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
