# Utilizamos un bucle for para ingresar dos números enteros
for i in range(2):
    num = int(input(f"Ingrese el número entero {i + 1}: "))

    if num % 2 == 0:
        print(f"{num} es un número par.")
    else:
        print(f"{num} es un número impar.")

for i in range(99, 0, -11):
    print(i)