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
        return f'Titular: {self.titular.nombre}, Cantidad: {self._cantidad:.2f}'

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad

    def saldo(self):
        return self._cantidad


class CuentasBancarias:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta: Cuenta):
        self.cuentas.append(cuenta)

    def saldo_deudor(self):
        total_deuda = sum(cuenta.saldo() for cuenta in self.cuentas if cuenta.saldo() < 0)
        return total_deuda

    def mostrar_cuentas_negativas(self):
        cuentas_negativas = [(cuenta.titular.nombre, cuenta.saldo()) for cuenta in self.cuentas if cuenta.saldo() < 0]
        for titular, saldo in cuentas_negativas:
            print(f'Titular: {titular}, Saldo Deudor: {saldo:.2f}')


# Ejemplo de uso
titular1 = Persona('Juan', 30, '12345678A')
titular2 = Persona('Ana', 25, '87654321B')

cuenta1 = Cuenta(titular1, 100.0)
cuenta2 = Cuenta(titular2, -50.0)
cuenta3 = Cuenta(titular1, -30.0)

banco = CuentasBancarias()
banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)
banco.agregar_cuenta(cuenta3)

print(f'Saldo deudor total: {banco.saldo_deudor():.2f}')
print('Cuentas con saldo negativo:')
banco.mostrar_cuentas_negativas()