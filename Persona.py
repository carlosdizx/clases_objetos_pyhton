class Persona:
    def __init__(self, nombre, apellido, edad, ):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        return f'{self._nombre} {self._apellido} {self._edad}'


persona1 = Persona('Carlos', 'Díaz', 23)
print(persona1.mostrar_detalle())
persona1.nombre = "Carlos Ernesto"
persona1.apellido = "Díaz Basante"
persona1.edad = "Veititres"
print(persona1.mostrar_detalle())
