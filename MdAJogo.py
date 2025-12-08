from MdAplayer import *
from MdAInimigo import *
from MdADraw import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from MdAKills import *

from MdABackground import *

def running_jogo(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira, morto, fase):


    if background == []:
        criar_bg(screen,background,fase)


    for t in range(len(timer)):
        timer[t] += screen.delta_time()

    screen.set_background_color([74, 138, 237])

    #background = Sprite("MdASprites/BG.png")

    #background.draw()

    bg_running(background,screen,player[0],projetil,fase,morto)

    bg_draw(screen,background,"floor",player[0])
    #bg_draw(screen,background,"acima",player[0])




    Scr_player(screen,room,player,timer,mouse,projetil)

    #bg_draw(screen,background,"abaixo",player[0])

    Scr_inimigo(screen,room,inimigo,player,timer,projetil,enemprojeteis,fase,morto)

    draw_cena(player,background,inimigo,projetil,enemprojeteis,screen)

    pedaços(morto,screen)

    scr_mira_running(mira[0],mouse)


    if player[0].hp <= 0:
        room[0] = "GAME OVER"
        room[2] += player[0].kills*100