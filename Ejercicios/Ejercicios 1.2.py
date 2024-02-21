# -----------------------------------------------------------------
# Ejercicio 09: Valor entero de un carácter
# (Valor entero de un carácter) HE aquí un avance. En las clases anteriores aprendiste
# sobre las cadenas o strings (str). Cada uno de los caracteres de una cadena tiene una representación
# entera. El conjunto con las representaciones enteras de los caracteres se denominan conjunto de
# caracteres de esa computadora. Puede indicar el valor de un carácter en un programa encerrando ese carácter
# entre comillas, como en 'A'. Para determinar el valor entero de un carácter, utilice la función incorporada ord.

# Muestra los equivalentes enteros de B C D b c d 0 1 2 $ * + y el carácter de espacio.

print('El valor entero de B es: ', ord('B'))
print('El valor entero de C es: ', ord('C'))
print('El valor entero de D es: ', ord('D'))
print('El valor entero de b es: ', ord('b'))
print('El valor entero de c es: ', ord('c'))
print('El valor entero de d es: ', ord('d'))
print('El valor entero de 0 es: ', ord('0'))
print('El valor entero de 1 es: ', ord('1'))
print('El valor entero de 2 es: ', ord('2'))
print('El valor entero de $ es: ', ord('$'))
print('El valor entero de * es: ', ord('*'))
print('El valor entero de + es: ', ord('+'))
print('El valor entero del espacio es: ', ord(' '))

# -----------------------------------------------------------------
#Jercicio 10: Aritmética, más pequeña y más grande
#Escriba un script (guión) que ingrese tres números enteros desde el usuario. Muestre la suma, el promedio
# el producto, el menor y el mayor de los 3 números. Tenga en cuenta que cada uno de estos es una reducción
# en la programación estilo funcional.

num1 = float(input('Ingrese el primer numero: '))
num2 = float(input('Ingrese el segundo numero: '))
num3 = float(input('Ingrese el tercer numero: '))

sum = num1 + num2 + num3
av = sum / 3
prod = num1 * num2 * num3

numMenor = num1
numMayor = num1

if numMenor > num2:
    numMenor = num2
if numMenor > num3:
    numMenor = num3

if numMayor < num2:
    numMayor = num2
if numMayor < num3:
    numMayor = num3

print('La suma de los tres números es: ', sum)
print('El promedio de los tres números es: ', av)
print('El producto de los tres números es: ', prod)
print('El número menor es: ', numMenor)
print('El número mayor es: ', numMayor)

# -----------------------------------------------------------------
# Ejercicio 11: Separar los dígitos de un número entero
# Escriba un script que ingrese un número entero de cinco dígitos desde el usuario. Separa el 
# número en sus dígitos individuales. Imprímelos separados por tres espacios cada uno

num = int(input('Ingrese un número entero de cinco dígitos: '))
num1 = num // 10000
num2 = (num // 1000) % 10
num3 = (num // 100) % 10
num4 = (num // 10) % 10
num5 = num % 10
print(num1, '  ', num2, '  ', num3, '  ', num4, '  ', num5)

# -----------------------------------------------------------------
# Ejercicio 12: 7% de rentabilidad de la inversión
# ALgunos asesores de inversión afirman que es razonable esperar una rentabilidad del 7 a largo plazo
# en el mercado de valores. Suponiendo que empiezas con $100,000 y dejas tu dinero invertido, calcula y vusualiza cuánto dinero tendrás
# al cabo de 10, 20 y 30 años. Utiliza la siguiente fórmula para determinar estas cantidades:
# a = p(1 + r)^n
# donde p es la cantidad original invertida, r es la tasa de interés anual y n es el número de años que el dinero está invertido.
# a es el monto depositado al final del enésimo año.

p = 100000
r = 0.07
a = p * (1 + r) ** 10
print('El monto depositado al final de 10 años es: ', a)
a = p * (1 + r) ** 20
print('El monto depositado al final de 20 años es: ', a)
a = p * (1 + r) ** 30 
print('El monto depositado al final de 30 años es: ', a)

# -----------------------------------------------------------------
# Ejercicio 13: ¿Qué tan grandes pueden ser los enteros en python?
# Use el operador de exponenciación ** con exponentes grandes, pero muy grandes para producir algunos numeros enteros enormes
# y asígnelo a una variable número para ver si python los aceptoa. ¿Encontraste algún valor entero que python no acepte?

numero = 2 ** 14284 # <-- El exponente es el máximo que puede ser ser ejecutado.
print(numero) 
# Si el exponente es mayor a 14284, el programa no se ejecutará.
# Si el exponente es menor a 14284, el programa se ejecutará y se imprimirá un numero con una cantidad de dígitos de 4300 que viene por default.
# Para aumentar la cantidad de dígitos a imprimir, se puede utilizar la función sys.set_int_max_str_digits() para aumentar la cantidad de dígitos a imprimir.

# -----------------------------------------------------------------
# Ejercicio 14: último dígito de un número
# El usuario ingresa un número x tal que regresara el último dígito de ese número
# (utilizar la función print()). Pista: utilizar el operador de residuo (%).

x = int(input('Ingrese un número entero: '))
print('El último dígito de', x, 'es: ', x % 10)

# -----------------------------------------------------------------
# Ejercicio 15: El numero menor de 3 valores
# Se le solicita al usuario ingresar 3 valores (numeros enteros o de punto flotante) y como resultado muestra el
# número menor de esos tres valores.

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = float(input('Ingrese el tercer número: '))

numMenor = num1
if numMenor > num2:
    numMenor = num2
if numMenor > num3:
    numMenor = num3

print('El número menor es: ', numMenor)

# -----------------------------------------------------------------
# Ejercicio 16: Los 3 números son o no son iguales
# Se le solicita al usuario ingresar 3 valores (números enteros o de punto flotante) y como resultado de salida muestra
# si estos tres valores ingresados son iguales o no.

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = float(input('Ingrese el tercer número: '))

prod = num1 * num2 * num3

if prod != (num1 ** 3):
    print('Los tres números son diferentes')

if prod == (num1 ** 3):
    print('Los tres números son iguales')

# -----------------------------------------------------------------
# Ejercicio 17: Establecer en orden ascendente
# (if anidados) Escriba un script que ingrese tres números diferentes de punto flotante desde el usuario
# Muestre los números en orden creciente. Recuerde que el conjunto de  declaraciones if puede contener más de una
# declaración. Demuestre que su script funciona ejecutándolo en los seis ordenamientos posibles
# de los números. ¿Su script funciona con números duplicados?










