def formatearNumero(numero):
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []  

    def agregarComponente(self, componente):
        self.componentes.append(componente)

    def getCostoTotal(self):
        costo = 0
        for componente in self.componentes:
            costo = costo + componente.getSubtotal()
        return costo

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
