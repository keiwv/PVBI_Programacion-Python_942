# Comenzando con 200 bacterias, el crecimientoen el número de bacterias
# después de n horas se calcula de la siguiente manera: B = 200 * 2n. Imprima la cantidad
# de bacterias dspués de 0, 5, 10 y 15 horas en forma de tabla como se muestra a continuación
# Utilice las siguientes de escape de tabulación para lograr el resultado de dos columnas.

print("Horas\t Numero de bacterias")

for n in range(0, 16, 5):
    total = 200 * (2 ** n)
    print(n, "\t", total)


# Reimplementar el script utilizando f-strings en el cual se muestre de la siguiente manera:
print("\nHoras\t Numero de bacterias")

for n in range(0, 16, 5):
    total = 200 * (2 ** n)
    print(f'{n:5d}\t{total:20d}')


# -----------------------------------------------------------------------------
# EJERCICIO 31
# Escriba un script que ingrese una cantidad desegundos desde el usuario.
# Calcula el numero de horas, minutos y segundos restantes. Imprimelos separados por "-"
# Por ejemplo, si el usuario escribe 3750 segundos como entrada, el script deberá imprimir 1 - 2 - 30
# -----------------------------------------------------------------------------
userInput = int(input("Ingresa el tiempo en segundos: "))

hours = userInput // 3600

seconds_left = userInput % 3600

minutes = seconds_left // 60

seconds = seconds_left % 60

print(f'{hours} - {minutes} - {seconds}')
# -----------------------------------------------------------------------------
# Ejercicio 32
# Escribió un script que calculaba la cantidad de horas, minutos y segundos
# restantes en función de la cantidad de segundos recibidos a través de la
# entrada del usuario. Vuelva a implementar su script para usar un bucle que en
# un proceso iterativo "recoja" las horas, minutos y segundos restantes usando
# los operadores // y %.

userInput = int(input("Ingresa el tiempo en segundos: "))

hours = 0
minutes = 0
seconds = 0

for _ in range(userInput // 3600):
    hours += 1
    userInput -= 3600

for _ in range(userInput // 60):
    minutes += 1
    userInput -= 60

seconds = userInput

print(f'{hours} - {minutes} - {seconds}')

# -----------------------------------------------------------------------------
# Ejercicio 33
# En teoría de números, un número perfecto es un número entero positivo que
# es igual a la suma de sus divisores. Los pitagóricos estudiaron por primera vez
# los números perfectos, quienes pensaban que tenían propiedades místicas.
# También fueron ampliamente estudiados por los griegos (incluido Euclides) por
# sus propiedades numerológicas.
# 
# El número perfecto más pequeño es 6, porque 6 = 3 + 2 + 1, siendo 3, 2 y 1 los
# divisores. Otros ejemplos de números perfectos son: 28, 496 y 8128. Escriba un
# script que ingrese un número entero no negativo y muestre si es un número
# perfecto o no.


userInput = int(input("Ingrese un entero positivo para saber si es un número perfecto: "))
sum_div = 1

if userInput > 0:
    for i in range(2, int(userInput/2) + 1):
        if userInput % i == 0:
            sum_div += i
    if userInput == sum_div:
        print(f"{userInput} es un número perfecto.")
    else:
        print(f"{userInput} no es un número perfecto.")
else:
    print("Por favor, ingrese un número entero no negativo.")


