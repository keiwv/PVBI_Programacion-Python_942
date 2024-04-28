'''
4. Generar un script en donde ingrese los 5 números ganadores(lista) del sorteo y muestre
la cantidad de números que acertó al leer el archivo de texto donde se generaron los
conjuntos de 1000 números a participar. La cantidad mínima de aciertos para obtener
un premio son los siguientes:
4.1. El mínimo de aciertos para obtener un premio son 2 aciertos por lista de
números.
4.2. El segundo premio son 3 aciertos.
4.3. El tercer premio son 4 aciertos.
4.4. Y por último el premio mayor es para quien acierte los 5 números de la lista del
sorteo ganador.
'''

import random

listas = []

with open('Ejercicios/Ejercicio 4.1/generateList1000.txt', 'r') as archivo:
    for linea in archivo:
        numbers = list(map(int, linea.strip().split()))
        listas.append(numbers)


def contar_aciertos(lista_ganadora, listas):
    aciertos = [0, 0, 0, 0, 0]  
    for lista in listas:
        num_aciertos = len(set(lista_ganadora) & set(lista))  
        if num_aciertos >= 2 and num_aciertos <= 5: #Tomar en cuenta únicamente del 2 al 5
            aciertos[num_aciertos - 2] += 1  
    return aciertos

lista_ganadora = []
for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista_ganadora.append(numero)

print("la lista ganadora es: ", lista_ganadora)

aciertos = contar_aciertos(lista_ganadora, listas)

for i, numero in enumerate(aciertos):
    print(f"El número de listas con {i + 2} aciertos es: {numero}")