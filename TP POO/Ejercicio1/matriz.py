class Matriz:
    def __init__(self):
        self.celdasMatriz = []
    def agregarCelda(self, celda):
        self.celdasMatriz.append(celda)
    def existeCelda(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False
    def getValor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

    def mostrarCeldas(self):
        if len(self.celdasMatriz) == 0:
            print("No se cargaron celdas.")
        else:
            for celda in self.celdasMatriz:
                celda.mostrar()
