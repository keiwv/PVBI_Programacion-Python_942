import pgzrun
import os
from pgzero.actor import Actor
from pgzero.keyboard import keys


WIDTH = 1920
HEIGHT = 1080

os.system("clear") 
carro = Actor('corolla.png')
carroGTR = Actor('gtr.png')  
meta = Actor('meta.png')  

carro.x = 50
carro.y = HEIGHT // 3
meta.x = WIDTH - 100
meta.y = HEIGHT // 2
carroGTR.x = 50
carroGTR.y = 2 * HEIGHT // 3

game_over = False
ganador = None

def draw():
    screen.fill((0, 0, 0))
    carro.draw()
    carroGTR.draw()
    meta.draw()
    if game_over:
        screen.draw.text(f"¡Ganó el {ganador}!", (WIDTH // 2 - 150, HEIGHT // 2), fontsize=50, color="white")

def on_key_down(key):
    global game_over, ganador
    if not game_over:
        if key == keys.UP:
            carro.x += 35
            if carro.x >= meta.x:
                game_over = True
                ganador = "carro negro"
                print("¡Ganó el poderoso corolla!")
                quit()
        elif key == keys.W:
            carroGTR.x += 35
            if carroGTR.x >= meta.x:
                game_over = True
                ganador = "carro rojo"
                print("¡Ganó el GTR zzzz!")
                quit()

pgzrun.go()
