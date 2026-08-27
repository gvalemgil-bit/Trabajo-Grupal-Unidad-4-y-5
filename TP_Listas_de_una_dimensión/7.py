#7) Promedio de una lista
lista_numeros = []
detener = False
print("A continuación, ingrese los números de la lista. Escriba DETENER para finalizar.")
while not detener:
    numero_usuario = input("Ingrese un número: ")
    if numero_usuario.upper() == "DETENER":
        detener = True
    else:
        numero_usuario = float(numero_usuario)
        lista_numeros.append(numero_usuario)
promedio = sum(lista_numeros)/len(lista_numeros)
print(f"Lista: {lista_numeros}")
print(f"El promedio de la lista es: {promedio}")