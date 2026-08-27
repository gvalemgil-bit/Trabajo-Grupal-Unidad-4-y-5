#2) Encontrar el mayor y el menor
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
        print(lista_numeros)

print(f"El mayor número de la lista es {max(lista_numeros)}, y el menor es {min(lista_numeros)}.")