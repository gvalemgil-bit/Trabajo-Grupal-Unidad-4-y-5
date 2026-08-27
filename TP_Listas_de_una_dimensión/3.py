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

print(f"La lista original es: {lista_numeros}")
lista_numeros.reverse()
print(f"El reverso de la lista es {lista_numeros}")