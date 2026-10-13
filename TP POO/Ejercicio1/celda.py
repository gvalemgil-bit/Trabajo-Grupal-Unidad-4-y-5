class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
    def mostrar(self):
        print("Fila:", self.fila, "| Columna:", self.columna, "| Valor:", self.valor)
