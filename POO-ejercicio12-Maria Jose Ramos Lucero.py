class Monedas:
    def __init__(self, cantidad, unidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = cantidad
        self.unidad = unidad

    def __str__(self):
        return f"{self.cantidad} {self.unidad}"

    def sumar(self, otra):
        if self.unidad != otra.unidad:
            raise ValueError("No se pueden sumar monedas de diferentes unidades.")
        return Monedas(self.cantidad + otra.cantidad, self.unidad)

    def sumar_valor(self, cantidad, unidad):
        if self.unidad != unidad:
            raise ValueError("La unidad de la moneda no coincide.")
        return Monedas(self.cantidad + cantidad, self.unidad)



if __name__ == "__main__":
    moneda1 = Monedas(100, "EUR")
    moneda2 = Monedas(50, "EUR")
    
    print("Moneda 1:", moneda1)
    print("Moneda 2:", moneda2)
    
    suma = moneda1.sumar(moneda2)
    print("Suma:", suma)

    moneda3 = moneda1.sumar_valor(30, "EUR")
    print("Suma con valor:", moneda3)

    try:
        moneda4 = Monedas(50, "USD")
        suma_diferente = moneda1.sumar(moneda4)
    except ValueError as e:
        print("Error:", e)

    try:
        moneda5 = moneda1.sumar_valor(20, "USD")
    except ValueError as e:
        print("Error:", e)