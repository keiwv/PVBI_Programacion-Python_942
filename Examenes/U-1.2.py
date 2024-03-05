num1 = int(input("Ingresa el primer valor entero: "))
num2 = int(input("Ingresa el segundo valor entero: "))
num3 = int(input("Ingrese el tercer valor entero: "))

isEqual = True

if num1 == num2 == num3:
    isEqual = False
    print("Los valores", num1, num2, num3, "son iguales")
    print("Todos los numeros son iguales, por lo  tanto no es necesario mostrar su ordenamiento")

if isEqual:
    print("Los valores", num1, num2, num3, "no son iguales")
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)

    mid = num1 + num2 + num3 - maximum - minimum

    print("El orden de los números de forma descendente son: ", maximum, mid, minimum)
