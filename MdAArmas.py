from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from math import *
import random 

def criar_bala(hand,projetil,mouse):
    if hand.name == "gun":
        bala = GameImage("MdASprites/bala.png")
        bala.name = "bala"
        bala.dano = 2

        bala.x = hand.x+hand.width
        bala.y = hand.y+hand.height/2

        dx = bala.x - mouse.get_position()[0]
        dy = bala.y - mouse.get_position()[1]

        dist = sqrt(dx**2+dy**2)

        dx/=-dist
        dy/=-dist

        bala.xspeed = 600*dx
        bala.yspeed = 600*dy

        projetil.append(bala)
    if hand.name == "metralhadora":
        bala = GameImage("MdASprites/balam.png")
        bala.name = "bala"
        bala.dano = 0.75

        bala.x = hand.x+hand.width 
        bala.y = hand.y+hand.height/2
        hand.munition = floor(hand.munition-1)
        hand.cooldown = 0.1
            

        dx = bala.x - mouse.get_position()[0] + random.randint(-10,10)
        dy = bala.y - mouse.get_position()[1] + random.randint(-10,10)

        dist = sqrt(dx**2+dy**2)

        dx/=-dist
        dy/=-dist

        bala.xspeed = 1000*dx
        bala.yspeed = 1000*dy

        projetil.append(bala)


def criar_espada(hand,armas):
    if hand.name == "sword":
        sword = Animation("MdASprites/sword attack.png",9,False)
        sword.set_total_duration(400)

        sword.xspeed,sword.yspeed = 0,0

        hand.cooldown = 1

        sword.name = hand.name
        sword.hand = hand.hand
        sword.dano = 5
        sword.acertados = []

        armas.append(sword)

    if hand.name == "picareta":
        sword = Animation("MdASprites/sword attack.png",9,False)
        sword.set_total_duration(600)

        sword.xspeed,sword.yspeed = 0,0

        hand.cooldown = 1.5

        sword.name = hand.name
        sword.hand = hand.hand
        sword.dano = 4
        sword.acertados = []

        armas.append(sword)

def weapons(player,hand,armas,screen):
    for arma in armas:
        if arma.name == "bala":
            arma.x += arma.xspeed*screen.delta_time()
            arma.y += arma.yspeed*screen.delta_time()
            arma.draw()
        if arma.name == "balam": #metralhadora
            arma.x += arma.xspeed*screen.delta_time()
            arma.y += arma.yspeed*screen.delta_time()
            arma.draw()
        if arma.name == "sword":

            n = arma.hand
            arma.x = player.x+player.width
            arma.y = player.y-player.height+arma.height

            hand[n].hide()

            if arma.is_playing() == False:
                armas.remove(arma)
                hand[n].unhide()
            arma.draw()
            arma.update()
        
        if arma.name == "picareta":

            n = arma.hand
            arma.x = player.x+player.width
            arma.y = player.y-player.height+arma.height

            hand[n].hide()

            if arma.is_playing() == False:
                armas.remove(arma)
                hand[n].unhide()
            arma.draw()
            arma.update()


            