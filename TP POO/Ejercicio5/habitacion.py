class Habitacion:
    """Clase Habitacion con los atributos nombre y metrosCuadrados."""

    def __init__(self, nombre, metrosCuadrados):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados

    def mostrar(self):
        print("   -", self.nombre, ":", self.metrosCuadrados, "m2")
