import pygame
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *

from MdAJogo import *
from MdAgameover import *
from MdAMenu import *
from MdASounds import *


def final():

    screen.update()


# room [Menu/Jogo/Game Over, Seleção de armas, Pontuação, Musica]
room = ["Menu", False, 0, 0]

screen = Window(1280,720)
screen.set_title("Mestre das Armas")
entrar = True

running = [True]

musica = [Sound("MdASprites/Sounds/menu-8_bit.mp3")]


while running[0]:
    if room[0] == "Menu":
        if room[3] != -1:
            room[3]=0
            fmusica(room, musica)

        running_menu(screen, room)


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
            morto = []
            mira = [scr_mira(mouse)]
            fase = ['rock']

        if room[1] == False:
            if room[3]!=-1:
                room[3]=1
                fmusica(room, musica)
                
            running_arma(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira, fase)
        else:
            if room[3]!=-1:
                fmusica(room, musica)

            running_jogo(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira, morto, fase[0])
            if player[0].timer_da_fase <= 0:
                entrar = True
                room[1] = False
                room[3] = 1

        final()

        if room[0] != "Jogo":
            entrar = True
    
    if room[0] == "GAME OVER":
        
        running_game_over(screen, room)
        final()