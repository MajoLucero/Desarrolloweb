from itertools import combinations

class SublistasGenerador:
    def __init__(self, lista):
        self.lista = lista

    def obtener_sublistas(self):
        sublistas = []
        # Generamos sublistas de diferentes longitudes
        for i in range(1, len(self.lista) + 1):
            for sublista in combinations(self.lista, i):
                sublistas.append(list(sublista))
        return sublistas

# Ejemplo de uso
if __name__ == "__main__":
    entrada = [4, 5, 6]
    generador = SublistasGenerador(entrada)
    resultado = generador.obtener_sublistas()
    print(resultado)