class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
    
        if punto_inicial is None:
            punto_inicial = [0, 0]
        if punto_final is None:
            punto_final = [0, 0]

        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        
        return abs(self.punto_final[0] - self.punto_inicial[0])

    def altura(self):
       
        return abs(self.punto_final[1] - self.punto_inicial[1])

    def area(self):
      
        return self.base() * self.altura()


if __name__ == "__main__":
    rect1 = Rectangulo([1, 2], [4, 5])
    print(f"Base: {rect1.base()}")        
    print(f"Altura: {rect1.altura()}")    
    print(f"Área: {rect1.area()}")         

    rect2 = Rectangulo()
    print(f"Base: {rect2.base()}")        
    print(f"Altura: {rect2.altura()}")    
    print(f"Área: {rect2.area()}")         