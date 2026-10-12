def formatearNumero(numero):
    """Muestra 450.0 como 450 y 450.5 como 450.5"""
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


class ComponenteCPU:
    """Clase ComponenteCPU con los atributos componente, marca, cantidad y precio."""

    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    # Subtotal = precio por la cantidad usada del componente
    def getSubtotal(self):
        return self.precio * self.cantidad

    def mostrar(self):
        print(
            self.componente.ljust(18)
            + self.marca.ljust(12)
            + str(self.cantidad).ljust(10)
            + formatearNumero(self.precio).ljust(18)
            + formatearNumero(self.getSubtotal())
        )
