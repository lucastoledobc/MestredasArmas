from PPlay.mouse import *
from PPlay.window import *

def running_menu(screen,room,mouse):
    screen.set_background_color([0, 0, 0])

    if mouse.is_button_pressed(1):
        room[0] = "Jogo"