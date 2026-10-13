class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []
    def agregarNota(self, nota):
        self.notas.append(nota)
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        total = 0
        for nota in self.notas:
            total = total + nota.notaExamen
        return total / len(self.notas)
    def mostrar(self):
        print("Alumno:", self.nombreCompleto, "| Legajo:", self.legajo)
        if len(self.notas) == 0:
            print("   El alumno no tiene notas cargadas.")
        else:
            for nota in self.notas:
                nota.mostrar()
