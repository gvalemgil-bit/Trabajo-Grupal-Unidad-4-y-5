from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion

class Principal:
    @staticmethod
    def main():
        barrio = Barrio("Los Aromos", "Constructora del Sur S.A.")

        vivienda1 = Vivienda("Av. Siempreviva", 742, "A", 1, 200)
        vivienda1.agregarHabitacion(Habitacion("Living", 30))
        vivienda1.agregarHabitacion(Habitacion("Cocina", 12))
        vivienda1.agregarHabitacion(Habitacion("Dormitorio", 14))
        vivienda1.agregarHabitacion(Habitacion("Bano", 5))

        vivienda2 = Vivienda("Av. Siempreviva", 744, "A", 2, 150)
        vivienda2.agregarHabitacion(Habitacion("Living", 25))
        vivienda2.agregarHabitacion(Habitacion("Dormitorio", 12))
        vivienda2.agregarHabitacion(Habitacion("Bano", 4))

        vivienda3 = Vivienda("Calle Serenata", 45, "B", 3, 120)
        vivienda3.agregarHabitacion(Habitacion("Living", 20))
        vivienda3.agregarHabitacion(Habitacion("Cocina", 10))
        vivienda3.agregarHabitacion(Habitacion("Dormitorio", 12))
        vivienda3.agregarHabitacion(Habitacion("Bano", 4))

        vivienda4 = Vivienda("Calle Serenata", 47, "B", 4, 90)
        vivienda4.agregarHabitacion(Habitacion("Living", 20))
        vivienda4.agregarHabitacion(Habitacion("Dormitorio", 12))
        vivienda4.agregarHabitacion(Habitacion("Bano", 4))

        barrio.agregarVivienda(vivienda1)
        barrio.agregarVivienda(vivienda2)
        barrio.agregarVivienda(vivienda3)
        barrio.agregarVivienda(vivienda4)


        print("=========== DATOS DEL BARRIO ===========")
        barrio.mostrar()

        print()
        print("=========== RESULTADOS ===========")
        print("a) Superficie total de terreno del barrio:", barrio.getSuperficieTotalTerreno(), "m2")
        print("b) Superficie de terreno de la manzana A:", barrio.getSuperficieTotalTerrenoXManzana("A"), "m2")
        print("   Superficie de terreno de la manzana B:", barrio.getSuperficieTotalTerrenoXManzana("B"), "m2")
        print("c) Metros cubiertos de la vivienda 1:", vivienda1.getMetrosCuadradosCubiertos(), "m2")
        print("d) Superficie total cubierta del barrio:", barrio.getSuperficieTotalCubierta(), "m2")

        print()
        print("=========== PRUEBA DE LA EXCEPCION ===========")
        viviendaIncorrecta = Vivienda("Calle Falsa", 123, "C", 5, 50)
        viviendaIncorrecta.agregarHabitacion(Habitacion("Living", 30))
        viviendaIncorrecta.agregarHabitacion(Habitacion("Dormitorio", 25))
        try:
            print("Metros cubiertos:", viviendaIncorrecta.getMetrosCuadradosCubiertos())
        except Exception as e:
            print("Excepcion lanzada:", e)

if __name__ == "__main__":
    Principal.main()
