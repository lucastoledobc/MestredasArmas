from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from PPlay.animation import *
from MdAConstantes import *
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

def choose(lista):
    r = random.randint(0,len(lista)-1)

    return lista[r]

def criar_inimigo(screen,room,type=1,scene = 'forest'):

    if type == 0:
        inimigo = Animation("MdASprites/ENEMIES/InimigoD.png",4,True)
        inimigo.set_total_duration(3000)

        inimigo.x = 0
        inimigo.y = 0

        inimigo.xspeed = 0
        inimigo.yspeed = 0

        inimigo.especie = ""
        inimigo.hp = 0
        inimigo.defesa = 0
        inimigo.type = 0
        inimigo.spd = 0

    if scene == 'rock':
        if type == 1:
            inimigo = Animation("MdASprites/ENEMIES/Rock/Inimigo1.png",4,True)
            inimigo.set_total_duration(1000)

            inimigo.dano = 1
            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)
            inimigo.especie = "rock"
            inimigo.hp = 4
            inimigo.defesa = random.randint(0,10)//10
            inimigo.type = 1
            inimigo.spd = 100

            inimigo.xspeed = 0
            inimigo.yspeed = 0
        
        if type == 2:

            inimigo = Animation("MdASprites/ENEMIES/Rock/Inimigo2.png",13,True)
            inimigo.set_total_duration(3000)

            inimigo.dano = 1
            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)
            inimigo.especie = "rock"
            inimigo.hp = 2
            inimigo.defesa = random.randint(0,10)//10
            inimigo.type = 2
            inimigo.spd = 100
            inimigo.timer = 0
            inimigo.radio = 500
            inimigo.wait = 0

            inimigo.xspeed = 0
            inimigo.yspeed = 0

        if type == 3:

            inimigo = Animation("MdASprites/ENEMIES/Rock/Inimigo3.png",12,True)
            inimigo.set_total_duration(1000)

            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)

            inimigo.dano = 1
            inimigo.especie = "rock"
            inimigo.hp = 4
            inimigo.defesa = 1
            inimigo.type = 3
            inimigo.spd = SPD_BACKGROUND
            inimigo.rocknroll = 0

            inimigo.xspeed = 0
            inimigo.yspeed = 0

        if type == 4:

            inimigo = Animation("MdASprites/ENEMIES/Rock/Inimigo4.png",1,False)
            inimigo.set_total_duration(1000)

            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)

            inimigo.dano = 2
            inimigo.especie = "rock"
            inimigo.hp = 10
            inimigo.defesa = 3
            inimigo.type = type
            inimigo.spd = 24
            inimigo.shake = 0
            inimigo.yy = inimigo.y
            inimigo.xx = inimigo.x

            inimigo.xspeed = 0
            inimigo.yspeed = 0

    
    if scene == 'forest':
        if type == 1:
            inimigo = Animation("MdASprites/ENEMIES/Forest/Inimigo1.png",2,True)
            inimigo.stop()

            inimigo.dano = 1
            inimigo.timer = 0
            inimigo.cooldown = random.randint(1,3)
            inimigo.x = screen.width
            inimigo.y = TOP_TELA+random.randint(1,3)*(140)-inimigo.height
            inimigo.especie = "forest"
            inimigo.hp = 5
            inimigo.defesa = 0
            inimigo.type = type
            inimigo.spd = 100
            inimigo.yy = inimigo.y
            inimigo.z = inimigo.y

            inimigo.xspeed = 0
            inimigo.yspeed = 0
            
        if type == 2:
            inimigo = Animation("MdASprites/ENEMIES/Forest/Inimigo2.png",6,False)
            inimigo.set_total_duration(250)
            inimigo.stop()

            inimigo.dano = 0
            inimigo.timer = 0
            inimigo.cooldown = random.randint(3,5)
            inimigo.x = screen.width
            inimigo.y = TOP_TELA+random.randint(1,5)*(440/5)-inimigo.height
            inimigo.especie = "forest"
            inimigo.hp = 3
            inimigo.defesa = random.randint(0,10)//10
            inimigo.type = type
            inimigo.spd = 100
            inimigo.xx = inimigo.x
            inimigo.yy = inimigo.y
            inimigo.z = [0,1]
            inimigo.magic = 0

            inimigo.xspeed = 0
            inimigo.yspeed = 0

        if type == 3:
            inimigo = Animation("MdASprites/ENEMIES/Forest/Inimigo3.png",4,True)
            inimigo.set_total_duration(1000/3)

            inimigo.dano = 0
            inimigo.timer = 0
            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)
            inimigo.especie = "forest"
            inimigo.hp = 10
            inimigo.defesa = 0
            inimigo.type = type
            inimigo.spd = -400
            inimigo.yy = inimigo.y
            inimigo.z = 0

            inimigo.xspeed = 0
            inimigo.yspeed = 0

        if type == 4:
            inimigo = Animation("MdASprites/ENEMIES/Forest/Inimigo4.png",7,True)
            inimigo.set_total_duration(1000*7/24)

            inimigo.dano = 0
            inimigo.timer = 0
            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)
            inimigo.especie = "forest"
            inimigo.hp = 1
            inimigo.defesa = 0
            inimigo.type = type
            inimigo.spd = -400
            inimigo.yy = inimigo.y
            inimigo.z = 0
            inimigo.spawn = 0
            inimigo.minxspeed = random.randint(200,350)
            inimigo.minyspeed = random.randint(180,240)
            inimigo.chupa = 0

            inimigo.xspeed = 0
            inimigo.yspeed = 0
    
    if scene == 'magma':
        if type == 1:
            r = choose([1,1,1,2,2])
            inimigo = Animation(f"MdASprites/ENEMIES/Magma/Inimigo1-{r}.png",4,True)
            inimigo.set_total_duration(1000/2)

            inimigo.dano = r
            inimigo.r = r
            inimigo.form = 1
            inimigo.timer = 0
            inimigo.cooldown = random.randint(1,2)
            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)
            inimigo.especie = "magma"
            inimigo.hp = 4
            inimigo.defesa = 0
            inimigo.type = type
            inimigo.spd = (1+(r==1)/4)*280
            inimigo.spd2 = (1+(r==1)/6)*120

            inimigo.xspeed = 0
            inimigo.yspeed = 0

        if type == 3:
            inimigo = Animation("MdASprites/ENEMIES/Magma/Inimigo3.png",5,True)
            inimigo.set_total_duration(1000*5/6)

            inimigo.dano = 1
            inimigo.timer = 0
            inimigo.timer2 = 0
            inimigo.cooldown = random.randint(1,3)
            inimigo.x = screen.width
            inimigo.y = TOP_TELA + random.random()*(DOWN_TELA-TOP_TELA-inimigo.height)
            inimigo.especie = "magma"
            inimigo.hp = 3
            inimigo.defesa = 0
            inimigo.type = type
            inimigo.spd = SPD_BACKGROUND-60

            inimigo.xspeed = 0
            inimigo.yspeed = choose([1,-1])*60



    return inimigo

