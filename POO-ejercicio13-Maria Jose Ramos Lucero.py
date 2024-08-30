import getpass

class CuentaCorreo:
    def __init__(self):
        self.id = input("Ingrese el ID de la cuenta: ")
        self.dominio = input("Ingrese el dominio de la cuenta: ")
        self.__password = self.solicitar_password()

    def solicitar_password(self):
        while True:
            password1 = getpass.getpass("Ingrese su password: ")
            password2 = getpass.getpass("Confirme su password: ")
            if password1 == password2:
                return password1
            else:
                print("Los passwords no coinciden. Intente de nuevo.")

    def cambiar_password(self, nuevo_password):
        self.__password = nuevo_password

    def mostrar_email(self):
        return f"{self.id}@{self.dominio}"

    def __str__(self):
        return self.mostrar_email()


# Ejemplo de uso
if __name__ == "__main__":
    cuenta = CuentaCorreo()
    print("Dirección de correo:", cuenta)