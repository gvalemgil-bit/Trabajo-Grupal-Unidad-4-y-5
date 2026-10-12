from componente_cpu import ComponenteCPU
from computadora import Computadora


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


def cargarComputadora():
    print()
    print("===== CARGA DE LA COMPUTADORA =====")
    marca = input("INGRESE MARCA: ")
    modelo = input("INGRESE MODELO: ")

    nuevaComputadora = Computadora(marca, modelo)

    while True:
        print("INGRESE LOS DATOS DEL COMPONENTE")
        componente = input("INGRESE COMPONENTE (Ej: Memoria RAM 2 Gb): ")
        marcaComponente = input("INGRESE MARCA DEL COMPONENTE: ")
        cantidad = pedirEntero("INGRESE CANTIDAD: ")
        precio = pedirDecimal("INGRESE PRECIO: ")

        nuevoComponente = ComponenteCPU(componente, marcaComponente, cantidad, precio)
        nuevaComputadora.agregarComponente(nuevoComponente)

        salirComponentes = input("DESEA CARGAR OTRO COMPONENTE? (SI/NO): ").strip().upper()
        if salirComponentes == "SI":
            continue
        elif salirComponentes == "NO":
            break
        else:
            print("Respuesta invalida, se toma como NO.")
            break

    # Muestro la informacion cargada y el costo de la computadora
    print()
    nuevaComputadora.mostrar()
    print()
    return nuevaComputadora


def main():
    while True:
        cargarComputadora()

        respuesta = input("DESEA COTIZAR UNA NUEVA COMPUTADORA? (SI/NO): ").strip().upper()
        if respuesta == "SI":
            continue
        elif respuesta == "NO":
            break
        else:
            print("Respuesta invalida, se toma como NO.")
            break

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
