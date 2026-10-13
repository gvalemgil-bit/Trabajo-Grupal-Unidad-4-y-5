def formatearNumero(numero):
    if numero == int(numero):
        return str(int(numero))
    return str(numero)

class Nota:
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra
        self.notaExamen = notaExamen

    def mostrar(self):
        print("   - Catedra:", self.catedra, "| Nota:", formatearNumero(self.notaExamen))
