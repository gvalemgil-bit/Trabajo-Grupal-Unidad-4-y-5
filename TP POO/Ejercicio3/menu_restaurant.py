from ingrediente import Ingrediente
from plato import Plato


def pedirDecimal(mensaje):
    """Pide un numero decimal al usuario hasta que lo cargue bien."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("El valor ingresado no es un numero, intente de nuevo.")


def cargarIngredientes(plato):
    """Carga los ingredientes del plato. Debe haber al menos 1."""
    while True:
        print("INGRESE LOS DATOS DEL INGREDIENTE")
        nombre = input("INGRESE NOMBRE DEL INGREDIENTE: ")
        cantidad = pedirDecimal("INGRESE CANTIDAD: ")
        unidad = input("INGRESE UNIDAD DE MEDIDA (gramos, unidades, litros...): ")

        plato.agregarIngrediente(Ingrediente(nombre, cantidad, unidad))

        salirIngredientes = input("DESEA CARGAR OTRO INGREDIENTE? (SI/NO): ").strip().upper()
        if salirIngredientes == "SI":
            continue
        elif salirIngredientes == "NO":
            break
        else:
            print("Respuesta invalida, se toma como NO.")
            break


def main():
    platosMenu = []  # platos que componen el menu del restaurant

    # --------- CARGA DE PLATOS ---------
    while True:
        print()
        print("INGRESE LOS DATOS DEL PLATO")
        nombreCompleto = input("INGRESE NOMBRE COMPLETO DEL PLATO: ")
        precio = pedirDecimal("INGRESE PRECIO: ")

        esBebida = False
        respuesta = input("ES UNA BEBIDA? (SI/NO): ").strip().upper()
        if respuesta == "SI":
            esBebida = True

        nuevoPlato = Plato(nombreCompleto, precio, esBebida)

        if not esBebida:
            # Si NO es bebida es obligatorio al menos 1 ingrediente
            cargarIngredientes(nuevoPlato)
            while len(nuevoPlato.ingredientes) == 0:
                print("El plato debe tener al menos 1 ingrediente.")
                cargarIngredientes(nuevoPlato)
        else:
            print("Al ser bebida no se cargan ingredientes.")

        platosMenu.append(nuevoPlato)

        salirPlatos = input("DESEA CARGAR OTRO PLATO? (SI/NO): ").strip().upper()
        if salirPlatos == "SI":
            continue
        elif salirPlatos == "NO":
            break
        else:
            print("Respuesta invalida, se toma como NO.")
            break

    # --------- MUESTRO EL MENU DEL RESTAURANT ---------
    print()
    print("-----------MENÚ----------------")
    for plato in platosMenu:
        plato.mostrar()
    print("Fin del menu.")


if __name__ == "__main__":
    main()
