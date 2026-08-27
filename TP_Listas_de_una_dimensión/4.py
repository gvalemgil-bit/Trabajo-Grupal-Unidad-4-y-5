#4) Contar elementos pares e impares
lista_numeros = []
detener = False
pares = 0
impares = 0
print("A continuación, ingrese los números de la lista. Escriba DETENER para finalizar.")
while not detener:
    numero_usuario = input("Ingrese un número: ")
    if numero_usuario.upper() == "DETENER":
        detener = True
    else:
        numero_usuario = int(numero_usuario)
        lista_numeros.append(numero_usuario)
for i in range(len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Lista: {lista_numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")