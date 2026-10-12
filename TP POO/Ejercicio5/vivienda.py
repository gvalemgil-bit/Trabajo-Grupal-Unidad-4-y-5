from habitacion import Habitacion


class Vivienda:
    """Clase Vivienda con los atributos calle, numero, manzana, nroCasa,
    superficieTerreno y la lista de habitaciones."""

    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []  # lista de objetos Habitacion

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Total de metros cuadrados cubiertos de la vivienda.
    # Si es mayor que la superficie del terreno lanza una excepcion.
    def getMetrosCuadradosCubiertos(self):
        total = 0
        for habitacion in self.habitaciones:
            total = total + habitacion.metrosCuadrados

        if total > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")

        return total

    def mostrar(self):
        print("Calle:", self.calle, "| Numero:", self.numero, "| Manzana:", self.manzana,
              "| Nro Casa:", self.nroCasa, "| Terreno:", self.superficieTerreno, "m2")
        for habitacion in self.habitaciones:
            habitacion.mostrar()
