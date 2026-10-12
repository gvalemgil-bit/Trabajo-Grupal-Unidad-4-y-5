# TP - POO en Python

Trabajo práctico de Programación Orientada a Objetos resuelto en Python 3.
Cada ejercicio está en su propia carpeta y las clases están en archivos separados (como lo pide el TP).

## Estructura

```
Ejercicio1/
  celda.py        -> clase Celda (fila, columna, valor)
  matriz.py       -> clase Matriz (lista celdasMatriz + método getValor)
  principal.py    -> programa principal (carga, validación y consulta)

Ejercicio2/
  nota.py         -> clase Nota (catedra, notaExamen)
  alumno.py       -> clase Alumno (nombreCompleto, legajo, notas[]) + promedio()
  carga_notas.py  -> clase con el método main

Ejercicio3/
  ingrediente.py      -> clase Ingrediente (nombre, cantidad, unidadMedida)
  plato.py            -> clase Plato (nombreCompleto, precio, esBebida, ingredientes[])
  menu_restaurant.py  -> clase con el método main

Ejercicio4/
  componente_cpu.py    -> clase ComponenteCPU (componente, marca, cantidad, precio)
  computadora.py       -> clase Computadora (marca, modelo, componentes[]) + costo y precio de venta
  costo_computadora.py -> clase con el método main

Ejercicio5/
  habitacion.py -> clase Habitacion (nombre, metrosCuadrados)
  vivienda.py   -> clase Vivienda + getMetrosCuadradosCubiertos() (lanza excepción)
  barrio.py     -> clase Barrio + getSuperficieTotalTerreno(),
                   getSuperficieTotalTerrenoXManzana(), getSuperficieTotalCubierta()
  principal.py  -> clase Principal que crea los objetos y ejecuta los métodos
```

## Cómo ejecutar

Desde la carpeta de cada ejercicio (para que encuentre los imports):

```bash
cd Ejercicio1
python principal.py

cd ../Ejercicio2
python carga_notas.py

cd ../Ejercicio3
python menu_restaurant.py

cd ../Ejercicio4
python costo_computadora.py

cd ../Ejercicio5
python principal.py
```

## Observaciones

- Los programas son interactivos: piden los datos por consola hasta que se responde `NO`
  (o se escribe `FIN` en el ejercicio 1).
- Se validan los datos numéricos (enteros y decimales) y las respuestas `SI/NO`.
- Ejercicio 1: no se permite cargar dos veces la misma fila y columna.
- Ejercicio 2: siempre se carga al menos 1 nota por alumno y se muestra su promedio.
- Ejercicio 3: si el plato no es bebida debe tener al menos 1 ingrediente.
- Ejercicio 4: costo + 40% si el costo es menor a 50000; costo + 30% en otro caso.
- Ejercicio 5: `getMetrosCuadradosCubiertos()` lanza la excepción
  *"La superficie cubierta no puede ser mayor a la superficie del terreno"*.
