
'''
2. Generar 1000 listas de 5 números y mostrarlos como dato de salida.
2.1. El conjunto de 1000 listas deberán estar ordenadas de forma ascendente.
2.2. Guardar las 1000 listas en un archivo .txt. Defina una función que escriba las
listas generadas(escribirListasEnArchivoTXT(archivo, listas)).
2.3. No deberá repetirse ninguna lista de 5 números en el conjunto de 1000 listas.
Podria definir una función verificarListaRepetida(ubicación_de_archivo,
listas) que regrese un booleano para validar que no se encuentre de la segunda
lista en adelante repetida. Podría utilizar listas bidimensionales para manejar
cada lista de 5 números que se encuentran en la lista. Sugerencia de funciones
a utilizar: strip(), split(' '), archivoListas.seek(0), archivoListas.readlines(),
enumerate() en el ciclo for y las listas de comprensión.
'''



import random

def generarLista():
    lista = []
    while len(lista) < 5:
        elemento = random.randint(1, 28)
        lista.append(elemento)
    lista.sort()
    return lista

def listaRepetidoEnLista(lista1:list, lista2:list):
    return lista2 in lista1

listaFile = []
while len(listaFile) < 1000:
    lista = generarLista()
    if not (listaRepetidoEnLista(listaFile, lista)):
        listaFile.append(lista)

listaFile.sort()

with open('Ejercicios/Ejercicio 4.1/generateList1000.txt', 'w') as archivo:
    for lista in listaFile:
        for elemento in lista:
            archivo.write(str(elemento) + ' ')
        archivo.write('\n')