import pygame
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *

from MdAJogo import *
from MdAgameover import *
from MdAMenu import *

def final():

    screen.update()

room = ["Menu", 0]

screen = Window(1280,720)
screen.set_title("Mestre das Armas")
entrar = True

running = [True, False]

while running[0]:
    if room[0] == "Menu":
        running_menu(room)
        
    if room[0] == "Jogo":
        if entrar:
            mouse = screen.get_mouse()
            inimigo = []
            projetil = []
            timer = [0,0,0]
            player = criar_player(screen)
            entrar = False
            background = []
            enemprojeteis = []
            mira = [scr_mira(mouse)]

        if running[1] == False:
            running[1] = True
        else:
            running_jogo(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira)

        final()

        if room[0] != "Jogo":
            entrar = True
    
    if room[0] == "GAME OVER":
        
        running_game_over(screen, room)
        final()