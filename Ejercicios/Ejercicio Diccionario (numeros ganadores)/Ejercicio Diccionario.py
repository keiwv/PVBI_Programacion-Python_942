
''' CONTAR CUANTAS VECES SE REPITE CADA COMBINACIÓN EN CADA GRUPO
    ASUMIENDO QUE SON 2 2 1 '''

from collections import Counter

def obtener_combinaciones(datos, grupo):
    combinaciones = []
    for fila in datos:
        combinacion = tuple(fila[i] for i in grupo)
        combinaciones.append(combinacion)
    return combinaciones

grupo1 = range(1, 10)
grupo2 = range(10, 20)
grupo3 = range(20, 29)

with open('C:\\Repositorios\\PVBI_Programacion-Python_942\\Ejercicios\\Ejercicio Diccionario (numeros ganadores)\\2 2 1 ganadores chispazo.txt', 'r') as archivo:
    lineas = archivo.readlines()

datos = [[int(num) for num in linea.split()] for linea in lineas]

conteo_grupo1 = Counter(obtener_combinaciones(datos, [0, 1]))
conteo_grupo2 = Counter(obtener_combinaciones(datos, [2, 3]))
conteo_grupo3 = Counter(obtener_combinaciones(datos, [4]))

print("Grupo 1:")
for combinacion, conteo in conteo_grupo1.items():
    print(f"{combinacion}: {conteo}")

print("\nGrupo 2:")
for combinacion, conteo in conteo_grupo2.items():
    print(f"{combinacion}: {conteo}")

print("\nGrupo 3:")
for combinacion, conteo in conteo_grupo3.items():
    print(f"{combinacion}: {conteo}")
