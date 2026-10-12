class Matriz:
    """Clase Matriz que contiene una lista de objetos Celda."""

    def __init__(self):
        self.celdasMatriz = []

    def agregarCelda(self, celda):
        self.celdasMatriz.append(celda)

    # Devuelve True si ya existe una celda con esa fila y columna
    def existeCelda(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    # Recibe fila y columna y retorna el valor almacenado en esa celda
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
