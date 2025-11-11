from PPlay.window import *
from PPlay.keyboard import *

def running_game_over(screen, room):
    
    screen.set_background_color([0,0,0])

    screen.draw_text("GAME OVER",300,screen.height/2,20,[255,255,255])

    if Keyboard().key_pressed("ESCAPE"):
        room[0] = "Jogo"