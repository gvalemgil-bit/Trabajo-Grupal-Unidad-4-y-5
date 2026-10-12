class Ingrediente:
    """Clase Ingrediente con los atributos nombre, cantidad y unidad de medida."""

    def __init__(self, nombre, cantidad, unidadMedida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadMedida = unidadMedida

    def mostrar(self):
        # Formatea la cantidad: 300.0 se muestra como 300
        cantidad = str(int(self.cantidad)) if self.cantidad == int(self.cantidad) else str(self.cantidad)
        print(self.nombre.ljust(22) + cantidad.ljust(12) + self.unidadMedida)
