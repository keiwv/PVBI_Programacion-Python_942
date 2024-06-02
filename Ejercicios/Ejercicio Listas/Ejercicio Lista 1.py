
'''
1. Generar un script en Python que seleccione y muestre 5 números aleatorios de 1 al 28
en una lista(por ejemplo: [1,5,13,19,24]) el cual debe cumplir los siguientes criterios:
1.1. Crear una función llamada generaLista() que devuelva una lista de 5 números
que se encuentre entre el 1 al 28. En esta parte puede usar las siguientes
funciones: random.randint(), random.choice(lista),
lista.append(elementoLista).
1.2. Cada elemento de la lista deberá estar ordenada de forma ascendente(puede
utilizar la función sorted(lista, reverse=False).
1.3. Crear una función elementoRepetidoEnLista(lista, elemento) que devuelva un
booleano(True o False) para que los 5 números no puedan repetirse al ser
seleccionados en la lista(por ejemplo: [3,7,18,22,22]).
1.4. Escribir la lista generada de 5 números en un archivo .txt de la siguiente forma:
'''


import random

def generarLista():
    lista = []
    while len(lista) < 5:
        elemento = random.randint(1, 28)
        lista.append(elemento)
    lista.sort()
    return lista

listaFile = generarLista()

with open('Ejercicios/Ejercicio Listas/generateList.txt', 'w') as archivo:
    for elemento in listaFile:
        archivo.write(str(elemento) + ' ')
    archivo.write('\n')