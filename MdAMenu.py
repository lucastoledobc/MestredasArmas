from PPlay.mouse import *
from PPlay.window import *
from PPlay.sprite import *


def running_menu(screen,room,mouse,titulo,bjoga,bdifc,brank,bsair):
    screen.set_background_color([0, 0, 0])
    titulo.draw()
    bjoga.draw()
    bdifc.draw()
    brank.draw()
    bsair.draw()

    if mouse.is_button_pressed(1) and mouse.is_over_object(bjoga) :
        room[0] = "Jogo"