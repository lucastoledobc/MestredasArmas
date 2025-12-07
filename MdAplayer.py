from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from MdAArmas import *
from MdAConstantes import *
from math import *


def criar_player(screen):

    #player é um vetor > jogador e mãos

    player = Animation("MdASprites/Player.png",4,True)
    player.set_total_duration(1800/4)

    player.x = screen.width/2
    player.y = screen.height/2

    player.hp = 3
    player.hpcor = player.hp

    player.hp = 5
    player.kills = 0
    player.kills_type = [0,0,0,0]

    player.xspeed = 0
    player.yspeed = 0

    hand1 = Animation("MdASprites/adaga.png",1,False)
    hand1.name = "machado"
    hand1.cooldown = 0.3
    hand1.hand = 1
    hand2 = Animation("MdASprites/gun.png",1,False)
    hand2.name = "metralhadora"
    hand2.munition = 10
    hand2.cooldown = 2
    hand2.hand = 2

    return [player,hand1,hand2]


def ataque(hand,projetil,mouse):
    if hand.name == "gun":
        criar_bala(hand,projetil,mouse)

    if hand.name == "metralhadora":
        if hand.munition >= 1:
            criar_bala(hand,projetil,mouse)  

    if hand.name == "lança-chamas":
        if hand.munition >= 1:
            criar_bala(hand,projetil,mouse)  
    
    if hand.name == "arco":
        criar_bala(hand,projetil,mouse)  

    if hand.name == "sword":
        criar_espada(hand,projetil)

    if hand.name == "adaga":
        criar_espada(hand,projetil)

    if hand.name == "picareta":
        criar_espada(hand,projetil)

    if hand.name == "machado":
        criar_espada(hand,projetil)
        


def Scr_player(screen,room,player,timer,mouse,projetil):

    player[0].xspeed = xspeed_player(yspeed_player())
    player[0].yspeed = yspeed_player(xspeed_player())

    player[0].x += player[0].xspeed*screen.delta_time()
    player[0].y += player[0].yspeed*screen.delta_time()

    player[1].x = player[0].x-30+player[0].width/2-player[1].width/2
    player[1].y = player[0].y+player[0].height/2-player[1].height/2

    player[2].x = player[0].x+30+player[0].width/2-player[2].width/2
    player[2].y = player[0].y+player[0].height/2-player[2].height/2
    
    if timer[1] < 0:
        screen.draw_text(f"{abs(timer[1]):.2f}",player[1].x+player[1].width/2,player[1].y+player[1].height+20)
    if timer[2] < 0:
        screen.draw_text(f"{abs(timer[2]):.2f}",player[2].x+player[2].width/2,player[2].y+player[2].height+20)


    #extra da metralhadora

    for i in range(2):
        if player[1+i].name == "metralhadora" or player[1+i].name == "lança-chamas":
            if player[1+i].munition<10:
                player[1+i].munition += screen.delta_time()*1.33

            else:
                player[1+i].munition = 10
            if player[1+i].name == "metralhadora": screen.draw_text(f"balas: {floor(player[1+i].munition)}",player[1+i].x+10,player[1+i].y-5)
            if player[1+i].name == "lança-chamas": screen.draw_text(f"gás: {floor(player[1+i].munition)}",player[1+i].x+10,player[1+i].y-5)

    '''
    MATATABI SEI LÁ impede de sair da tela
    '''

    if player[0].y+player[0].height >= DOWN_TELA:
        player[0].y = DOWN_TELA - player[0].height

    if player[0].y <= TOP_TELA:
        player[0].y = TOP_TELA

    if player[0].x < 0:
        player[0].x = 0

    if player[0].x + player[0].width > screen.width:
        player[0].x = screen.width - player[0].width
    
    player[0].update()
   
        
    weapons(player[0],player,projetil,screen,mouse)

    #ATAQUE DAS MÃOS

    #MÃO ESQUERDA

    if mouse.is_button_pressed(1) and timer[1] >= 0:
        ataque(player[1],projetil,mouse)
        timer[1] = -player[1].cooldown

    #MÃO DIREITA

    if mouse.is_button_pressed(3) and timer[2] >= 0:
        ataque(player[2],projetil,mouse)
        timer[2] = -player[2].cooldown

    #desenhando na tela

    #screen.draw_text("HP: "+str(player[0].hp),50,50,24,[255,255,255])
    coração = GameImage("MdASprites/HP.png")
    coração.x = 50
    coração.y = 50

    for i in range(player[0].hp):
        coração.draw()
        coração.x+=coração.width*1.5

    kills = 0
    for k in player[0].kills_type:
        kills += k

    player[0].kills = kills

    screen.draw_text("KILLS: "+str(player[0].kills),50,100,24,[255,255,255])



def xspeed_player(y=0):
    esq = Keyboard().key_pressed("A")
    dir = Keyboard().key_pressed("D")

    spd = 200
    if y:
        spd *= 0.71
    return (dir-esq)*spd

def yspeed_player(x=0):
    up = Keyboard().key_pressed("W")
    down = Keyboard().key_pressed("S")

    spd = 200
    if x:
        spd *= 0.71
    return (down-up)*spd


def scr_mira(mouse):
    mira = Animation("MdASprites/mira.png",2)
    mira.set_total_duration(2000)

    mira.x = mouse.get_position()[0]
    mira.y = mouse.get_position()[1]
    return mira


def scr_mira_running(mira,mouse):
    mira.x = mouse.get_position()[0]-mira.width/2
    mira.y = mouse.get_position()[1]-mira.height/2

    mira.draw()
    mira.update()

