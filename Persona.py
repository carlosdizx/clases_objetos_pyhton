class Persona:
    def __init__(self, nombre, apellido, edad, ):
        self.__nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        return f'{self.__nombre} {self._apellido} {self._edad}'

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


persona1 = Persona('Carlos', 'Díaz', 23)
print(persona1.nombre)
persona1.nombre = "Carlos Ernesto"
print(persona1.nombre)
