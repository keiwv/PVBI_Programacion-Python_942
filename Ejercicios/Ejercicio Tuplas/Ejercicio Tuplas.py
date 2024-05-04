import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import statistics as st

def lanzar_dado():
    """Lanza dos dados y regresa los valores de sus caras como una tupla."""
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    return (dado1, dado2)  # Empaqueta los valores de las caras de los dados en una tupla.

def mostrar_dado(dado):
    """Muestra un lanzamiento de los dos dados."""
    dado1, dado2 = dado  # Desempaqueta la tupla en las variables dado1 y dado2.
    print(f'Jugador lanzó {dado1} + {dado2} = {sum(dado)}')

# Listas para contar victorias y derrotas en cada juego
ganados = [0] * 14
perdidos = [0] * 14

# Diccionario para registrar la duración de los juegos ganados
duracion_juegos = {}

# Verificar si tiene argumentos al momento de ejceutar el programa
if len(sys.argv) < 2:
    lanzar = int(input("Ingrese el número de juegos a simular: "))
else:
    lanzar = int(sys.argv[1])


for _ in range(lanzar):
    juegoNumero = 1
    
    valor_dado = lanzar_dado()  # Primer tiro
    # Determina el estado y puntaje del juego, basándose en el primer tiro
    suma_de_dados = sum(valor_dado)

    if suma_de_dados in (7, 11):  # Ganó
        estatus_juego = 'Ganó'
    elif suma_de_dados in (2, 3, 12):  # Perdió
        estatus_juego = 'Perdió'
    else:  # Recuerda el punto
        estatus_juego = 'Continua'
        mi_punto = suma_de_dados

    # Continúa lanzando hasta que el jugador gana o pierde
    while estatus_juego == 'Continua':
        valor_dado = lanzar_dado()
        suma_de_dados = sum(valor_dado)
    
        if suma_de_dados == mi_punto:  # Ganó por los puntos
            estatus_juego = 'Ganó'
            duracion = juegoNumero
            if duracion in duracion_juegos:
                duracion_juegos[duracion] += 1
            else:
                duracion_juegos[duracion] = 1
            break
        elif suma_de_dados == 7:  # Perdió lanzando 7
            estatus_juego = 'Perdió'
            break

        juegoNumero += 1

    if estatus_juego == 'Ganó':
        if juegoNumero >= 13:
            ganados[13] += 1
        else:
            ganados[juegoNumero] += 1
    elif estatus_juego == 'Perdió':
        if juegoNumero >= 13:
            perdidos[13] += 1
        else:
            perdidos[juegoNumero] += 1
   

# Probabilidad de ganar general
total_victorias = sum(ganados)
prob_ganar = total_victorias / lanzar

# Obtener probabilidades de ganar en una lista
probabilidades_ganar = [ganados[v] / total_victorias for v in range(len(ganados))]
probabilidades_ganar_redondeadas = [round(prob, 4) for prob in probabilidades_ganar]

# MEDIA
total_juegos = sum(duracion_juegos.values())
media = st.mean(duracion_juegos)

# MEDIANA
sorted_data = sorted(duracion_juegos)
mediana = st.median(sorted_data)

# MODA
moda = st.mode(duracion_juegos)

# Mostrar en la terminal los datos.
print(f'Victorias: {ganados}')
print(f'Derrotas: {perdidos}')
print(f'La probabilidad de ganar es: {prob_ganar}')
print(f'La media de duración de los juegos: {media:.4f}')
print(f'La mediana de duración de los juegos: {mediana:.4f}')
print(f'Moda de duración de los juegos: {moda} veces')
print(f'Las probabilidades de ganar es: {probabilidades_ganar_redondeadas}')


# Mostrar gráfica.
y = np.arange(14)
x1 = ganados
x2 = perdidos

plt.barh(y, x1, color='b', label='Victorias')
plt.barh(y, x2, color='r', label='Derrotas', left=x1)
plt.ylabel('Jugadas')
plt.xlabel('Cantidad de veces')
plt.title('Victorias y Derrotas')
plt.legend()
plt.show()
