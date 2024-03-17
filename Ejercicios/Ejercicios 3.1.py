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

# -----------------------------------------------------------------------------
# Ejercicio 34
# Ingrese un número entero que contenga 0 y 1 (es decir, un número entero
# “binario”) y muestre su equivalente decimal. [Sugerencia: utilice los
# operadores de residuo y división(o división de piso) para seleccionar los dígitos
# del número "binario" uno a la vez, de derecha a izquierda. Así como en el
# sistema numérico decimal, donde el dígito más a la derecha tiene el valor
# posicional 1 y el siguiente dígito a la izquierda tiene el valor posicional 10,
# luego 100, luego 1000, etc., en el sistema numérico binario, el dígito más a la
# derecha tiene el valor posicional 1, el siguiente dígito a la izquierda tiene el
# valor posicional 2, luego 4, luego 8, etc. Por lo tanto, el número decimal 234 se
# puede interpretar como 2 * 100 + 3 * 10 + 4 * 1. El decimal equivalente del
# binario 1101 es 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.] NOTA: No utilizar la función
# reversed().

binary_number = input("Ingrese un número binario (conteniendo solo 0 y 1): ")


number_decimal = 0

for index in range(len(binary_number)):
    digit_binary = int(binary_number[index])
    value = 2 ** (len(binary_number) - index - 1)
    number_decimal += digit_binary * value

print(f"El número decimal equivalente de {binary_number} es: {number_decimal}")

# -----------------------------------------------------------------------------
# Ejercicio 35
# Ingrese un número(es decir, un entero positivo) y muestre su equivalente en
# binario. [Sugerencia: utilice los operadores de residuo y división(o división de
# piso) para seleccionar los dígitos del número entero uno a la vez, de derecha a
# izquierda. Por lo tanto, el número decimal 234 se puede interpretar como 2 *
# 100 + 3 * 10 + 4 * 1. El decimal equivalente del binario 1101 es 1 * 8 + 1 * 4 + 0
# * 2 + 1 * 1.] NOTA: No utilizar la función reversed().

number = int(input("Ingresa un número en decimal: "))

bit1 = "1"
bit0 = "0"
result = ''

while number != 0:
    if number % 2 == 1:
        result = result + bit1
        number = int(number // 2)
    else:
        result = result + bit0
        number = int(number // 2)

sizeString = len(result) - 1
result2 = ""
while sizeString >= 0:
    result2 = result2 + result[sizeString]
    sizeString = sizeString - 1

print("Representación binaria invertida:", result2)

# -----------------------------------------------------------------------------
# Ejercicio 36
# Capicúa es un término que hace referencia a aquel número que resulta
# idéntico cuando se lee de derecha a izquierda y de izquierda a derecha.
# Implemente un script donde el usuario ingrese un número entero positivo y
# determine si es capicúa o no. Por ejemplo la matrícula del maestro es 311113
# por lo tanto es capicúa!
# Sugerencia: Los operadores // y % le podrían ayudar.
# NOTA: No utilizar la función reversed().

number = str(input("Ingresa un numero para saber si es capicúa: "))

length = len(number)
isCapicua = True


for index in range(length // 2):
    if number[index] != number[length - 1 - index]:
        isCapicua = False

if isCapicua:
    print(f"El numero {number} es Capicúa")
else:
    print(f"El numero {number} no es Capicúa")

# -----------------------------------------------------------------------------
# Ejercicio 37
# Se le llama palíndromo a la palabra o frase cuyas letras están dispuestas de tal
# manera que resulta la misma leída de izquierda a derecha que de derecha a
# izquierda. Por ejemplo:
# ● Anita lava la tina
# ● La ruta nos aportó otro paso natural
# Implemente un script donde el usuario ingresa una palabra o frase y determine
# si es palindromo o no.
# NOTA: Al ingresar la palabra o frase, no deberá tener acentos, tildes, diéresis y
# mayúsculas. Los espacios si están permitidos. No utilizar la función reversed(),
# y tampoco listas.

text = str(input("Ingresa un texto para saber si es palíndromo: "))

length = len(text)
text = text.lower()
isPalindrome = True
finaltext = ''

for index in range(length):
    if text[index] != ' ':
        finaltext = finaltext + text[index]

length = len(finaltext)

for index in range(length):
    if finaltext[index] != finaltext[length - index - 1]:
        isPalindrome = False
    
if isPalindrome:
    print(f"El texto '{text}' es un palíndromo.")
else:
    print(f"El texto '{text}' no es un palíndromo.")

