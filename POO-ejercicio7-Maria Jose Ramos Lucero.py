class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        else:  # self.x > 0 and self.y < 0
            return "Cuarto cuadrante"

    def vector(self, otro):
        return (otro.x - self.x, otro.y - self.y)


if __name__ == "__main__":
    punto1 = Punto(3, 4)
    punto2 = Punto(1, 2)

    print(f"Punto 1: {punto1}")                   
    print(f"Punto 2: {punto2}")                   

    print(f"Cuadrante de Punto 1: {punto1.cuadrante()}")  
    print(f"Cuadrante de Punto 2: {punto2.cuadrante()}")  

    vector_resultante = punto1.vector(punto2)
    print(f"Vector desde Punto 1 a Punto 2: {vector_resultante}") 