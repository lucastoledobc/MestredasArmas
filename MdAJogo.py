from MdAplayer import *
from MdAInimigo import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

from MdABackground import *
from MdAMenu import *


def running_jogo(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira):

    if background == []:
        criar_bg(screen,background)

    for t in range(len(timer)):
        timer[t] += screen.delta_time()

    screen.set_background_color([74, 138, 237])

    #background = Sprite("MdASprites/BG.png")

    #background.draw()

    bg_running(background,screen,player[0],projetil)

    bg_draw(screen,background,"floor",player[0])
    bg_draw(screen,background,"acima",player[0])




    Scr_player(screen,room,player,timer,mouse,projetil)

    bg_draw(screen,background,"abaixo",player[0])

    Scr_inimigo(screen,room,inimigo,player,timer,projetil,enemprojeteis)

    scr_mira_running(mira[0],mouse)


    if player[0].hp <= 0:
        room[0] = "GAME OVER"
        frank(player[0].kills*100)