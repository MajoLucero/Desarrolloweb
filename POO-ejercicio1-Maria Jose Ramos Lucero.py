class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'DNI: {self.dni}')

    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo de uso
persona1 = Persona('Juan', 25, '12345678A')
persona1.mostrar_datos()
print(f'¿Es mayor de edad? {"Sí" if persona1.es_mayor_de_edad() else "No"}')

persona2 = Persona('Ana', 17, '87654321B')
persona2.mostrar_datos()
print(f'¿Es mayor de edad? {"Sí" if persona2.es_mayor_de_edad() else "No"}')