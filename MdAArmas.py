from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from math import *

def criar_espada(hand,armas):
    if hand.name == "sword":
        sword = Animation("MdASprites/sword attack.png",9,False)
        sword.set_total_duration(400)

        sword.xspeed,sword.yspeed = 0,0

        sword.name = hand.name
        sword.dano = 5
        sword.acertados = []

        armas.append(sword)

def weapons(player,armas,screen):
    for arma in armas:
        if arma.name == "bala":
            arma.x += arma.xspeed*screen.delta_time()
            arma.y += arma.yspeed*screen.delta_time()
            arma.draw()
        if arma.name == "sword":
            arma.x = player.x+player.width
            arma.y = player.y-player.height/2

            if arma.is_playing() == False:
                armas.remove(arma)
            arma.draw()
            arma.update()


            