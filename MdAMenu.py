from PPlay.window import *
from PPlay.sprite import *


def running_menu(room):
    screen = Window(1280,720)
    mouse = screen.get_mouse()
    menu = 0

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

    while room[0]=='Menu':
        screen.set_background_color([0, 0, 0])
        titulo.draw()
        bjoga.draw()
        bdifc.draw()
        brank.draw()
        bsair.draw()

        if mouse.is_button_pressed(1) and mouse.is_over_object(bjoga) :
            room[0] = "Jogo"

        screen.update() 