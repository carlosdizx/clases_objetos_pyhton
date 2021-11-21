class Persona:
    def __init__(self, nombre, apellido, edad, ):
        self.__nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        return f'{self.__nombre} {self._apellido} {self._edad}'


persona1 = Persona('Carlos', 'Díaz', 23)
persona1.__nombre = 1
print(persona1.mostrar_detalle())
