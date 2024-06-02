'''
3. Modificar la función generaLista() para que seleccione ciertos números en los
siguientes tres grupos:

3.1. Habra 3 grupos:
3.1.1. El primer grupo tendrá números del 1 al 9.
3.1.2. El segundo grupo tendrá números del 10 al 19.
3.1.3. El tercer grupo tendrá números del 20 al 28.
3.2. Generar 100 lista de números con el grupo 2 2 1. 2 2 1 significa lo siguiente:
3.2.1. Tendrá que escoger al azar 2 números del grupo 1 al 9.
3.2.2. Tendrá que escoger al azar 2 números del grupo 10 al 19.
3.2.3. Tendrá que escoger al azar un número del grupo 20 al 28.
3.2.4. En la función generaLista() se podrá modificar el grupo 2 2 1 por
otro(ejemplo 2 1 2, 1 2 2, 1 3 1, 4 0 1).
'''

import random

def generaLista(num1, num2, num3):
    lista = []
    while len(lista) < 5:
        for i in range(num1):
            numero = random.randint(1, 9)
            lista.append(numero)
        for i in range(num2):
            numero = random.randint(10, 19)
            lista.append(numero)
        for i in range(num3):
            numero = random.randint(20, 28)
            lista.append(numero)
    return lista 

# Verificar repetición de listas.
def listaRepetidoEnLista(lista1, lista2):
    return lista2 in lista1

listas_generadas = []

# Generar 100 listas de 5 numeros y mostrarlos como datos de salida
for _ in range(100):
    lista_generada = generaLista(2, 2, 1)
    listas_generadas.append(lista_generada)
    print(lista_generada)

listas_generadas.sort()

with open('Ejercicios/Ejercicio Listas/lista.txt', 'w') as archivo:
    for lista in listas_generadas:
        archivo.write(' '.join(map(str, lista)) + '\n')
