from celda import Celda
from matriz import Matriz

def pedirEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("El valor ingresado no es un numero entero, intente de nuevo.")


def main():
    mi_matriz = Matriz()

    print("===== CARGA DE CELDAS =====")
    while True:
        valor = input("Ingrese el valor de la celda (FIN para terminar): ")
        if valor == "FIN":
            break

        fila = pedirEntero("Ingrese la fila: ")
        columna = pedirEntero("Ingrese la columna: ")

        if mi_matriz.existeCelda(fila, columna):
            print("Esa posicion ya fue cargada, no se puede repetir la celda.")
        else:
            nuevaCelda = Celda(fila, columna, valor)
            mi_matriz.agregarCelda(nuevaCelda)
            print("Celda agregada correctamente.")

    print()
    print("===== VALORES CARGADOS EN LA LISTA =====")
    mi_matriz.mostrarCeldas()

    print()
    print("===== CONSULTA DE CELDAS =====")
    while True:
        respuesta = input("Desea consultar una celda? (SI/NO): ").strip().upper()
        if respuesta == "NO":
            break
        elif respuesta == "SI":
            fila = pedirEntero("Ingrese la fila a buscar: ")
            columna = pedirEntero("Ingrese la columna a buscar: ")
            print("Valor:", mi_matriz.getValor(fila, columna))
        else:
            print("Respuesta invalida, debe ingresar SI o NO.")

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
