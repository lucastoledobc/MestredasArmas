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
    if hand.name == "lança-chamas":
        bala = Animation("MdASprites/Fosgo.png",4)
        bala.set_total_duration(750)
        bala.name = "fogo"
        bala.dano = 0.45

        bala.acertados = []

        bala.x = hand.x+hand.width 
        bala.y = hand.y+hand.height/2-bala.height/2
        hand.munition = floor(hand.munition-1)
        hand.cooldown = 0.1
        bala.hp = 1.5
            

        dx = bala.x - mouse.get_position()[0] + random.randint(-10,10)
        dy = bala.y - mouse.get_position()[1] + random.randint(-10,10)

        dist = sqrt(dx**2+dy**2)

        dx/=-dist
        dy/=-dist

        bala.xspeed = 300*dx
        bala.yspeed = 300*dy

        projetil.append(bala)

    if hand.name == "arco":
        bala = Animation("MdASprites/flechas.png",8)
        bala.set_total_duration(400)
        bala.name = "flecha"
        bala.dano = 0.25

        bala.ant = 1

        bala.hp = 1
        bala.launch = 0
        bala.hand = hand.hand
        bala.spd = 0
        hand.cooldown = 3

        bala.xspeed = 0
        bala.yspeed = 0

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

def weapons(player,hand,armas,screen,mouse):
    for arma in armas:
        if arma.name == "bala":
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

        if arma.name == "fogo":
            arma.dano = 6*screen.delta_time()
            arma.hp -= screen.delta_time()
            arma.x += arma.xspeed*screen.delta_time()
            arma.y += arma.yspeed*screen.delta_time()

            arma.draw()
            arma.update()

            if arma.hp <= 0:
                armas.remove(arma)

        if arma.name == "flecha":

            arma.draw()
            arma.update()

            if (arma.launch == 0): 

                n = arma.hand

                arma.x = hand[n].x+hand[n].width - (arma.spd)*10
                arma.y = hand[n].y+hand[n].height/2-arma.height/2
                arma.curr_frame = 0

                arma.spd = min(arma.spd+2*screen.delta_time(),3)
                if arma.spd == 3:
                    print(arma.name)

                    dx = arma.x - mouse.get_position()[0] + random.randint(-10,10)
                    dy = arma.y - mouse.get_position()[1] + random.randint(-10,10)

                    dist = sqrt(dx**2+dy**2)

                    dx/=-dist
                    dy/=-dist    

                    arma.xspeed = (arma.spd**2)*100*dx
                    arma.yspeed = (arma.spd**2)*100*dy
                    arma.dano = arma.spd**2

                    arma.launch = 1
                


            elif arma.launch == 1:
                
                arma.curr_frame = 0

                arma.x += arma.xspeed*screen.delta_time()
                arma.y += arma.yspeed*screen.delta_time()

                arma.draw()
                arma.update()

                if arma.hp <= 0:
                    arma.set_total_duration(65)
                    arma.launch = 2
                    arma.yspeed = -250
                    arma.xspeed = -100

            else:

                arma.x += arma.xspeed*screen.delta_time()
                arma.y += arma.yspeed*screen.delta_time()
                arma.yspeed+=8*60*screen.delta_time()
                
                if arma.y >= screen.height+50:
                    armas.remove(arma)

            


