def formatearNumero(numero):
    """Muestra 450.0 como 450 y 450.5 como 450.5"""
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


class Plato:
    """Clase Plato con los atributos nombreCompleto, precio, esBebida y ingredientes."""

    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes = []  # lista de objetos Ingrediente

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def mostrar(self):
        print(self.nombreCompleto)
        print("Precio: $", formatearNumero(self.precio))

        if self.esBebida:
            print("(Es una bebida, no lleva ingredientes)")
        else:
            print("Ingredientes:")
            print("Nombre".ljust(22) + "Cantidad".ljust(12) + "Unidad de Medida")
            for ingrediente in self.ingredientes:
                ingrediente.mostrar()

        print("----------------------------------")
