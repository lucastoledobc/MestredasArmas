from PPlay.gameimage import *

def draw_cena(player,cenario,inimigos,projeteis,enemprojeteis,screen):
    draw = []

    for c in cenario: 
        if c.name != "floor": draw.append(c)
    for c in inimigos: draw.append(c)
    draw.append(player[0])

    if 1==1:
        for i in range(len(draw)):
            for j in range(len(draw)-1):
                if draw[j].y + draw[j].height > draw[j+1].y + draw[j+1].height:
                    draw[j], draw[j+1] = draw[j+1], draw[j]

    for c in enemprojeteis: 
        if c.porcima == 1: draw.append(c)
        else: draw.insert(0, c)
    for c in projeteis: draw.append(c)

    for c in inimigos: 
        if c.type==0: draw.append(c)

    for c in draw:
        if c == player[0]:
            if player[0].hp == player[0].hpcor:
                player[2].draw()
                player[0].draw()
                player[1].draw()
            
            else:
                if player[0].hp + 1 <= player[0].hpcor: player[0].hpcor = player[0].hp + 1
                player[0].hpcor -= 0.5*screen.delta_time()
                if player[0].hpcor*100%8<3:
                        for p in player:
                            player[2].draw()
                            player[0].draw()
                            player[1].draw()

                if player[0].hpcor <= player[0].hp: 
                    player[0].hpcor = player[0].hp

        else: 
            c.draw()

def draw_cena_novo(player,cenario,inimigos,projeteis,enemprojeteis,screen):
    
    for c in cenario: 
        if c.name != "floor" and c.y+c.height < player[0].y+player[0].height: c.draw()

    for c in enemprojeteis: 
        if c.porcima == 0: c.draw()
    for c in inimigos: 
        if c.type != 0 and c.y+c.height < player[0].y+player[0].height: c.draw()

    if player[0].hp == player[0].hpcor:
        for p in player:
            p.draw()
    
    else:
        if player[0].hp + 1 <= player[0].hpcor: player[0].hpcor = player[0].hp + 1
        player[0].hpcor -= 0.5*screen.delta_time()
        if player[0].hpcor*100%8<3:
                for p in player:
                    p.draw()

        if player[0].hpcor <= player[0].hp: 
            player[0].hpcor = player[0].hp

    for c in inimigos: 
        if c.type != 0 and c.y+c.height >= player[0].y+player[0].height: c.draw()

    for c in cenario: 
        if c.name != "floor" and c.y+c.height >= player[0].y+player[0].height: c.draw()

    for c in projeteis: c.draw()
    for c in enemprojeteis: 
        if c.porcima == 1: c.draw()

    for c in inimigos: 
        if c.type == 0: c.draw()
