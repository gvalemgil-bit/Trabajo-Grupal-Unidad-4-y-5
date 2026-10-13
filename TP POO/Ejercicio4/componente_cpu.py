def formatearNumero(numero):
    if numero == int(numero):
        return str(int(numero))
    return str(numero)

class ComponenteCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
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
