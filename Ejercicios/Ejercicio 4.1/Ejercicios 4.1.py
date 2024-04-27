import random

def generarLista():
    lista = []
    while len(lista) < 5:
        elemento = random.randint(1, 28)
        if not (elementoRepetidoEnLista(lista,elemento)):
            lista.append(elemento)
    lista.sort()
    print(lista)
    return lista

def elementoRepetidoEnLista(lista:list, elemento:int):
    return elemento in lista

def listaRepetidoEnLista(lista1:list, lista2:list):
    return lista2 in lista1

listaFile = []
while len(listaFile) < 1000:
    lista = generarLista()
    if not (listaRepetidoEnLista(listaFile, lista)):
        listaFile.append(lista)

listaFile.sort()


with open('Ejercicios/Ejercicio 4.1/lista.txt', 'w') as archivo:
    for lista in listaFile:
        for elemento in lista:
            archivo.write(str(elemento) + ' ')
        archivo.write('\n')