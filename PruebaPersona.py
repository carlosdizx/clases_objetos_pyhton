from Persona import Persona

print("Creacion de objetos".center(50, '-'))
persona1 = Persona("Carlos", "Diaz", 30)
print(persona1.mostrar_detalle())

print("Eliminacion de objetos".center(50, '-'))
del persona1
