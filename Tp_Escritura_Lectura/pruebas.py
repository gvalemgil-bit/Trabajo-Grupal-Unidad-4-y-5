import os
def separar_datos():
    datos_alumnos = []
    with open("alumnos.txt","r", encoding="utf-8") as archivo:
        verificar_vacio = archivo.readlines()
        if not verificar_vacio:
            print("Error: El archivo está vacío.")
        else:
            for linea in verificar_vacio:
                lineas = linea.strip()
                nombre,apellido,legajo,promedio = lineas.split(";")
                datos_alumnos.append((nombre,apellido,legajo,promedio))
    return datos_alumnos
def leer_alumnos():
    datos = separar_datos()
    for nombre, apellido, legajo, promedio in datos:
        print(f"{nombre} {apellido}:\nLegajo: {legajo}\nNota Promedio: {promedio}")
        print()
def generar_diccionario():
    datos = separar_datos()
    for nombre,apellido,legajo,promedio in datos:            
        diccionarios_alumnos.append({legajo:(apellido,promedio)})
    print(diccionarios_alumnos)
def agregar_alumno():
    pass
def validar_existe_alumno():
    pass
def guardar_aprobados():
    pass
diccionarios_alumnos = []
if not os.path.exists("alumnos.txt"):
    with open("alumnos.txt","w", encoding="utf-8") as archivo: #Sin la codificación utf-8 las tildes no se imprimen correctamente.
        pass #Pass hace que el archivo se genere vacío
while True:
    print("-"*8,"MENÚ","-"*8)
    print("1) Ver alumnos")
    print("2) Agregar alumno")
    print("3) Generar archivo de aprobados")
    print("4) Salir")
    eleccion = input("Seleccione una opción: ")
    if not eleccion.isdigit():
        print("Error: Selección inválida. Elija una opción del 1 al 4")
    else:
        leer_alumnos()
        generar_diccionario()
