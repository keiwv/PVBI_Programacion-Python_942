# -----------------------------------------------------------------
# Ejercicio 1
# ¿qué hace el siguiente código? Crea las variables x = 2
# e y = 3, y luego determina lo que muestra cada una de las siguientes declaraciones

x = 2
y = 3

print("x = ", x) # Output: "x = 2"
print("Value of", x, "+", x, "is", (x + x)) # Output: "Value of 2 + 2 is 4" 
print("x = ") # Output: "x = "
print((x + y), "=", (y + x)) # Output: "5 = 5"

# -----------------------------------------------------------------
# Ejercicio 2
# ¿Qué hay de malo con este código? El siguiente código debe leer un entero en la variable de calificación
# calificacion = input('Ingrese una calificación entera entre 1 y 100: ')
# El problema con este código, es que la función input guardará el valor como una cadena/string.
# y no guardará el valor como entero. 
calificacion = (int(input('Ingrese una calificación entera entre 1 y 100: ')))
# -----------------------------------------------------------------
# Ejercicio 3
# (Complete el código faltante) Reemplace *** en el siguiente código con
# una sentencia que imprimirá un mensajae como '¡Felicidades! tu calificación de 91 te otorga 
# una A en este curso'. Su declaración debe imprimir un valor almacenado en la variable calificación

if calificacion >= 90:
    print('¡Felicidades! tu calificación de', calificacion, 'te otorga una A en este curso')

# -----------------------------------------------------------------
# Ejercicio 4
# (Área, diámetro y circunferencia del círculo) Para un círculo de radio 2, muestre el díametro, la circunferencia y el área.
# Utilice el valor 3.14159 para PI. Utilice las siguientes fórmulas: 
# (r es el radio): diametro = 2r, circunferencia = 2πr, área = PIr^2

r = (float(input('Ingrese el radio del círculo: ')))

PI = 3.14159
diametro = 2 * r
circunferencia = 2 * PI * r
area = PI * (r ** 2)

print('El radio introducido es: ', r)
print('PI: ', PI)
print('Diametro: ', diametro)
print('Circunferencia: ', circunferencia)
print('Área: ', area)

# -----------------------------------------------------------------
# Ejercicio 5
# (Par o impar) Utilice sentencias if para determinar si un número entero es par o impar.
# [Sugerencia: utilice el operador residuo. Un número par es multiple de 2. Cualquier múltiple de 2 deja
# un residuo de 0 cuando se divide entre 2]

numero = (int(input('Ingrese un número entero para conocer si es par o impar: ')))

if (numero % 2) == 0:
    print('El número', numero, 'es par')

if (numero % 2) != 0:
    print('El número', numero, 'es impar')
# -----------------------------------------------------------------
# Ejercicio 6
# (Multiplos) Utilice sentencias if para determinar si 1024 es múltiplo de 4 y si 2 es
# múltiplo de 10. (Sugerencia: utilice el operador residuo)
num1 = int(input('Ingrese el primer entero: '))
num2 = int(input('Ingrese el segundo entero: '))

if (num1 % num2) == 0:
    print(num2, 'es múltiplo de', num1)

if (num1 % num2) != 0:
    print(num2, 'no es múltiplo de', num1)

# -----------------------------------------------------------------
# Ejercicio 7
# (Tabla de cuadrados y cubos) Escriba un guión (script) que calcule los cuadrados y cubos
# de los números de 0 al 5. Imprima los valores resultantes en formato de tabla, como se muestra a continuación
# Utilice la secuencia de escape de tabulación para lobrar resultado de tres columnas.
    
print('numero', '\t', 'cuadrado', ' ', 'cubo')
print(f"{0:1}\t{0:2}\t{0:5}")
print(f"{1:1}\t{1:2}\t{1:5}")
print(f"{2:1}\t{4:2}\t{8:5}")
print(f"{3:1}\t{9:2}\t{27:6}")
print(f"{4:1}\t{16:3}\t{64:6}")
print(f"{5:1}\t{25:3}\t{125:7}")

# -----------------------------------------------------------------
# Ejercicio 8
# Muestra cómo "alinear a la derecha" los números. Podrías
# intentarlo aquí como un reto extra.
print('numero', '\t', 'cuadrado', ' ', 'cubo')
print(f"{0:>6}\t{0:>9} {0:>6}")
print(f"{1:>6}\t{1:>9} {1:>6}")
print(f"{2:>6}\t{4:>9} {8:>6}")
print(f"{3:>6}\t{9:>9} {27:>6}")
print(f"{4:>6}\t{16:>9} {64:>6}")
print(f"{5:>6}\t{25:>9} {125:>6}")

# -----------------------------------------------------------------
