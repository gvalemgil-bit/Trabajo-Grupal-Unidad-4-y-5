def generar_lista_usuario(): #Para evitar repetir código, creé esta función para generar las listas.
    print("A continuación, ingrese los números de la lista. Escriba DETENER para finalizar.")
    detener = False
    while not detener:
        numero_usuario = input("Ingrese un número: ")
        if numero_usuario.upper() == "DETENER":
            detener = True
        else:
            numero_usuario = float(numero_usuario)
            lista_numeros.append(numero_usuario)
            print(lista_numeros)

#1) Suma de elementos
lista_numeros = []
generar_lista_usuario()
suma =  sum(lista_numeros)
print(f"La suma de los números en la lista es: {suma}")
print()

#2) Encontrar el mayor y el menor
lista_numeros = []
generar_lista_usuario()
print(f"El mayor número de la lista es {max(lista_numeros)}, y el menor es {min(lista_numeros)}.")
print()

#3) Invertir una lista
lista_numeros = []
generar_lista_usuario()
print(f"La lista original es: {lista_numeros}")
lista_numeros.reverse()
print(f"El reverso de la lista es {lista_numeros}")
print()

#4) Contar elementos pares e impares
lista_numeros = []
pares = 0
impares = 0
generar_lista_usuario()
for i in range(len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Lista: {lista_numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print()

#5) Multiplicar elementos por un valor
import random
lista = [random.randint(1,10) for i in range(10)]
print(f"Lista: {lista}")
multiplo = float(input("Eliga un número para multiplicar los elementos de la lista: "))
for i in range(len(lista)):
    lista[i] = lista[i] * multiplo
print(f"Lista multiplicada por {multiplo}: {lista}")
print()

#6) Eliminar duplicados
lista_numeros = []
generar_lista_usuario()
lista_sin_duplicados = list(set(lista_numeros))
print(f"Lista original: {lista_numeros}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")
print()

#7) Promedio de una lista
lista_numeros = []
generar_lista_usuario()
promedio = sum(lista_numeros)/len(lista_numeros)
print(f"Lista: {lista_numeros}")
print(f"El promedio de la lista es: {promedio}")
print()

#8) Encontrar elementos repetidos
lista = [random.randint(1,10) for i in range(10)]
revisados = set()
duplicados = set()
for i in range(len(lista)):
    if lista[i] in revisados:
        duplicados.add(lista[i])
    else:
        revisados.add(lista[i])
duplicados = list(duplicados)
print(f"Lista original: {lista}")
if not duplicados:
    print("No hay números repetidos.")
else:
    print(f"Los números repetidos son: {duplicados}")
print()

#9) Lista de números primos
def numeros_primos(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        if lista[i] <= 1:
            lista_compuestos.append(lista[i])
        for j in range(2,lista[i]):
            if lista[i] % j == 0:
                lista_compuestos.append(lista[i])
                break
        if lista[i] not in lista_compuestos:
            lista_primos.append(lista[i])

lista_primos = []
lista_compuestos = []
lista_numeros = []
generar_lista_usuario()
numeros_primos(lista_numeros)
print(f"Lista original: {lista_numeros}")
print(f"Lista de números primos: {lista_primos}")
print(f"Lista de números compuestos: {lista_compuestos}")
print()

#10) Eliminar un elemento por su índice
lista_numeros = []
generar_lista_usuario()
print(f"Lista original: {lista_numeros}")
indice = int(input("Indíque el número del índice que desea eliminar: "))
lista_numeros.remove(lista_numeros[indice])
print(f"Lista nueva: {lista_numeros}")
print()

#11) Contar ocurrencias de un elemento
lista_numeros = []
generar_lista_usuario()
numero_repetido = float(input("Ingrese el número cuyas repeticiones quiere saber: "))
veces_repetido = 0
for i in range(len(lista_numeros)):
    if lista_numeros[i] == numero_repetido:
        veces_repetido += 1

print(f"Cantidad de {numero_repetido} en la lista: {veces_repetido}")
print()

#12) Sumar listas elemento por elemento
lista_1 = [random.randint(1,100) for i in range(10)]
lista_2 = [random.randint(1,100) for i in range(10)]
suma_elementos = 0
suma_total = 0
print(f"Primera lista: {lista_1}")
print(f"Segunda lista: {lista_2}")
for i in range(10):
   suma_elementos = lista_1[i] + lista_2[i]
   suma_total += suma_elementos
   print(f"{lista_1[i]} + {lista_2[i]} = {suma_elementos}")

print(f"La suma total de las sumas de cada elemento es: {suma_total}")
print()

#13) Explique y ejemplifique la librería Numpy para trabajar con matrices y arrays
print("NumPy es una biblioteca especializada en el cálculo numérico y el manejo de grandes volúmenes de datos estructurados en vectores y matrices.")

print("======Ejemplos======")
import numpy as np
print("Crear un array de una dimensión")
vector = np.array([1, 2, 3, 4, 5])
print(vector)
print()
print("Sumar, restar o multiplicar sin usar for")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

suma = a + b
print(f"Suma: {suma}")  

multiplicacion = a * 2
print(f"Multiplicación: {multiplicacion}") 