from PPlay.gameimage import *

import random

CONS = 200

def criar_bg(screen,background):

    x = 0

    for i in range(3):
        floor = GameImage("MdASprites/Background/bg 2.png")

        floor.name = "floor"

        floor.timer = 0

        floor.x = x
        floor.y = screen.height - floor.height
        background.append(floor)
        x += floor.width

    outramatrix = []

    for i in range(random.randint(4,6)):

        rock = GameImage("MdASprites/Rock Pile - ORANGE -/Rock Pile "+str(random.randint(1,13))+" - ORANGE - BIG.png")

        rock.x = random.randint(screen.width-450, screen.width)
        rock.y = random.randint(CONS, screen.height-100)

        rock.name = "rock"

        outramatrix.append(rock)

    for i in range(len(outramatrix)):
        for j in range(len(outramatrix)-1):    
            if outramatrix[j].y < outramatrix[j+1].y:
                outramatrix[j], outramatrix[j+1] = outramatrix[j+1], outramatrix[j]

    for i in outramatrix:
        background.append(i)

def continuar_bg(screen,background):

        rock = GameImage("MdASprites/Rock Pile - ORANGE -/Rock Pile "+str(random.randint(1,13))+" - ORANGE - BIG.png")

        rock.x = screen.width + 100
        rock.y = random.randint(CONS, screen.height-100)

        rock.name = "rock"

            
        for i in range(len(background)):
            for j in range(len(background)-1):    
                if background[j].y < background[j+1].y and background[j].name != "floor":
                    background[j], background[j+1] = background[j+1], background[j]

        background.append(rock)

def bg_running(background,screen,player,projetil):
    for b in background:
        b.x -= 180*screen.delta_time()

        if b.name != "floor" and player.hp == player.hpcor:
            if abs(b.y+b.height-(player.y+player.height)) <= 14 and b.collided(player):
                player.hp -= 1

        for p in projetil:
            if p.name == "picareta" and abs(p.height+p.y-(b.y+b.height))<=30 and b.name == "rock":
                if p.collided(b):
                    background.remove(b)

    background[0].timer += screen.delta_time()

    if background[0].timer >= random.randint(6,8):
        continuar_bg(screen,background)
        background[0].timer = 0
    


def bg_draw(screen,background,typedraw,player):

    for b in background:

        if b.name == "floor" and typedraw == "floor":
            b.draw()
            if b.x<=-b.width:
                b.x+= 3*b.width-1