def seleciona_inimigos(inteiro):
    if inteiro < 30: return 1
    elif inteiro < 60: return 2
    elif inteiro < 90: return 3
    else: return 4

def Scr_inimigo(screen,room,inimigo,player,timer,projeteis,enemprojeteis):

    w = seleciona_inimigos(random.randint(0,100))

    if timer[0] >= 3*((16-(15-player[0].kills)*(player[0].kills<15))/(player[0].kills+1)):
        timer[0] = 0
        t = 1 + ((player[0].kills+1)%10==0)+(2*(player[0].kills%7==6))
        inimigo.append(criar_inimigo(screen,room,1,'magma'))

    for enem in inimigo:

        ###COMPORTAMENTO###

        if enem.type == 0:
            enem.x -= SPD_BACKGROUND*screen.delta_time()
            enem.y -= 360*screen.delta_time()

        if enem.especie == 'rock':
            if enem.type == 1:
                enem.yspeed = sign(player[0].y+player[0].height-enem.height - enem.y)*enem.spd if abs(player[0].y+player[0].height-enem.height - enem.y) > 3 else 0

                enem.x += enem.spd*-3*screen.delta_time()
                enem.y += enem.yspeed*screen.delta_time()*(enem.x>player[0].x)



                if enem.x<=-100:
                    inimigo.remove(enem)

            if enem.type == 2:
                enem.xspeed = -enem.spd
                if sqrt((enem.x-player[0].x)**2+(enem.y-player[0].y)**2)-enem.wait*50 >= enem.radio or (enem.x>=screen.width-100):
                    enem.wait = 0
                    enem.x += enem.xspeed*screen.delta_time()
                else:
                    enem.wait = 2
                    enem.timer -= screen.delta_time()
                    if enem.timer <= -2.5:
                        criar_enemprojeteis(enem,enemprojeteis,player[0])
                        enem.timer = 0

            if enem.type == 3:
                enem.x -= enem.spd*screen.delta_time()

                if enem.rocknroll == 0:
                    criar_enemprojeteis(enem,enemprojeteis,player)
                    enem.rocknroll = 1

            if enem.type == 4:
                enem.yspeed = sign(player[0].y+player[0].height-enem.height - enem.y)*enem.spd if abs(player[0].y+player[0].height-enem.height - enem.y) > 3 else 0
                enem.shake += screen.delta_time()
                enem.x += enem.spd*-1*screen.delta_time()
                enem.yy += enem.yspeed*screen.delta_time()*(enem.x>player[0].x)

                enem.y = enem.yy +15*sin(enem.shake*pi)

                if enem.x<=-100:
                    inimigo.remove(enem)

        if enem.especie == 'forest':
            if enem.type == 1:
                enem.timer += screen.delta_time()

                if enem.timer >= enem.cooldown:
                    enem.cooldown = random.randint(3,5)/2
                    enem.timer = 0
                    while enem.yy == enem.y:
                        enem.yy = TOP_TELA+random.randint(1,3)*(140)-enem.height
                    enem.jump = enem.yy-enem.y
                    enem.jumpforce = abs(enem.jump)/140*80

                if enem.y != enem.yy:
                    enem.z += sign(enem.yy-enem.z)*screen.delta_time()*240
                    z = (enem.yy-enem.z)/enem.jump
                    enem.y = enem.z - sin(pi*z)*enem.jumpforce
                    if abs(enem.z-enem.yy) <= 10: enem.y = enem.yy
                    enem.x -= 200*screen.delta_time()


                enem.curr_frame = (enem.y != enem.yy)

                enem.x -= (SPD_BACKGROUND)*screen.delta_time()

                if enem.x<=-100:
                    inimigo.remove(enem)

            if enem.type == 2:
                enem.timer += screen.delta_time()
                if enem.timer < enem.cooldown or enem.z[0] != 15:
                    enem.xx -= SPD_BACKGROUND*(enem.xx>1000)*screen.delta_time()
                    enem.z[0] += 30*enem.z[1]*screen.delta_time()
                    if enem.z[0]<=0: enem.z[1] = 1
                    if enem.z[0]>=30: enem.z[1] = -1

                    enem.curr_frame = enem.z[0]//10 if enem.z[0] < 30 else 2

                    enem.x = enem.xx + enem.z[0]*3
                    enem.y = enem.yy - 80*sin(pi*enem.z[0]/30)

                if enem.timer >= enem.cooldown:
                    if abs(enem.z[0]-15) <= 1:
                        enem.z[0] = 15

                        if enem.curr_frame < 3:
                            enem.curr_frame = 3
                            enem.play()

                        if enem.curr_frame == 5 and enem.magic == 0:
                            for i in range(3):
                                enem.p = i-(enem.yy==TOP_TELA+(440)-enem.height)+(enem.yy==TOP_TELA+(440/5)-enem.height)
                                criar_enemprojeteis(enem,enemprojeteis,player)
                            enem.magic = 1

                        if enem.timer > enem.cooldown + 2:
                            inimigo.remove(enem)
            
            if enem.type == 3:
                enem.x += enem.spd*screen.delta_time()
                enem.y = enem.yy - abs(sin(enem.z)*45)

                enem.z += screen.delta_time()*pi

                if enem.x <= player[0].x+player[0].width and abs((enem.yy+enem.height)-(player[0].y+player[0].height)) <= enem.height and enem.x >=player[0].width:
                    if enem.collided(player[0]):
                        player[0].x = enem.x - enem.width

            if enem.type == 4:
                if enem.spawn == 0:
                    for i in range(6):
                        a = (criar_inimigo(screen,room,4,'forest'))
                        a.curr_frame += random.randint(1,5)
                        a.x, a.y = a.x+random.randint(-20,20)+i*a.width,a.y+random.randint(-20,20)
                        a.yy = a.y
                        a.spawn = 1
                        inimigo.append(a)
                        
                    enem.spawn = 1

                
                enem.x += enem.xspeed*screen.delta_time()
                enem.y += enem.yspeed*screen.delta_time()

                enem.yspeed = min(abs(enem.yspeed),enem.minyspeed)*sign(enem.yspeed)
                enem.xspeed = min(abs(enem.xspeed),enem.minxspeed)*sign(enem.xspeed)

                enem.xspeed += sign(player[0].x+player[0].width-enem.width-enem.x)*3
                enem.yspeed += sign(player[0].y+player[0].height-enem.height-enem.y)

                
                if enem.collided(player[0]):
                        enem.chupa += screen.delta_time()

                        if enem.chupa >= 0.5:
                            enem.chupa = 0
                            if player[0].hp == player[0].hpcor:
                                player[0].hp-=1
        
        if enem.especie == 'magma':
            if enem.type == 1:
                enem.xspeed = -enem.spd
                enem.x += enem.xspeed*screen.delta_time()
                if enem.form == 1:
                    enem.yspeed = sign(player[0].y+player[0].height-enem.height - enem.y)*enem.spd2 if abs(player[0].y+player[0].height-enem.height - enem.y) > 3 else 0

                    enem.y += enem.yspeed*screen.delta_time()

                    enem.timer += screen.delta_time()

                    if enem.timer >= enem.cooldown:
                        p = Animation(f"MdASprites/ENEMIES/Magma/Inimigo1-{enem.r}projétil.png",2)
                        p.set_total_duration(1000/6)

                        p.hp = enem.hp
                        p.especie=enem.especie
                        p.defesa = enem.defesa

                        p.dano = enem.r
                        p.form = 2
                        p.x = enem.x
                        p.y = enem.y
                        p.type = enem.type

                        p.spd = enem.spd*2
                        p.yspeed = 0

                        inimigo.append(p)
                        inimigo.remove(enem)


            if enem.type == 3:
                enem.x += -enem.spd*screen.delta_time()
                enem.y += enem.yspeed*screen.delta_time()

                if enem.y+enem.height < TOP_TELA: enem.y = TOP_TELA
                if enem.y+enem.height > DOWN_TELA: enem.y = DOWN_TELA+enem.height

                enem.timer += screen.delta_time()
                enem.timer2 += screen.delta_time()

                
                if enem.timer2 >= 0.5:
                    enem.timer2 = 0
                    criar_enemprojeteis(enem,enemprojeteis,player)

                if enem.timer >= 2:
                    enem.yspeed *= -1
                    enem.timer = 0

                            
        ###FIM DO COMPORTAMENTO
                   

        def dano(enem,p,condicion="none"):
            if  p.dano-enem.defesa>0:
                enem.hp -= (p.dano-enem.defesa)*(1+(enem.especie==condicion))
            else:
                enem.hp -= min(1,p.dano)

        for p in projeteis:
            lança_chamas = 0
            if p.collided(enem):
                if p.name == "bala":    
                    projeteis.remove(p)
                    dano(enem,p)
                if p.name == "fogo" and lança_chamas == 0:
                        lança_chamas = 1 
                        dano(enem,p)
                if p.name == "flecha":
                    if p.launch == 1:
                        p.hp-=enem.hp
                        dano(enem,p)
                if p.name == "sword":    
                    if encontrar(p.acertados,enem) == 0:
                        dano(enem,p)
                        p.acertados.append(enem)
                if p.name == "picareta":    
                    if encontrar(p.acertados,enem) == 0:
                        dano(enem,p,"rock")
                        p.acertados.append(enem)
                if p.name == "machado":    
                    if encontrar(p.acertados,enem) == 0:
                        dano(enem,p,"forest")
                        p.acertados.append(enem)
                if p.name == "adaga":    
                    if encontrar(p.acertados,enem) == 0:
                        dano(enem,p)
                        p.acertados.append(enem)

        if enem.hp <= 0 and enem.type != 0:
                
                morto = criar_inimigo(screen,room,0)
                morto.x, morto.y = enem.x, enem.y

                inimigo.remove(enem)
                inimigo.append(morto)
                player[0].kills_type[enem.type-1]+=1
        
        if enem.y <= -100:
            inimigo.remove(enem)

        if enem.collided(player[0]) and enem.type != 0 and player[0].hpcor == player[0].hp:
            player[0].hp -= enem.dano

            
    Scr_enemprojeteis(enemprojeteis,player[0],screen,inimigo) 

    for enem in inimigo:

        enem.update()


