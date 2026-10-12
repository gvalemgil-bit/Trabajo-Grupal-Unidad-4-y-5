from celda import Celda
from matriz import Matriz


def pedirEntero(mensaje):
    """Pide un numero entero al usuario hasta que lo cargue bien."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("El valor ingresado no es un numero entero, intente de nuevo.")


def main():
    miMatriz = Matriz()

    # --------- CARGA DE CELDAS ---------
    print("===== CARGA DE CELDAS =====")
    while True:
        valor = input("Ingrese el valor de la celda (FIN para terminar): ")
        if valor == "FIN":
            break

        fila = pedirEntero("Ingrese la fila: ")
        columna = pedirEntero("Ingrese la columna: ")

        if miMatriz.existeCelda(fila, columna):
            print("Esa posicion ya fue cargada, no se puede repetir la celda.")
        else:
            nuevaCelda = Celda(fila, columna, valor)
            miMatriz.agregarCelda(nuevaCelda)
            print("Celda agregada correctamente.")

    # --------- MUESTRO LOS VALORES DE LA LISTA ---------
    print()
    print("===== VALORES CARGADOS EN LA LISTA =====")
    miMatriz.mostrarCeldas()

    # --------- CONSULTA DE VALOR POR FILA Y COLUMNA ---------
    print()
    print("===== CONSULTA DE CELDAS =====")
    while True:
        respuesta = input("Desea consultar una celda? (SI/NO): ").strip().upper()
        if respuesta == "NO":
            break
        elif respuesta == "SI":
            fila = pedirEntero("Ingrese la fila a buscar: ")
            columna = pedirEntero("Ingrese la columna a buscar: ")
            print("Valor:", miMatriz.getValor(fila, columna))
        else:
            print("Respuesta invalida, debe ingresar SI o NO.")

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
