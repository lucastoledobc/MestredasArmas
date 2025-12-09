from PPlay.gameimage import *
from MdAConstantes import *
from MdAKills import *

import random

CONS = 200

def criar_bg(screen,background,fase):

    x = 0

    for i in range(3):
        floor = GameImage(f"MdASprites/Background/bg 2 - {fase}.png")

        floor.name = "floor"

        floor.timer = 0

        floor.x = x
        floor.y = screen.height - floor.height
        background.append(floor)
        x += floor.width
        floor.xx = 0
        floor.xxx = 0

    outramatrix = []

    for i in range(random.randint(3,4)):

        rock = GameImage(f"MdASprites/{fase} Pile - ORANGE -/Rock Pile "+str(random.randint(1,13))+" - ORANGE - BIG.png")

        rock.x = random.randint(screen.width-450, screen.width)
        rock.y = random.randint(TOP_TELA,DOWN_TELA-rock.height)

        rock.name = fase

        outramatrix.append(rock)

    for i in range(len(outramatrix)):
        for j in range(len(outramatrix)-1):    
            if  outramatrix[j].y+outramatrix[j].height > outramatrix[j+1].y+outramatrix[j+1].height:
                outramatrix[j], outramatrix[j+1] = outramatrix[j+1], outramatrix[j]

    for i in outramatrix:
        background.append(i)

def continuar_bg(screen,background,fase):

        rock = GameImage(f"MdASprites/{fase} Pile - ORANGE -/Rock Pile "+str(random.randint(1,13))+" - ORANGE - BIG.png")

        rock.x = screen.width + 100
        rock.y = random.randint(TOP_TELA,DOWN_TELA-rock.height)

        rock.name = fase

            
        for i in range(len(background)):
            for j in range(len(background)-1):    
                if background[j].y+background[j].height > background[j+1].y+background[j+1].height and background[j].name != "floor":
                    background[j], background[j+1] = background[j+1], background[j]

        background.append(rock)

def bg_running(background,screen,player,projetil,fase,morto):
    for b in background:
        b.x -= 180*screen.delta_time()

        if b.name != "floor" and b.x <= -b.width*2:
            continuar_bg(screen,background,fase)
            background.remove(b)


        if b.name != "floor" and player.hp == player.hpcor:
            if abs(b.y+b.height-(player.y+player.height)) <= 20 and b.collided(player):
                player.hp -= 1

        for p in projetil:
            if p.name == "picareta" and abs(p.height+p.y-(b.y+b.height))<=30 and (b.name == "rock" or b.name == "magma"):
                if p.collided(b):
                    criar_pedaços_chão(b,morto)
                    background.remove(b)
                    player.ground+=1

            if p.name == "machado" and abs(p.height/2+p.y-(b.y+b.height))<=p.height/2 and (b.name == "forest"):
                if p.collided(b):
                    criar_pedaços_chão(b,morto)
                    background.remove(b)
                    player.ground+=1

            if p.name == "explosion" and b.name != "floor":
                if p.collided(b):
                    criar_pedaços_chão(b,morto)
                    background.remove(b)
                    player.ground+=1



    background[0].timer += screen.delta_time()

    if background[0].timer >= random.randint(6,8):
        continuar_bg(screen,background,fase)
        background[0].timer = 0
    


def bg_draw(screen,background,typedraw,player,fase):

    sol = Animation(f"MdASprites/Background/sol {fase}.png",1,False)
    sol.draw()

    p = Animation(f"MdASprites/Background/fundão {fase} 2.png",1,False)
    p.x = background[0].xxx

    background[0].xxx -= SPD_BACKGROUND*0.4*screen.delta_time()

    if background[0].xxx < -p.width: background[0].xxx = 0

    while p.x < screen.width:
        p.draw()
        p.x+=p.width

    p = Animation(f"MdASprites/Background/fundão {fase} 1.png",1,False)
    p.x = background[0].xx

    background[0].xx -= SPD_BACKGROUND*0.6*screen.delta_time()

    if background[0].xx < -p.width: background[0].xx = 0

    while p.x < screen.width:
        p.draw()
        p.x+=p.width

    for b in background:

        if b.name == "floor" and typedraw == "floor":
            b.draw()
            if b.x<=-b.width:
                b.x+= 3*b.width-2


def pontos(player, fase, room):
    pontos_temp = pontuação(player[0], fase)+room[2]
    
    pontos = Sprite("MdASprites/Background/pontos/pontos.png")
    pontos.set_position(10, 10)

    score2=[]
    texto=str(int(pontos_temp))
    for i in range(len(texto)):
        x = Sprite("MdASprites/Background/pontos/"+texto[i]+".png")
        x.set_position(pontos.width+20+i*20, 10)
        score2.append(x)
        
    pontos.draw()
    for i in range(len(score2)):
        score2[i].draw()

    if player[0].timer_da_fase <= 0:
        room[2]+=pontos_temp

def tempo(player):
    try:
        score2=[]
        texto=str(int(player.timer_da_fase))
        for i in range(len(texto)):
            x = Sprite("MdASprites/Background/pontos/"+texto[i]+".png")
            x.set_position(1100+i*20, 10)
            score2.append(x)
            
        for i in range(len(score2)):
            score2[i].draw()
    except:
        return