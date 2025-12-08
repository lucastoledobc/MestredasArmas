from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from math import *
import random 

ID_SWORD = 1
ID_ADAGA = 2
ID_PICARETA = 3
ID_MACHADO = 4
ID_GUN = 5
ID_ARCO = 6
ID_METRALHADORA = 7
ID_LANÇACHAMAS = 8

def criar_bala(hand,projetil,mouse):
    if hand.name == "gun":
        bala = GameImage("MdASprites/bala.png")
        bala.x = -bala.width*2
        bala.y = -bala.height*2
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
        bala.x = -bala.width*2
        bala.y = -bala.height*2
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
        bala.x = -bala.width*2
        bala.y = -bala.height*2
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
        bala.x = -bala.width*2
        bala.y = -bala.height*2
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
        sword.x = -sword.width*2
        sword.y = -sword.height*2

        armas.append(sword)

    if hand.name == "adaga":
        sword = GameImage("MdASprites/adaga.png")
        sword.x = -sword.width*2
        sword.y = -sword.height*2

        sword.xspeed,sword.yspeed = 0,0

        hand.cooldown = 0.5

        sword.name = hand.name
        sword.hand = hand.hand
        sword.dano = 2
        sword.acertados = []
        sword.xx = 0

        armas.append(sword)

    if hand.name == "picareta":
        sword = Animation("MdASprites/sword attack.png",9,False)
        sword.x = -sword.width*2
        sword.y = -sword.height*2
        sword.set_total_duration(600)

        sword.xspeed,sword.yspeed = 0,0

        hand.cooldown = 1.5

        sword.name = hand.name
        sword.hand = hand.hand
        sword.dano = 4
        sword.acertados = []

        armas.append(sword)

    if hand.name == "machado":
        sword = Animation("MdASprites/Machado anim.png",4,True)
        sword.x = -sword.width*2
        sword.y = -sword.height*2
        sword.set_total_duration(1000/4)

        sword.xspeed,sword.yspeed = 0,0

        hand.cooldown = 2.5

        sword.name = hand.name
        sword.hand = hand.hand
        sword.hp = 3
        sword.hpcor = sword.hp
        sword.dano = 2
        sword.acertados = []

        armas.append(sword)

def weapons(player,hand,armas,screen,mouse):
    for arma in armas:
        if arma.name == "bala":
            arma.x += arma.xspeed*screen.delta_time()
            arma.y += arma.yspeed*screen.delta_time()
            

        if arma.name == "sword":

            n = arma.hand
            arma.x = player.x+player.width
            arma.y = player.y+player.height-arma.height

            hand[n].hide()

            if arma.is_playing() == False:
                armas.remove(arma)
                hand[n].unhide()

            arma.update()

        if arma.name == "adaga":

            n = arma.hand
            arma.x = player.x+player.width+arma.xx*100
            arma.y = player.y+player.height-arma.height

            arma.xx += screen.delta_time()*3

            hand[n].hide()

            if arma.xx >= 0.6:
                armas.remove(arma)
                hand[n].unhide()
        
        if arma.name == "picareta":

            n = arma.hand
            arma.x = player.x+player.width
            arma.y = player.y-player.height+arma.height

            hand[n].hide()

            if arma.is_playing() == False:
                armas.remove(arma)
                hand[n].unhide()
                
            arma.update()

        if arma.name == "machado":

            n = arma.hand
            arma.x = player.x+player.width/2 - arma.width/2
            arma.y = player.y+player.height*2/3- arma.height/2

            hand[n].hide()

            arma.hp -= 3*screen.delta_time()

            if arma.hpcor > ceil(arma.hp):
                arma.hpcor -= 1
                arma.acertados = []
            
            if arma.hp <= 0:
                    armas.remove(arma)
                    hand[n].unhide()
            arma.update()

        if arma.name == "fogo":
            arma.dano = 6*screen.delta_time()
            arma.hp -= screen.delta_time()
            arma.x += arma.xspeed*screen.delta_time()
            arma.y += arma.yspeed*screen.delta_time()

            arma.update()

            if arma.hp <= 0:
                armas.remove(arma)

        if arma.name == "flecha":
            
            arma.update()

            if (arma.launch == 0): 

                n = arma.hand

                arma.x = hand[n].x+hand[n].width - (arma.spd)*10
                arma.y = hand[n].y+hand[n].height/2-arma.height/2
                arma.curr_frame = 0

                arma.spd = min(arma.spd+2*screen.delta_time(),3)
                if arma.spd == 3:

                    dx = arma.x - mouse.get_position()[0] + random.randint(-10,10)
                    dy = arma.y - mouse.get_position()[1] + random.randint(-10,10)

                    dist = sqrt(dx**2+dy**2)

                    arma.dx, arma.dy = -dx, -dy

                    dx/=-dist
                    dy/=-dist    

                    arma.xspeed = (arma.spd**2)*100*dx
                    arma.yspeed = (arma.spd**2)*100*dy
                    arma.dano = arma.spd*2

                    arma.launch = 1
                


            elif arma.launch == 1:
                
                arma.curr_frame = flecha(arma)

                arma.x += arma.xspeed*screen.delta_time()
                arma.y += arma.yspeed*screen.delta_time()

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

            

def flecha(arma):

    x = arma.dx
    y = arma.dy

    arctan = atan(y/(abs(x)+(x==0)))
    
    if (-pi/2) <= arctan < (-pi/4): return 2
    elif arctan < (pi/4): return 0 + 4*(x<0)
    else: return 6


