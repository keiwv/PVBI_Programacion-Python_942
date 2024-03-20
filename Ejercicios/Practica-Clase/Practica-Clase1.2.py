total = 0
califCounter = 0
num = 0

num = int(input("Ingrese la calificacion: "))

while num != -1:
    total += num
    califCounter += 1
    num = int(input("Ingresse la calificación: "))

if califCounter != 0:
    print("La media es: ", (total / califCounter))
else:
    print("No se ingresaron calificaciones")