# feito por Felipe Mehiel e Lucas Toledo


# Importações
import pygame
from PPlay import *


# criação da janela
screen = window.Window(1280, 720)
screen.set_title("Mestre das Armas")

# teclado e mouse
keyb = screen.get_keyboard()
mous = screen.get_mouse()


# fundo e botões
fundo = sprite.Sprite("anexos/img/fundo.png")
fundo.set_position(0, 0)

bjoga = sprite.Sprite("anexos/img/bjoga.png")
bjoga.set_position(int(screen.width/2)-bjoga.width/2, 300)
bdifc = sprite.Sprite("anexos/img/bdifc.png")
bdifc.set_position(int(screen.width/2)-bdifc.width/2, 350)
brank = sprite.Sprite("anexos/img/brank.png")
brank.set_position(int(screen.width/2)-brank.width/2, 400)
bsair = sprite.Sprite("anexos/img/bsair.png")
bsair.set_position(int(screen.width/2)-bsair.width/2, 450)


# tela do jogo (partida)
def fjogo():

    # tela de selação de armas
    loop_menu = True
    while loop_menu:
        screen.set_background_color([0,0,0])
        fundo.draw()

        screen.update()
        # condição de saída da partida
        if keyb.key_pressed('esc'):
            loop_jogo = False



    # tela de luta
    loop_jogo = True
    while loop_jogo:
        # screen e fps
        screen.set_background_color([0,0,0])
        fundo.draw()

        screen.update()
        # condição de saída da partida
        if keyb.key_pressed('esc'):
            loop_jogo = False





# tela de dificuldade
def fdifc():
        
        screen.update()
        # condição apra voltar ao menu principal
        if keyb.key_pressed('esc'):
            difc_loop = False





# tela do ranking
def frank():
    rank_loop = True
    while rank_loop:
        screen.set_background_color([0,0,0])


        screen.update()
        # condição apra voltar ao menu principal
        if keyb.key_pressed('esc'):
            rank_loop = False





loop_menu = True
while loop_menu:
    screen.set_background_color([0,0,0])
    fundo.draw()

    bjoga.draw()
    bdifc.draw()
    brank.draw()
    bsair.draw()
    
    if mous.is_over_object(bjoga) and mous.is_button_pressed(1):
        fjogo()

    if mous.is_over_object(bdifc) and mous.is_button_pressed(1):
        fdifc()

    if mous.is_over_object(brank) and mous.is_button_pressed(1):
        frank()

    if mous.is_over_object(bsair) and mous.is_button_pressed(1):
        screen.close()


    screen.update()