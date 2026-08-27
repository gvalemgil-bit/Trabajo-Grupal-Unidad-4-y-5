import random
lista = [random.randint(1,10) for i in range(10)]
print(f"Lista: {lista}")
multiplo = float(input("Eliga un número para multiplicar los elementos de la lista: "))
for i in range(len(lista)):
    lista[i] = lista[i] * multiplo
print(f"Lista multiplicada por {multiplo}: {lista}")