
# *************************************************************
num1 = int(input("Ingresa un numero: "));

if (num1 % 2) == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# *************************************************************
num1 = int(input("Ingrese el primer entero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    if (num1 % num2) == 0:
        print(num2, "es multiplo de ", num1)
    else:
        print(num2, "no es multiplo de ", num1)
else:
    if (num2 % num1) == 0:
        print(num1, "es multiplo de ", num2)
    else:
        print(num1, "no es multiplo de ", num2)

# *************************************************************

num1 = int(input("Ingrese el primer entero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer entero: "))

if num1 == num2 == num3:
    print("Los numeros son iguales")
else:
    print("Los numeros no son iguales")

# *************************************************************

calificacion = int(input("Ingresa la calificacion del alumno: "))

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")

# *************************************************************
