class Habitacion:
    def __init__(self, nombre, metrosCuadrados):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados
    def mostrar(self):
        print("   -", self.nombre, ":", self.metrosCuadrados, "m2")
