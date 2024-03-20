aprove = 0
reprobado = 0

for student in range(1,10):
    student = int(input("Ingrese el resultado (1 = aprobado, 0 = reporbado):"))
    if student == 1:
        aprove += 1
    else:
        reprobado += 1

print("reporbados: ", reprobado)

print("Aprobados: ", aprove)

if aprove >= 8:
    print("Bonificación para el instructor")