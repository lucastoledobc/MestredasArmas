import pygame
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *

from MdAJogo import *
from MdAgameover import *
from MdAMenu import *

def final():

    screen.update()

room = ["Menu"]

screen = Window(1280,720)
screen.set_title("Mestre das Armas")
entrar = True

running = [True]

while running[0]:
    if room[0] == "Menu":
        if entrar:
            # título e botões
            titulo = Sprite("MdASprites/Menu/titulo.png")
            titulo.set_position(int(screen.width/2)-titulo.width/2, 30)

            bjoga = Sprite("MdASprites/Menu/bjoga.png")
            bjoga.set_position(int(screen.width/2)-bjoga.width/2, 300)
            bdifc = Sprite("MdASprites/Menu/bdifc.png")
            bdifc.set_position(int(screen.width/2)-bdifc.width/2, 350)
            brank = Sprite("MdASprites/Menu/brank.png")
            brank.set_position(int(screen.width/2)-brank.width/2, 400)
            bsair = Sprite("MdASprites/Menu/bsair.png")
            bsair.set_position(int(screen.width/2)-bsair.width/2, 450)

            # mouse e teclado
            mouse = screen.get_mouse()
            
            entrar = False

        running_menu(screen,room,mouse,titulo,bjoga,bdifc,brank,bsair)

        if room[0] != "Menu":
            entrar = True

        final()
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


        running_jogo(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira)

        final()

        if room[0] != "Jogo":
            entrar = True
    
    if room[0] == "GAME OVER":

        running_game_over(screen, room)
        final()