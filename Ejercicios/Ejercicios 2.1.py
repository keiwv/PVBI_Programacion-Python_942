# Utiliza la sentancia de repeticion while(mientras) para imprimir
# en pantalla los enteros del 1 al 5 (de forma ascendete) incrementando en 1.
# La salida es la siguiente:
# 1 
# 2
# 3
# 4
# 5

print("\n")
count = 1
maxNums = 5

while count <= maxNums:
    print(count)
    count = count + 1


# Utiliza la sentencia de repeticion while(mientras) para imprimir en pantalla los enteros del 5 al 1 (de forma descente)
# decrementando en 1. La salida en pantalla es la siguiente:
# 5
# 4
# 3
# 2
# 1

count = 5
minimum = 1

print("\n")
while count >= minimum:
    print(count)
    count = count - 1 

print("\n")
# Utiliza la sentencia de repeteción while (mientras) para imprimir
# en pantalla los enteros del 1 al 5 (de forma ascendete) incrementando
# en 1 separado por comas. La calida en pantalla es la siguiente.
# 1, 2, 3, ,4 , 5;

count = 1
maxNums = 5
text = ''

while count <= maxNums:
    text = text + str(count)
    if(count != maxNums):
        text = text + ', '
    count =  count + 1;
print(text)

print("\n")
# Utiliza la sentencia de repeteción while (mientras) para imprimir
# en pantalla los enteros del 1 al 5 (de forma descendente) incrementando
# en 1 separado por comas. La calida en pantalla es la siguiente.
# 5, 4, 3, 2, 1

count = 5
maxNums = 1
text = ''
while count >= maxNums:
    text = text + str(count)
    if(count != maxNums):
        text = text + ', '
    count =  count - 1;
print(text)

# (Sumatoria) Solicitar al usuario un numero entero para calcular la
# sumatoria.
# Primero deberá realizar el pseudocódigo de este ejercicio
# y después su solución en python
print("\n")

num = int(input("Ingrese un numero por favor para hacer la sumatoria: "))

count = 0
result = 0
while (num >= count):
    result = result + count
    count = count + 1
print("El resultado es: ", result);

# Encontrar detalle que se debe modificar en el siguiente codigo en Python

renglon=0
maximo_renglon=10
maximo_columna=16
cadena_renglon_columna=""

while renglon < maximo_renglon:
    columna=0
    while columna < maximo_columna:
        cadena_renglon_columna= cadena_renglon_columna + '♥' + ' '
        columna = columna +1
    cadena_renglon_columna=cadena_renglon_columna + '\n'
    renglon = renglon+1
print(cadena_renglon_columna)


# Generar un escript donde el usuario ingresa dos tdatos de entrada:
# * Nombre completo
# * Carácter que será el marco que rodea el nombre completo.
# UN ejemplo de salida es el siguiente: 
# Ingrese su nombre completo: Cesar ANtillon Macias
# Teclee un solo carácter que será su marco alrededor del nombre: *
# ***********************
# *Cesar Antillon Macias*
# ***********************

name = input("Ingrese su nombre por favor: ")
characterName = input("Ingrese el símbolo que desea alrededor de su nombre: ")
lenghtName = len(name) + 1
print(lenghtName)

count = 0
text = ''

while lenghtName >= count:
    text = text + characterName + ''
    count = count + 1

print()
text = text + "\n"
text = text + characterName + '' + name + characterName
text = text + "\n"
count = 0
while lenghtName >= count:
    text = text + characterName + ''
    count = count + 1  
print(text)


# Escriba un script para que imprima una figura de rombo donde debe
# leer un número impar de manera que especifique el numero de filas en el rombo
# y también debe leer e carácter con el quqe pintará el rombo.

limite = int(input("Ingrese un numero impar para establecer la longitud horizontal más larga del rombo: "))
simbolo = input("Ingrese el carácter que tendrá el rombo: ")

if (limite % 2 == 0):
    print("El numero no es impar")

else:
    i = 1
    while i <= limite:
        print((simbolo * i).center(limite, ' '))
        i += 2

    i = limite - 2
    while i > 0:
        print((simbolo * i).center(limite, ' '))
        i -= 2
