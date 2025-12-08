from MdAplayer import *
from MdAInimigo import *
from MdADraw import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

def pedaços(morto,screen):
    
    for i in morto:
        i.x+=i.xspeed*screen.delta_time()
        i.y+=i.yspeed*screen.delta_time()

        i.yspeed += 500*screen.delta_time()

        i.draw()

        if i.y>screen.height:
            morto.remove(i) 
        

    
def criar_pedaços(enem,morto):
    for i in range(4):
        m = Animation(f"MdASprites/ENEMIES/InimigoPedaços{enem.especie}{enem.type}.png",4,False)
        m.stop()
        m.curr_frame = i
        m.update()

        m.x = enem.x+enem.width/2-m.width/2
        m.y = enem.y+enem.height/2-m.height/2

        if i == 0:
            m.xspeed = -200
            m.yspeed = -200

        if i == 1:
            m.xspeed = -200
            m.yspeed = -100

        if i == 2:
            m.xspeed = 200
            m.yspeed = -200

        if i == 3:
            m.xspeed = 200
            m.yspeed = -100

        morto.append(m)

def criar_pedaços_chão(enem,morto):
    for i in range(4):
        m = Animation(f"MdASprites/Background/Pedaços{enem.name}.png",4,False)
        m.stop()
        m.curr_frame = i
        m.update()

        m.x = enem.x+enem.width/2-m.width/2
        m.y = enem.y+enem.height-m.height

        if i == 0:
            m.xspeed = -200
            m.yspeed = -200

        if i == 1:
            m.xspeed = -200
            m.yspeed = -100

        if i == 2:
            m.xspeed = 200
            m.yspeed = -200

        if i == 3:
            m.xspeed = 200
            m.yspeed = -100

        morto.append(m)