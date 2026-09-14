alumnos = {60902: "Rodolfo Fernandez",61654: "Luis Gomez", 61852: "Andrea Pereira",61754: "Juan Cruz Gonzales"}
notas_finales = [["Rodolfo Fernandez"],["Luis Gomez"],["Andrea Pereira"],["Juan Cruz Gonzales"]]
for legajo in alumnos:
    print(alumnos[legajo])
    nota_mas_alta = 0
    nota_valida = True
    materias = [["Ciencias"],["Historia"],["Geografía"],["Matemáticas"],["Física"]]
    promedio_final = []
    for materia in range(len(materias)):
        nota_valida = True
        while nota_valida:
            nota1 = float(input(f"Ingrese la primer nota de {materias[materia][0]}: "))
            nota2 = float(input(f"Ingrese la segunda nota de {materias[materia][0]}: "))
            if (nota1 > nota2 or nota1 == nota2) and nota1 > nota_mas_alta:
                nota_mas_alta = nota1
            elif nota2 > nota_mas_alta:
                nota_mas_alta = nota2
            if  10 < nota1 or nota1 < 0 or 10 < nota2 or nota2 < 0:
                print("Error: Notas fuera de rango.")
            else:
                nota_valida = False 
        promedio = (nota1 + nota2) / 2
        materias[materia].append(nota1)
        materias[materia].append(nota2)
        materias[materia].append(promedio)
        promedio_final.append(nota1)
        promedio_final.append(nota2)
    promedio_final_suma = sum(promedio_final)
    promedio_final_division = promedio_final_suma / len(promedio_final)
    for i in range(len(notas_finales)):
        if notas_finales[i][0] == alumnos[legajo]:
            notas_finales[i].append(promedio_final_division)
    print(f"Notas de {alumnos[legajo]}:")
    for i in range(len(materias)):
        nombre_materia = materias[i][0]
        nota_1_materia = materias[i][1]
        nota_2_materia = materias[i][2]
        promedio_materia = materias[i][3]
        print(nombre_materia,nota_1_materia,nota_2_materia,promedio_materia)
    print(f"Nota mas alta: {nota_mas_alta}")
    print()
mejor_promedio = [notas_finales[0]]

for i in range(1, len(notas_finales)):
    if notas_finales[i][1] > mejor_promedio[0][1]:
        mejor_promedio = [notas_finales[i]]  
    elif notas_finales[i][1] == mejor_promedio[0][1]:
        mejor_promedio.append(notas_finales[i]) 
if len(mejor_promedio) == 1:
    print(f"El alumno con el mejor promedio es {mejor_promedio[0][0]}, con un promedio final de {mejor_promedio[0][1]}")
else:
    print("Los alumnos con el mejor promedio son:")
    for estudiante in mejor_promedio:
        nombre = estudiante[0]
        nota = estudiante[1]
        print(nombre, nota)

