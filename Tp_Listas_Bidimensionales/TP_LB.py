import random
import numpy as np
#Debido a que varios ejercicios piden la creación de matrices, y para evitar repetir código, creé las siguiente función que genera la matriz con números al azar, para más variedad.
def generar_matriz_random(fila, columna):
    matriz = np.random.randint(1, 101, size=(fila, columna))
    return matriz

#1) Crear una matriz de números
def generar_matriz(filas, columnas): #Este ejercicio pide que la matriz consista de números consecutivos, por lo que la primer función no aplica.
    matriz = [[(i * columnas) + j + 1 for j in range(columnas)] for i in range(filas)]
    matriz_ordenada = np.array(matriz)
    return matriz_ordenada

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
print(generar_matriz(filas,columnas))
print() #Imprimo espacios vacios luego de cada ejercicos para que sean mas fáciles de distinguir por pantalla.
#2) Suma de todos los elementos
matriz = generar_matriz_random(3,3)
suma_total = suma_total = sum(sum(filas) for filas in matriz)
print(matriz)
print(f"La suma total de los elementos de la matriz es: {suma_total}")
print()

#3) Suma de cada fila
matriz = generar_matriz_random(3,3)
print(matriz)
for i, fila in enumerate(matriz):
    print(f"Suma de la fila {i+1}: {sum(fila)}")
print()

#4) Matriz transpuesta
matriz = generar_matriz_random(3,3)
print("Matriz Original")
print(matriz)
print("===================")
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print("Matriz Transpuesta")
print(np.array(transpuesta))
print()

#5) Encontrar el elemento mayor
matriz = generar_matriz_random(3,3)
print(matriz)
mayor = matriz.max()
print(f"El valor más grande de la matriz es {mayor}")
print()

#6) Multiplicar una matriz por un escalar
matriz = generar_matriz_random(3,3)
print("========Matriz Original========")
print(matriz)
escalar = int(input("Ingrese el valor escalar para multiplicar la matriz: "))
matriz_multiplicada = escalar * matriz
print("========Matriz Multiplicada========")
print(matriz_multiplicada)
print()

#7) Diagonal de una matriz cuadrada
matriz = matriz = np.random.randint(1, 101, size=(3,3))
print(f"========Matriz Original========")
print(matriz)
diagonal = np.diag(matriz)
print(f"========Diagonal========")
print(diagonal)
print()

#8) Matriz identidad
n = int(input("Ingrese el tamaño de la matriz: "))
matriz_identidad = np.array([[1 if i == j else 0 for j in range(n)] for i in range(n)])
print(matriz_identidad)

#9) Matriz de indentidad inversa
n = int(input("Ingrese el tamaño de la matriz: "))
matriz_identidad = np.array([[1 if j == n - 1 - i else 0 for j in range(n)] for i in range(n)])
print(matriz_identidad)
print()

#10) Verificar matriz simétrica
matriz = np.array([[1, 2, 3], [2, 5, 4], [3, 4, 9]])
print(matriz)
if np.array_equal(matriz,matriz.T): #array_equal verifica si 2 matrices son iguales. ".T" hace automaticamente el transpuesto de la matriz
    print("La matriz es simétrica.")
else:
    print("La matriz no es simétrica.")
print()

#11) Rotar una matriz 90 grados
matriz = generar_matriz_random(4,4)
print("========Matriz Original========")
print(matriz)
matriz_rotada = np.rot90(matriz, k=-1) #por defecto np.rot90 gira la matriz en sentido antihorario, k=-1 lo invierte al sentido horario
print("========Matriz Rotada========")
print(matriz_rotada)
print()

#12) Analizador y filtrado de calificaciones
notas = "45,88,-5,92,30,110,75,60,15"
notas_lista = notas.split(",")
aprobados = []
reprobados = []
for i in range(len(notas_lista)):
    notas_lista[i] = float(notas_lista[i])
    if 0 > notas_lista[i] or notas_lista[i] > 100:
        continue
    else:
        if notas_lista[i] >= 60:
            aprobados.append(notas_lista[i])
        else:
            reprobados.append(notas_lista[i])
promedio_total = (sum(aprobados+reprobados))/len(aprobados+reprobados)

print(f"Lista de aprobados: {aprobados}")
print(f"Lista de reprobados: {reprobados}")
print(f"El promedio total de las notas válidas es: {promedio_total:.2f}")
print(f"Las ultimas 2 notas aprobadas fueron: {aprobados[-2:]}")
print()

#13) Gestor interactivo de proyectos con while y operador in
tareas = []
while True:
    print("========Menú de Opciones========")
    print("1- Agregar Tarea")
    print("2- Eliminar Tarea")
    print("3- Ver Resumen")
    print("4- Salir")
    eleccion_usuario = float(input("Ingrese su elección: "))
    if eleccion_usuario < 1 or eleccion_usuario > 4:
        print("Error: Número fuera de rango.")
    else:
        match eleccion_usuario:
            case 1:
                nombre_tarea = input("Ingrese el nombre de la tarea que desea agregar: ").title()
                if nombre_tarea in tareas:
                    print(f"Error: {nombre_tarea} ya está en la lista.")
                else:
                    tareas.append(nombre_tarea)
                    print("Tarea guardad con exito.")
            case 2:
                nombre_tarea = input("Ingrese el nombre de la tarea que desea eliminar: ").title()
                if nombre_tarea not in tareas:
                    print(f"Error: {nombre_tarea} no está en la lista.")
                else:
                    confirmacion = input(f"Está seguro de que desea eliminar {nombre_tarea}?(S/N)").upper()
                    if confirmacion == "N":
                        print("Eliminación cancelada")
                    else:
                        tareas.remove(nombre_tarea)
            case 3:
                print(f"Total de tareas registradas: {len(tareas)}")
                print(f"Primeras 3 tareas de la lista: {tareas[:3]}")
            case 4:
                confirmacion = input("¿Esta seguro de que desea salir?(S/N): ").upper()
                if confirmacion == "N":
                    print("Cancelado.")
                else:
                    break