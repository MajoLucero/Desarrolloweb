class NumeroEntero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, otro):
        """Suma."""
        return NumeroEntero(self.valor + otro.valor)

    def __sub__(self, otro):
        """Resta."""
        return NumeroEntero(self.valor - otro.valor)

    def __mul__(self, otro):
        """Multiplicación."""
        return NumeroEntero(self.valor * otro.valor)

    def __truediv__(self, otro):
        """División."""
        if otro.valor == 0:
            print("Error: División por cero. Devolviendo 0.")
            return NumeroEntero(0)
        return NumeroEntero(self.valor // otro.valor)

    def __str__(self):
        """Representación en forma de string."""
        return str(self.valor)

# Ejemplo de uso
if __name__ == "__main__":
    num1 = NumeroEntero(20)
    num2 = NumeroEntero(4)
    num3 = NumeroEntero(0)

    print(f"Suma: {num1} + {num2} = {num1 + num2}")         
    print(f"Resta: {num1} - {num2} = {num1 - num2}")       
    print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")  
    print(f"División: {num1} / {num2} = {num1 / num2}")     
    print(f"División: {num1} / {num3} = {num1 / num3}")     