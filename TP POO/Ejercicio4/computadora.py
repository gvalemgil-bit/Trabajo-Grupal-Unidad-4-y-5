def formatearNumero(numero):
    """Muestra 450.0 como 450 y 450.5 como 450.5"""
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


class Computadora:
    """Clase Computadora con los atributos marca, modelo y la lista de componentes."""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []  # lista de objetos ComponenteCPU

    def agregarComponente(self, componente):
        self.componentes.append(componente)

    # Costo total = suma de (precio * cantidad) de cada componente
    def getCostoTotal(self):
        costo = 0
        for componente in self.componentes:
            costo = costo + componente.getSubtotal()
        return costo

    # Precio de venta sugerido: costo + 40% si el costo es menor a 50000,
    # sino costo + 30%
    def getPrecioVenta(self):
        costo = self.getCostoTotal()
        if costo < 50000:
            return costo + costo * 0.40
        else:
            return costo + costo * 0.30

    def mostrar(self):
        print("-----------Computadora----------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Componentes:")
        print(
            "Componente".ljust(18)
            + "Marca".ljust(12)
            + "Cantidad".ljust(10)
            + "Precio X Unidad".ljust(18)
            + "SubTotal"
        )
        for componente in self.componentes:
            componente.mostrar()

        costo = self.getCostoTotal()
        recargo = self.getPrecioVenta() - costo
        print(" ".rjust(50), "Costo Total", formatearNumero(costo).rjust(12))
        print()
        print("El precio sugerido de venta es", formatearNumero(costo), "+",
              formatearNumero(recargo), "=", formatearNumero(self.getPrecioVenta()))
