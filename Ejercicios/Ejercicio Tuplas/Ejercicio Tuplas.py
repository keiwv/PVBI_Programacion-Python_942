import numpy 
import matplotlib
import random

wins = 0
losses = 0

def lanzar_dado():
    """Lanza dos dados y regresa los valores de sus caras como una tupla."""
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    return (dado1, dado2) #empaqueta los valores de las caras de los dados en una tupla.

def mostrar_dado(dado):
    """Muestra un lanzamiento de los dos dados."""
    dado1, dado2 = dado #desempaqueta la tupla en las variables dado1 y dado2.
    print(f'Jugador lanzo {dado1} + {dado2} = {sum(dado)}')
   
valor_dado = lanzar_dado() #primer tiro
mostrar_dado(valor_dado)

#determina el estado y puntaje del juego, basandose en el primer tiro
suma_de_dados = sum(valor_dado)

if suma_de_dados in (7, 11): #ganó
    estatus_juego = 'Ganó'
elif suma_de_dados in (2, 3, 12): #perdio
    estatus_juego = 'Perdio'
else: #recuerda el punto
    estatus_juego = 'Continua'
    mi_punto = suma_de_dados
    print('El punto es:', mi_punto)

#Continua lanzando hasta que el jugar gana o pierde
while estatus_juego == 'Continua':
    valor_dado = lanzar_dado()
    mostrar_dado(valor_dado)
    suma_de_dados = sum(valor_dado)
   
    if  suma_de_dados == mi_punto: #Ganó por los puntos
        estatus_juego = 'Ganó'
    elif suma_de_dados == 7: #Perdio lanzando 7
        estatus_juego = 'Perdio'
   
#Muestra el mensaje "Ganó" o "Perdio :|"
if estatus_juego == 'Ganó':
    print('Ganó el jugador')
else:
    print('Perdio el jugador :(')