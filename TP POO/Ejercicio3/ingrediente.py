class Ingrediente:
    def __init__(self, nombre, cantidad, unidadMedida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadMedida = unidadMedida
    def mostrar(self):
        cantidad = str(int(self.cantidad)) if self.cantidad == int(self.cantidad) else str(self.cantidad)
        print(self.nombre.ljust(22) + cantidad.ljust(12) + self.unidadMedida)
