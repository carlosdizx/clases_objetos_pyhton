class Persona:
    def __init__(self, nombre, edad, ):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        return f'{self._nombre} {self._edad}'


class Empleado(Persona):
    def __init__(self, sueldo, nombre, edad):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo


empleado1 = Empleado('2M', 'Carlos', 28)
print(empleado1.mostrar_detalle()+" "+empleado1.sueldo)
