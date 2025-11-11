from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from PPlay.animation import *
from math import *
import random

def sign(x):
    if x == 0: return 0
    if x < 0: return -1
    if x > 0: return 1

def encontrar(lista,quero):
    for i in lista:
        if i == quero:
            return 1
    return 0

def criar_inimigo(screen,room,type=1):

    if type == 0:
        inimigo = Animation("MdASprites/ENEMIES/InimigoD.png",4,True)
        inimigo.set_total_duration(3000)

        inimigo.x = 0
        inimigo.y = 0

        inimigo.xspeed = 0
        inimigo.yspeed = 0

        inimigo.hp = 0
        inimigo.defesa = 0
        inimigo.type = 0
        inimigo.spd = 0

    if type == 1:
        inimigo = Animation("MdASprites/ENEMIES/Jones.png",4,True)
        inimigo.set_total_duration(1000)

        inimigo.x = screen.width*random.randint(1,1)
        inimigo.y = screen.height*random.randint(0,100)/100

        inimigo.hp = 4
        inimigo.defesa = random.randint(0,10)//10
        inimigo.type = 1
        inimigo.spd = 100

        inimigo.xspeed = 0
        inimigo.yspeed = 0
    
    if type == 2:

        inimigo = Animation("MdASprites/ENEMIES/Inimigo2.png",13,True)
        inimigo.set_total_duration(3000)

        inimigo.x = screen.width*random.randint(1,1)
        inimigo.y = screen.height*random.randint(0,100)/100

        inimigo.hp = 2
        inimigo.defesa = random.randint(0,10)//10
        inimigo.type = 2
        inimigo.spd = 100
        inimigo.timer = 0
        inimigo.radio = 500
        inimigo.wait = 0

        inimigo.xspeed = 0
        inimigo.yspeed = 0


    return inimigo

def Scr_inimigo(screen,room,inimigo,player,timer,projeteis,enemprojeteis):
    if timer[0] >= 3*((16-(15-player[0].kills)*(player[0].kills<15))/(player[0].kills+1)):
        timer[0] = 0
        inimigo.append(criar_inimigo(screen,room,1+((player[0].kills+1)%10==0)))

    for enem in inimigo:
        spd = enem.spd*(1-0.29*(enem.xspeed>0 and enem.yspeed>0))
        enem.xspeed = sign(player[0].x-enem.x)*spd
        enem.yspeed = sign(player[0].y-enem.y)*spd*(abs(player[0].y-enem.y)>= 5)

        if enem.type == 0:
            enem.x -= 180*screen.delta_time()
            enem.y -= 360*screen.delta_time()

        if enem.type == 1:
            enem.x += enem.spd*-3*screen.delta_time()
            enem.y += enem.yspeed*screen.delta_time()*(enem.x>player[0].x)

            if enem.x<=-100:
                inimigo.remove(enem)

        if enem.type == 2:
            if sqrt((enem.x-player[0].x)**2+(enem.y-player[0].y)**2)-enem.wait*50 >= enem.radio or (enem.x>=screen.width-100):
                enem.wait = 0
                enem.x += enem.xspeed*screen.delta_time()
                enem.y += enem.yspeed*screen.delta_time()
            else:
                enem.wait = 2
                enem.timer -= screen.delta_time()
                if enem.timer <= -4:
                    criar_enemprojeteis(enem,enemprojeteis,player[0])
                    enem.timer = 0

        Scr_enemprojeteis(enem,enemprojeteis,player[0],screen)    

            

        for p in projeteis:
            if p.collided(enem):
                if p.name == "bala":    
                    projeteis.remove(p)
                    enem.hp -= p.dano-enem.defesa
                if p.name == "sword":    
                    if encontrar(p.acertados,enem) == 0:
                        enem.hp -= p.dano-enem.defesa
                        p.acertados.append(enem)

        if enem.hp <= 0 and enem.type != 0:
                
                morto = criar_inimigo(screen,room,0)
                morto.x, morto.y = enem.x, enem.y

                inimigo.remove(enem)
                inimigo.append(morto)
                player[0].kills+=1
        
        if enem.y <= -100:
            inimigo.remove(enem)

        if enem.collided(player[0]) and enem.type != 0 and player[0].hpcor == player[0].hp:
            player[0].hp -= 1

    for enem in inimigo:

        enem.draw()
        enem.update()


def criar_enemprojeteis(enem,enemprojeteis,player):
    if enem.type == 2:
        p = Animation("MdASprites/ENEMIES/Inimigo2projétil.png",4)
        p.set_total_duration(1000)

        p.dano = 1
        p.x = enem.x+enem.width/2
        p.y = enem.y+enem.height/2

        x = player.x+player.width/2
        y = player.y+player.height/2

        dx = p.x - x
        dy = p.y - y

        dist = sqrt(dx**2+dy**2)

        dx/=-dist
        dy/=-dist

        p.xspeed = 200*dx
        p.yspeed = 200*dy

        enemprojeteis.append(p)

def Scr_enemprojeteis(enem,enemprojeteis,player,screen):

    for p in enemprojeteis:
        p.x+=p.xspeed*screen.delta_time()
        p.y+=p.yspeed*screen.delta_time()
        if p.collided(player) and player.hp == player.hpcor:
            player.hp -= p.dano
            enemprojeteis.remove(p)
            


    for p in enemprojeteis:
        p.draw()
        p.update()