longitud = int(
    input(
        "Ingrese un número impar para establecer la longitud horizontal de la base del triángulo: "
    )
)
caracter = input("Ingrese el caracter que imprimirá el triángulo: ")

cadena_triangulo = ''
numero_espacio = longitud // 2
numero_caracter = 1

# Eliminamos el renglon_parte1 debido a que el for lo inicializa en 0
for renglon_parte1 in range(numero_espacio):                     # En vez de calcular varias veces longitud//2, es mejor poner algo que ya lo ha calculado 
    numero_caracteres_renglon = numero_espacio + numero_caracter #  como numero_espacio
    
    for columna in range(numero_caracteres_renglon): # Columna ya auto inicializa en 0 debido al for
        if columna < numero_espacio:
            cadena_triangulo = cadena_triangulo + ' ' # El problema estaba aquí, debido a que se estaba reiniciando / borrando la cadena del triangulo (unicamente se iba a imprimir la última parte del código)
        else:
            cadena_triangulo = cadena_triangulo + caracter
        #Ya no es necesario el contador debido a que el for lo aumenta en 1 y 1

    numero_caracter = numero_caracter + 2
    numero_espacio = numero_espacio - 1
    cadena_triangulo = cadena_triangulo + '\n'
    #Ya no es necesario el contador debido a que el for lo aumenta en 1 y 1

# renglon_parte2 ya se auto inicializa en 0 debido al for
for renglon_parte2 in range(longitud):
    cadena_triangulo = cadena_triangulo + caracter
cadena_triangulo = cadena_triangulo  + "\n"

print(cadena_triangulo)
