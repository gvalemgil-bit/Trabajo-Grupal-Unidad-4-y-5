def formatearNumero(numero):
    """Muestra 8.0 como 8 y 7.5 como 7.5"""
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


class Nota:
    """Clase Nota con los atributos catedra y notaExamen."""

    def __init__(self, catedra, notaExamen):
        self.catedra = catedra
        self.notaExamen = notaExamen

    def mostrar(self):
        print("   - Catedra:", self.catedra, "| Nota:", formatearNumero(self.notaExamen))
