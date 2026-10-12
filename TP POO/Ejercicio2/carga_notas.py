from nota import Nota
from alumno import Alumno


def pedirEntero(mensaje):
    """Pide un numero entero al usuario hasta que lo cargue bien."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("El valor ingresado no es un numero entero, intente de nuevo.")


def pedirDecimal(mensaje):
    """Pide un numero decimal al usuario hasta que lo cargue bien."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("El valor ingresado no es un numero, intente de nuevo.")


def cargarNotasDelAlumno(alumno):
    """Carga N notas para el alumno recibido. Valida que haya al menos 1 nota."""
    while True:
        print("INGRESE LOS DATOS DE LA NOTA")
        catedra = input("INGRESE NOMBRE CATEDRA: ")
        notaExamen = pedirDecimal("Nota: ")

        nuevaNota = Nota(catedra, notaExamen)
        alumno.agregarNota(nuevaNota)

        salirNotas = input("DESEA SALIR DE LA CARGA DE NOTAS? (SI/NO): ").strip().upper()
        if salirNotas == "SI":
            break
        elif salirNotas != "NO":
            print("Respuesta invalida, se toma como NO.")


def main():
    alumnos = []  # conjunto de Alumnos

    # --------- CARGA DE ALUMNOS Y NOTAS ---------
    while True:
        print()
        print("INGRESE DATOS DEL ALUMNO")
        nombreCompleto = input("INGRESE NOMBRE COMPLETO: ")
        legajo = pedirEntero("INGRESE LEGAJO: ")

        alumno = Alumno(nombreCompleto, legajo)
        cargarNotasDelAlumno(alumno)  # siempre carga al menos 1 nota

        alumnos.append(alumno)

        salirAlumno = input("DESEA SALIR DE LA CARGA DE ALUMNOS? (SI/NO): ").strip().upper()
        if salirAlumno == "SI":
            break
        elif salirAlumno != "NO":
            print("Respuesta invalida, se toma como NO.")

    # --------- MUESTRO LA INFORMACION CARGADA ---------
    print()
    print("===== INFORMACION CARGADA =====")
    for alumno in alumnos:
        alumno.mostrar()
        print("   El promedio del alumno es:", round(alumno.promedio(), 2))
        print()


if __name__ == "__main__":
    main()
