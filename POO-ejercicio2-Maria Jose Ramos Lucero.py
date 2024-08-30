class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class Cuenta:
    def __init__(self, titular: Persona, cantidad=0.0):
        self.titular = titular
        self._cantidad = cantidad  # Atributo privado

    def mostrar(self):
        print(f'Titular: {self.titular.nombre}')
        print(f'Cantidad: {self._cantidad:.2f}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
            print(f'Ingresado: {cantidad:.2f}')
        else:
            print('La cantidad a ingresar debe ser positiva.')

    def retirar(self, cantidad):
        self._cantidad -= cantidad
        print(f'Retirado: {cantidad:.2f}')

# Ejemplo de uso
titular = Persona('Juan', 30, '12345678A')
cuenta = Cuenta(titular, 100.0)

cuenta.mostrar()
cuenta.ingresar(50.0)
cuenta.mostrar()
cuenta.retirar(30.0)
cuenta.mostrar()
cuenta.ingresar(-10.0)  