def criar_enemprojeteis(enem,enemprojeteis,player):
    if enem.especie == 'rock':
        if enem.type == 2:
            p = Animation("MdASprites/ENEMIES/Rock/Inimigo2projétil.png",4)
            p.set_total_duration(1000)

            p.dano = 1
            p.porcima = 1
            p.x = enem.x+enem.width/2
            p.y = enem.y+enem.height/2
            p.type = enem.type

            x = player.x+player.width/2
            y = player.y+player.height/2

            dx = p.x - x
            dy = p.y - y

            dist = sqrt(dx**2+dy**2)

            dx/=-dist
            dy/=-dist

            p.xspeed = 450*dx
            p.yspeed = 450*dy

            enemprojeteis.append(p)

        if enem.type == 3:
            p = Animation("MdASprites/ENEMIES/Rock/Inimigo3projétil.png",12)
            p.set_total_duration(1000)

            p.dano = 2
            p.porcima = 1
            p.type = enem.type
            p.x = enem.x+enem.width/2-p.width/2
            p.y = enem.y+enem.height/2 - p.height/2

            p.enem = enem

            p.xspeed = -enem.spd
            p.yspeed = 0
            

            enemprojeteis.append(p)

    if enem.especie == 'forest':
        if enem.type == 2:
            p = Animation("MdASprites/ENEMIES/Forest/Inimigo2projétil.png",8,True)
            p.set_total_duration(1000*2/3)

            p.dano = 1
            p.porcima = 1
            p.x = enem.x+enem.width/2
            p.y = enem.y+enem.height/4
            p.type = 6

            p.xspeed = -350
            if enem.p == -1: p.yspeed = -160
            if enem.p == 0: p.yspeed = -80
            if enem.p == 1: p.yspeed = 0
            if enem.p == 2: p.yspeed = 80
            if enem.p == 3: p.yspeed = 160

            enemprojeteis.append(p)

    if enem.especie == 'magma':

        if enem.type == 3:
            p = Animation("MdASprites/ENEMIES/Magma/Inimigo3projétil.png",4)
            p.set_total_duration(1000*4/6)

            p.dano = 1
            p.timer = 0
            p.porcima = 0
            p.x = enem.x
            p.y = enem.y+enem.height-p.height
            p.type = enem.type+8

            p.xspeed = -SPD_BACKGROUND
            p.yspeed = 0

            enemprojeteis.append(p)


def Scr_enemprojeteis(enemprojeteis,player,screen,enemmatriz):

    for p in enemprojeteis:
        p.x+=p.xspeed*screen.delta_time()
        p.y+=p.yspeed*screen.delta_time()
        if player.hp == player.hpcor:
            if p.collided(player):
                player.hp -= p.dano
                if p.type != 3: enemprojeteis.remove(p)

        if p.type == 3:
            if encontrar(enemmatriz,p.enem) == 0:
                enemprojeteis.remove(p)

            else:
                p.x = p.enem.x+p.enem.width/2 - p.width/2
        
        if p.type == 11:
            p.timer += screen.delta_time()
            if p.timer > 2.5:
                enemprojeteis.remove(p)

        if p.x < -p.width*3:
            enemprojeteis.remove(p)
            


    for p in enemprojeteis:

        p.update()