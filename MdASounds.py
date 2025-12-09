from PPlay.sound import *

def fmusica(room, musica):
    musica[0].stop()
    if room[3]==0:
        musica[0] = Sound("MdASprites/Sounds/menu-8_bit.mp3")
        musica[0].loop = True
    elif room[3] == 1:
        musica[0] = Sound("MdASprites/Sounds/select-bit_beats_1.mp3")
        musica[0].loop = True
    elif room[3] == 2:
        musica[0] = Sound("MdASprites/Sounds/rock-my_8_bit_hero.mp3")
        musica[0].loop = True
    elif room[3] == 3:
        musica[0] = Sound("MdASprites/Sounds/forest-8_bit_arcade.mp3")
        musica[0].loop = True
    elif room[3] == 4:
        musica[0] = Sound("MdASprites/Sounds/magma-8_bit_game.mp3")
        musica[0].loop = True
    musica[0].play()
    room[3] = -1