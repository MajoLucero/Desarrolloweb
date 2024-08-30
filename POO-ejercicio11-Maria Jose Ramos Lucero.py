import matplotlib.pyplot as plt
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        if punto_inicial is None:
            punto_inicial = Punto(0, 0)
        if punto_final is None:
            punto_final = Punto(1, 1)

        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

    def dibujar(self):
        x_values = [self.punto_inicial.x, self.punto_final.x, self.punto_final.x, self.punto_inicial.x, self.punto_inicial.x]
        y_values = [self.punto_inicial.y, self.punto_inicial.y, self.punto_final.y, self.punto_final.y, self.punto_inicial.y]
        
        plt.plot(x_values, y_values, marker='o')
        plt.fill(x_values, y_values, alpha=0.3)
        plt.xlim(min(x_values) - 1, max(x_values) + 1)
        plt.ylim(min(y_values) - 1, max(y_values) + 1)
        plt.title("Rectángulo")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.grid()
        plt.show()


# Ejemplo de uso
if __name__ == "__main__":
    p1 = Punto(1, 2)
    p2 = Punto(4, 5)

    rect = Rectangulo(p1, p2)

    print(f"Punto inicial: {rect.punto_inicial}")
    print(f"Punto final: {rect.punto_final}")
    print(f"Base: {rect.base()}")
    print(f"Altura: {rect.altura()}")
    print(f"Área: {rect.area()}")
