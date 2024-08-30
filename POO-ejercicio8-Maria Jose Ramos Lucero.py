from datetime import datetime, timedelta

class Fecha:
    def __init__(self, dia=1, mes=1, anio=1900):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.validar()

    def __str__(self):
        return self.corta()

    def año_bisiesto(self):
        """Indica si el año es bisiesto."""
        return (self.__anio % 4 == 0 and self.__anio % 100 != 0) or (self.__anio % 400 == 0)

    def dias_mes(self, mes):
        """Devuelve el número de días del mes."""
        if mes < 1 or mes > 12:
            return 0
        if mes == 2:
            return 29 if self.año_bisiesto() else 28
        elif mes in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def validar(self):
        """Valida la fecha y corrige si es necesario."""
        if self.__anio < 1900 or self.__anio > 2050:
            self.__anio = 1900
        if self.__mes < 1 or self.__mes > 12:
            self.__mes = 1
        if self.__dia < 1 or self.__dia > self.dias_mes(self.__mes):
            self.__dia = 1

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia
        self.validar()

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes
        self.validar()

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio
        self.validar()

    def hoy(self):
        """Devuelve la fecha actual."""
        now = datetime.now()
        return Fecha(now.day, now.month, now.year)

    def corta(self):
        """Muestra la fecha en formato corto."""
        return f"{self.__dia:02d}-{self.__mes:02d}-{self.__anio}"

    def larga(self):
        """Muestra la fecha en formato largo."""
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        fecha = datetime(self.__anio, self.__mes, self.__dia)
        dia_semana = dias_semana[fecha.weekday()]
        return f"{dia_semana} {self.__dia} de {fecha.strftime('%B')} de {self.__anio}"

# Ejemplo de uso
if __name__ == "__main__":
    fecha1 = Fecha(2, 9, 2003)
    print(f"Fecha corta: {fecha1.corta()}")        
    print(f"Fecha larga: {fecha1.larga()}")        
    print(f"Año bisiesto: {fecha1.año_bisiesto()}")  

    fecha2 = Fecha(29, 2, 2020)  
    print(f"Fecha corta: {fecha2.corta()}")        
    print(f"Fecha larga: {fecha2.larga()}")        

    fecha_invalida = Fecha(31, 13, 2025)  
    print(f"Fecha corregida: {fecha_invalida}") 