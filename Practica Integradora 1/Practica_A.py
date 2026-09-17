#Practica A- Máquina de golosinas.
matriz_golosinas = [[1,"KitKat",20],
                    [2,"Chicles",50],
                    [3,"Caramelos de Menta",50],
                    [4,"Huevo Kinder",10],
                    [5,"Cheetos",10],
                    [6,"Twix",10],
                    [7,"M&M's",10],
                    [8,"Papas Lays",2],
                    [9,"Milkybar",10],
                    [10,"Alfajor Tofi",15],
                    [11,"Lata Coca",20],
                    [12,"Chitos",10]]
def menu_golosinas():
    for i in range(len(matriz_golosinas)):
        codigo = matriz_golosinas[i][0]
        golosina = matriz_golosinas[i][1]
        stock = matriz_golosinas[i][2]
        print(codigo,golosina,stock)
def golosinas_pedidas_menu():
    for i in range(len(golosinas_pedidas)):
        codigo = golosinas_pedidas[i][0]
        golosinas = golosinas_pedidas[i][1]
        cant_pedidas = golosinas_pedidas[i][2]
        print(codigo,golosinas,cant_pedidas)
def checkear_codigo(codigo):
    for i in range(len(matriz_golosinas)):
        if matriz_golosinas[i][0] == codigo:
            return True
def fue_pedido(codigo):
    for i in range(len(golosinas_pedidas)):
        if golosinas_pedidas[i][1] == matriz_golosinas[codigo-1][1]:
            golosinas_pedidas[i][2] += 1
            return True
empleados = {1100:"José Alonso",1200:"Federico Pacheco",1300:"Nelson Pereira",1400:"Osvaldo Tejada",1500:"Gastón Garcia"}
claves_tecnico = ("admin","CCCDDD","2020")
golosinas_pedidas = []
while True:
   no_golosina = False
   print("-"*8,"MENU","-"*8)
   print("a) Pedir Golosina")
   print("b) Mostrar Golosina")
   print("c) Rellenar Golosinas")
   print("d) Apagar Máquina")
   eleccion = input("Ingrese una opción: ").lower()
   match eleccion:
    case "a":
        legajo = input("Ingrese su legajo: ")
        if not legajo.isdigit():
            print("Error: Legajo inválido.")
        else:
            legajo = float(legajo)
        if legajo in empleados:
            while not no_golosina:
                codigo_golosina = input("Ingrese el código de la golosina: ")
                if not codigo_golosina.isdigit():
                    print("Error: Código Inválido:")
                    break
                else:
                    codigo_golosina = int(codigo_golosina)
                if codigo_golosina == 0:
                    no_golosina = True
                for i in range(len(matriz_golosinas)):
                    if matriz_golosinas[i][0] == codigo_golosina:
                        if matriz_golosinas[i][2] <= 0:
                            print(f"Lo sentimos, la golosina {matriz_golosinas[i][1]} no se encuentra disponible, seleccione otra golosina o ingresa '0' si no desea otra golosina.")
                        else:
                            matriz_golosinas[i][2] -= 1
                            if fue_pedido(codigo_golosina):
                                no_golosina = True
                            else:
                                golosinas_pedidas.append([matriz_golosinas[i][0],matriz_golosinas[i][1],+1])
                                no_golosina = True
        else:
            print("Usted no es un empleado de la empresa.")
            break
    case "b":
           menu_golosinas()
    case "c":
            recarga = True
            contra_1 = input("Ingrese la primera contraseña: ")
            contra_2 = input("Ingrese la segunda contraseña: ")
            contra_3 = input("Ingrese la tercer contraseña: ")
            tupla_admin = (contra_1,contra_2,contra_3)
            if tupla_admin == claves_tecnico:
               while recarga:
                print("Para salir del menu de recarga, presione '0'")
                codigo_golosina = float(input("Ingrese el código de la golosina: "))
                if codigo_golosina == 0:
                   break
                if checkear_codigo(codigo_golosina):
                    for i in range(len(matriz_golosinas)):
                        if matriz_golosinas[i][0] == codigo_golosina:
                            cantidad_a_recargar = input(f"Ingrese la cantidad a recargar de {matriz_golosinas[i][1]}: ")
                            if not cantidad_a_recargar.isdigit():
                                print("Error: Número inválido.")
                            else:
                                cantidad_a_recargar = int(cantidad_a_recargar)
                                if cantidad_a_recargar <= 0:
                                    print("Error: La cantidad a recargar debe ser mayor a cero.")
                                else:
                                    matriz_golosinas[i][2] += cantidad_a_recargar
                else:
                    print("Error: Código inválido.")       
            else:
                print("No tiene permiso para ejecutar la función de recarga")
    case "d":
        golosinas_pedidas_menu()
        break
    case _:
        print("Error: Elección de menú inválida.")