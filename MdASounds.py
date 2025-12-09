from PPlay.sound import *

def fmusica(room, musica):
    musica[0].stop()
    if room[3]==0:
        musica[0] = Sound("MdASprites/Sounds/musica0.mp3")
        musica[0].loop = True
        room[3]=1
    else:
        musica[0] = Sound("MdASprites/Sounds/musica1.mp3")
        musica[0].loop = True
        room[3]=0
    musica[0].play()
    print(room[3])