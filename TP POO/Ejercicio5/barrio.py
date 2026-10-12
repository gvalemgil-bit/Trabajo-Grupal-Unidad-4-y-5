class Barrio:
    """Clase Barrio con los atributos nombre, empresaConstructora y la lista de viviendas."""

    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []  # lista de objetos Vivienda

    def agregarVivienda(self, vivienda):
        self.viviendas.append(vivienda)

    # a) Total de metros de terreno del barrio (todas las viviendas)
    def getSuperficieTotalTerreno(self):
        total = 0
        for vivienda in self.viviendas:
            total = total + vivienda.superficieTerreno
        return total

    # b) Total de metros de terreno de una manzana especifica del barrio
    def getSuperficieTotalTerrenoXManzana(self, manzana):
        total = 0
        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                total = total + vivienda.superficieTerreno
        return total

    # d) Total de metros cuadrados cubiertos del barrio.
    # Reutiliza getMetrosCuadradosCubiertos() de la clase Vivienda.
    def getSuperficieTotalCubierta(self):
        total = 0
        for vivienda in self.viviendas:
            total = total + vivienda.getMetrosCuadradosCubiertos()
        return total

    def mostrar(self):
        print("Barrio:", self.nombre, "| Empresa constructora:", self.empresaConstructora)
        for vivienda in self.viviendas:
            vivienda.mostrar()
