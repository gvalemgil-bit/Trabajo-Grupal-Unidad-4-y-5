#6) Eliminar duplicados
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

lista_sin_duplicados = list(set(lista_numeros))
print(f"Lista original: {lista_numeros}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")