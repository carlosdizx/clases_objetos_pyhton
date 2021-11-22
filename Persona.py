class Persona:
    def __init__(self, nombre, apellido, edad, ):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        return f'{self._nombre} {self._apellido} {self._edad}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


persona1 = Persona('Carlos', 'Díaz', 23)
print(persona1.nombre)
print(persona1.nombre)
