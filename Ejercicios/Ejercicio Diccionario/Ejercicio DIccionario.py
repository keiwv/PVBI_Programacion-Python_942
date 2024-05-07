import os

class Student:
    def __init__(self, nombre, numero_identificacion):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion

def pause():
    input("Presiona enter para continuar...")

def menu():
    op = -1
    while op > 5 or op < 0:
        os.system("clear")
        print("Menu:")
        print("1. Agregar un nuevo estudiante")
        print("2. Buscar estudiante por numero de identificacion.")
        print("3. Mostrar todos los estudiantes registrados")
        print("4. Eliminar un estudiante")
        print("5. Salir")
        op = int(input("Selecciona una opcion: "))
    return op

def addStudent(DicStdnt):
    nombre = input("Ingrese el nombre del estudiante: ")
    numero_identificacion = input("Ingrese el numero de identificacion: ")
    estudiante = Student(nombre, numero_identificacion)
    DicStdnt[numero_identificacion] = estudiante
    print("Estudiante agregado exitosamente.")

def searchStudent(DicStdnt):
    numero_identificacion = input("Ingrese el numero de identificacion del estudiante a buscar: ")
    if numero_identificacion in DicStdnt:
        print("Nombre del estudiante:", DicStdnt[numero_identificacion].nombre)
    else:
        print("Estudiante no encontrado.")

def showAllStudents(DicStdnt):
    print("Estudiantes registrados:")
    for identificacion, estudiante in DicStdnt.items():
        print(f"Número de Identificación: {identificacion}, Nombre: {estudiante.nombre}")

def removeStudent(DicStdnt):
    numero_identificacion = input("Ingrese el numero de identificacion del estudiante a eliminar: ")
    if numero_identificacion in DicStdnt:
        del DicStdnt[numero_identificacion]
        print("Estudiante eliminado exitosamente.")
    else:
        print("Estudiante no encontrado.")

DicStdnt = {}

op = -1
while op != 5:
    op = menu()

    if op == 1:
        addStudent(DicStdnt)
    elif op == 2:
        searchStudent(DicStdnt)
    elif op == 3:
        showAllStudents(DicStdnt)
    elif op == 4:
        removeStudent(DicStdnt)
    pause()

