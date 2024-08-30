class Persona:
    def __init__(self, nombre, edad):
        if not nombre or edad is None:
            raise ValueError("El nombre y la edad no pueden ser nulos.")
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.notas = {
            'lengua': None,
            'matematica': None,
            'historia': None,
            'geografia': None
        }
        self.__comision = None
        self.asignar_comision()

    def asignar_comision(self):
        promedio = self.promedio()
        if self.edad > 17:
            self.__comision = 'N'
        elif promedio >= 8:
            self.__comision = 'A'
        elif promedio >= 6:
            self.__comision = 'B'
        else:
            self.__comision = 'C'

    def asignar_nota(self, materia, nota):
        if materia in self.notas:
            self.notas[materia] = nota
            self.asignar_comision()
        else:
            raise ValueError("Materia no válida.")

    def promedio(self):
        notas_validas = [nota for nota in self.notas.values() if nota is not None]
        return sum(notas_validas) / len(notas_validas) if notas_validas else 0

    def mostrar_notas(self):
        return {materia: nota for materia, nota in self.notas.items()}

    def get_comision(self):
        return self.__comision


class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        if not materia:
            raise ValueError("La materia no puede ser nula.")
        self.materia = materia

    def evaluar(self, alumno, materia, nota):
        if materia != self.materia:
            raise ValueError(f"El profesor solo puede evaluar en {self.materia}.")
        alumno.asignar_nota(materia, nota)


# Ejemplo de uso
if __name__ == "__main__":
    alumno1 = Alumno("Juan", 18)
    alumno1.asignar_nota("lengua", 8)
    alumno1.asignar_nota("matematica", 7)
    alumno1.asignar_nota("historia", 9)

    profesor1 = Profesor("Pedro", 35, "matematica")
    profesor1.evaluar(alumno1, "matematica", 6)

    print(f"Notas de {alumno1.nombre}: {alumno1.mostrar_notas()}")
    print(f"Promedio de {alumno1.nombre}: {alumno1.promedio()}")
    print(f"Comisión de {alumno1.nombre}: {alumno1.get_comision()}")