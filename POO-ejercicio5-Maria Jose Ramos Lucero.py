class ParSumador:
    def __init__(self, numeros):
        self.numeros = numeros

    def encontrar_par(self, objetivo):
        posiciones = {}
        
        for i, num in enumerate(self.numeros):
            complemento = objetivo - num
            if complemento in posiciones:
                return posiciones[complemento], i
            posiciones[num] = i
        
        return None  # Si no se encuentra ningún par

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [10, 20, 10, 40, 50, 60, 70]
    objetivo = 50
    sumador = ParSumador(numeros)
    resultado = sumador.encontrar_par(objetivo)
    
    if resultado:
        print(resultado[0], resultado[1])  # Salida: 3, 4
    else:
        print("No se encontró ningún par que cumpla la condición.")