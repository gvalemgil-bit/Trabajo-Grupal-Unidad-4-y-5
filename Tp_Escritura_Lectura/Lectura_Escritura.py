import os
def separar_datos():
    datos_alumnos = []
    with open("alumnos.txt","r", encoding="utf-8") as archivo:
        for linea in archivo:
            lineas = linea.strip()
            nombre,apellido,legajo,promedio = lineas.split(";")
            datos_alumnos.append((nombre,apellido,legajo,promedio))
    return datos_alumnos
def archivo_aprobados():
    if not os.path.exists("aprobados.txt"):
        with open("aprobados.txt","w", encoding="utf-8") as archivo: 
            pass 
    with open("alumnos.txt", "r", encoding="utf-8") as alumnos, open("aprobados.txt", "w", encoding="utf-8") as aprobados:
     for linea in alumnos:
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue 
        nombre,apellido,legajo,promedio = linea_limpia.split(";")
        promedio = float(promedio)
        if promedio >= 6.0:
            aprobados.write(linea)
            print(f"{nombre} {apellido}:\nLegajo: {legajo}\nNota Promedio: {promedio}")
def leer_alumnos():
    datos = separar_datos()
    if datos == []:
        print("Error: El archivo está vacío.")
    else:
        for nombre, apellido, legajo, promedio in datos:
            print(f"{nombre} {apellido}:\nLegajo: {legajo}\nNota Promedio: {promedio}")
            print()
def generar_diccionario():
    datos = separar_datos()
    for nombre,apellido,legajo,promedio in datos:            
        diccionarios_alumnos.append({legajo:(apellido,promedio)})
    return diccionarios_alumnos
def agregar_alumno():
    legajo_valido = False
    nombre = input("Ingrese el nombre del alumno: ").title()
    while not nombre.isalpha():
        print("Error: El nombre solo puede contener letras.")
        nombre = input("Ingrese nuevamente el nombre del alumno: ").title()
    apellido = input("Ingrese el apellido del alumno: ").title()
    while not apellido.isalpha():
        print("Error: El apellido solo puede contener letras.")
        apellido = input("Ingrese nuevamente el apellido del alumno: ").title()
    while not legajo_valido:
        legajo_repetido = False
        legajo = input("Ingrese el legajo del alumno: ")
        datos = separar_datos()
        for elemento in datos:
            if legajo in elemento:
                print("Error: El legado ya se encuentra en el archivo")
                legajo_repetido = True
        if len(legajo) != 5:
            print("Error: El legajo debe tener una longitud de 5 dígitos")
        elif not legajo.isdigit():
            print("Error: El legajo debe ser un número entero válido")
        elif not legajo_repetido:
            legajo_valido = True
    promedio = input("Ingrese la nota del alumno: ")
    while True:
        try:
            rango_valido = False
            while not rango_valido:
                promedio = float(promedio)
                if promedio <= 10 and promedio >= 1:
                    rango_valido = True
                else:
                    print("Error: El promedio debe estar entre 1 y 10")
                    promedio = input("Ingrese nuevamente el promedio: ")
            break
        except ValueError:
            print("Error: El promedio ingresado es inválido.")
            promedio = input("Ingrese nuevamente el promedio: ")
    with open("alumnos.txt","a",encoding="utf-8") as nuevo_alumno:
        nuevo_alumno.write(f"{nombre};{apellido};{legajo};{promedio}\n")
    diccionarios_alumnos.append({legajo:(nombre,apellido,promedio)})
def validar_existe_alumno():
    pass
if not os.path.exists("alumnos.txt"):
    with open("alumnos.txt","w", encoding="utf-8") as archivo: #Sin la codificación utf-8 las tildes no se imprimen correctamente.
        pass #Pass hace que el archivo se genere vacío
diccionarios_alumnos = []
generar_diccionario()

while True:
    print("-"*8,"MENÚ","-"*8)
    print("1) Ver alumnos")
    print("2) Agregar alumno")
    print("3) Generar archivo de aprobados")
    print("4) Salir")
    eleccion = input("Seleccione una opción: ")
    match eleccion:
        case "1":
            leer_alumnos()
        case "2":
            print("Ha elegido agregar un nuevo alumno.")
            agregar_alumno()
        case "3":
            archivo_aprobados()                
        case "4":
            print("Ha salido del sistema.")
            break
        case _:
            print("Error: Selección inválida. Ingrese una opción del 1 al 4.")
    