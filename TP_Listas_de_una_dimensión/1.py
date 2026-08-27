#1) Suma de elementos
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

suma =  sum(lista_numeros)
print(f"La suma de los números en la lista es: {suma}")