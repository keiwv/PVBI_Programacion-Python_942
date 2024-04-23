promedio = 0
calificacion = 0
num_estudiante = 0
num_aprobados = 0
num_reprobados = 0

while calificacion != -1:
    calificacion = int(input("Ingrese la calificacion, -1 para terminar: "))
    if (calificacion > 100) or (calificacion < -1):
        print("La calificacion esta fuera del rango establecido, por favor ingrese una calificacion entre 0 y 100")
    elif (calificacion == -1):
        if (num_estudiante == 0):
            print("No se ingresaron calificaciones")
        else:
            print("")
            print(f'Promedio de las calificaciones capturas del segundo examen parcial: {int(promedio / num_estudiante)}')
            print(f'Cantidad de alumnos aprobados en el segundo examen parcial: {num_aprobados}')
            print(f'Cantidad de alumnos reprobados en el segundo examen parcial: {num_reprobados}')
        
            if promedio >= 90:
                print("El docente obtuvo un buen desempeño en el segundo parcial")
            else:
                print("El docente no obtuvo un buen desempeño en el segundo parcial")
    else:
        promedio += calificacion
        num_estudiante += 1
        
        if calificacion >= 60:
            num_aprobados += 1
        else:
            num_reprobados += 1


