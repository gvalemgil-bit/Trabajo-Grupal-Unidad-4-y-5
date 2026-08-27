import random
lista = [random.randint(1,10) for i in range(10)]
revisados = set()
duplicados = set()
for i in range(len(lista)):
    if lista[i] in revisados:
        duplicados.add(lista[i])
    else:
        revisados.add(lista[i])
print(f"Lista: {lista}")

duplicados = list(duplicados)
print(f"Lista original: {lista}")
if not duplicados:
    print("No hay números repetidos.")
else:
    print(f"Los números repetidos son: {duplicados}")