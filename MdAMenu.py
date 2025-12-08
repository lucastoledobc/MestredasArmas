from PPlay.window import *
from PPlay.sprite import *
import random

def menu_rank(screen):
    # variáveis
    tam = 30
    cor0 = (0,0,0)
    cor1 = (255,255,255)
    teclado = screen.get_keyboard()

    # título
    rank_title = Sprite("MdASprites/Menu/title_rank.png")
    rank_title.set_position(int(screen.width/2)-rank_title.width/2, 30)

    # cria uma array para receber os scores
    scores=[]
    # lê os dados do arquivo e separa em uma array
    with open("scores.txt") as f:
        scores2=f.read().split()

    # escreve na forma de biblioteca
    for i in range(0, 10, 2):
        score={}
        score['nome']=scores2[i]
        score['score']=int(scores2[i+1])
        scores.append(score)

    # inicia o loop
    rank_loop = True
    while rank_loop:
        # desenha do fundo e título
        screen.set_background_color(cor0)
        rank_title.draw() 

        for i in range(len(scores)):
            screen.draw_text("Nome:", (screen.width)*1/10, (screen.height)*1/3, tam, cor1)
            screen.draw_text("Pontos:", (screen.width)*8/10, (screen.height)*1/3, tam, cor1)
            screen.draw_text(str(i+1)+"º lugar: "+str(scores[i]['nome']), (screen.width)*1/10, (screen.height)*2/5+i*3/2*tam, tam, cor1)
            screen.draw_text(str(scores[i]['score']), (screen.width)*8/10, (screen.height)*2/5+i*3/2*tam, tam, cor1)
            
        screen.update()
        # condição apra voltar ao menu principal
        if teclado.key_pressed('esc'):
            return

def running_menu(screen, room):
    # variáveis
    mouse = screen.get_mouse()


    ### lista das pontuações
    # primeiro, tenta ver se o arquivo txt ja existe:
    try:
        # cria uma array para receber os scores
        scores=[]
        # lê os dados do arquivo e separa em uma array
        with open("scores.txt") as f:
            scores2=f.read().split()

        # escreve na forma de biblioteca
        for i in range(0, 10, 2):
            score={}
            score['nome']=scores2[i]
            score['score']=int(scores2[i+1])
            scores.append(score)

    # caso contrario, cria uma nova
    except:
        scores = [
            {"nome": "MASTER", "score": 100},
            {"nome": "PACOCA", "score": 1000},
            {"nome": "MESTRE", "score": 10000},
            {"nome": "SPEDDY", "score": 100000},
            {"nome": "NOOB", "score": 1000000}
        ]
        scores = sorted(scores, key=lambda d: d['score'], reverse=True)

        # cria um arquivo em branco caso não exista ou apaga ele totalmente
        with open("scores.txt", "w") as f:
            f.write("")

        # escreve o score de cada um no arquivo
        for i in range(5):
            with open("scores.txt", "a") as f:
                texto=" "+str(scores[i]['nome'])+" "+str(scores[i]['score'])
                f.write(texto)


    # título e botões
    fundo = Sprite("MdASprites/Menu/fundo.png")
    fundo.set_position(0, 0)
    titulo = Sprite("MdASprites/Menu/title_main.png")
    titulo.set_position(int(screen.width/2)-titulo.width/2, 130)

    bjoga = Sprite("MdASprites/Menu/bjoga.png")
    bjoga.set_position(int(screen.width/2)-bjoga.width/2, screen.height/2+30)
    brank = Sprite("MdASprites/Menu/brank.png")
    brank.set_position(int(screen.width/2)-brank.width/2, bjoga.y + brank.height*3/2)
    bsair = Sprite("MdASprites/Menu/bsair.png")
    bsair.set_position(int(screen.width/2)-bsair.width/2, brank.y + bsair.height*3/2)

    # armas    
    time_arma = 2
    arma1 = []
    arma2 = []

    while room[0]=='Menu':
        screen.set_background_color([0, 0, 0])
        fundo.draw()
        titulo.draw()
        bjoga.draw()
        brank.draw()
        bsair.draw()

        # espada.draw()

        if mouse.is_button_pressed(1) and mouse.is_over_object(bjoga):
            room[0] = "Jogo"
            room[1] = False
            room[2] = 0

        if mouse.is_button_pressed(1) and mouse.is_over_object(brank):
            menu_rank(screen)

        if mouse.is_over_object(bsair) and mouse.is_button_pressed(1):
            screen.close()
            # fecha a janela

        #armas 

        time_arma += screen.delta_time()
        if time_arma > 2:
            a=random.randint(1,12)
            item = Sprite("MdASprites/Menu/armas/"+str(a)+".png")
            item.set_position(1300, 45)
            arma1.append(item)
            a=random.randint(1,12)
            item = Sprite("MdASprites/Menu/armas/"+str(a)+".png")
            item.set_position(-30, 645)
            arma2.append(item)
            time_arma = 0

        for item1 in arma1:
            item1.x -= 0.3
            item1.draw()

        for item2 in arma2:
            item2.x += 0.3
            item2.draw()


        for item1 in arma1:
            if item1.x < -30:
                del item1

        for item2 in arma2:
            if item2.x > 1300:
                del item2

        screen.update()


def running_arma(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira, fase):
    # título e botões
    title_armas = Sprite("MdASprites/Menu/title_armas.png")
    title_armas.set_position(int(screen.width)/2-title_armas.width/2, 20)
    bjoga = Sprite("MdASprites/Menu/bjoga.png")
    bjoga.set_position(int(screen.width)-bjoga.width-40, screen.height-bjoga.height-30)
    bfases = Sprite("MdASprites/Menu/fases.png")
    bfases.set_position(40, 550)

    armas = [
        'adaga',
        'arco',
        'machado',
        'picareta',
        'sword',
        'gun',
        'metralhadora',
        'lança-chamas',
        'rocket-launcher',
        'punch2'
    ]
    armas_s = []

    for i in range (len(armas)):
        x = Sprite("MdASprites/Armas/"+str(armas[i])+".png")
        armas_s.append(x)


    slots = []
    slots_e = []
    slots_n = 0
    time_click = 0

    for i in range(2):
        item = Sprite("MdASprites/Menu/slot0.png")
        item.set_position(int(screen.width)/2-item.width*5/4+item.width*3/2*i, 200)
        slots.append(item)
        slots_e.append(0)

    for i in range(len(armas)):
        item = Sprite("MdASprites/Menu/slot0.png")
        item.set_position(int(screen.width)/2-(item.width*((len(armas)-1)*3/2)+item.width)/2+item.width*3/2*i, 350)
        slots.append(item)
        slots_e.append(0)

        armas_s[i].set_position(item.x+item.width/2-armas_s[i].width/2, item.y+item.height/2-armas_s[i].height/2)
    
    armas_escolhidas = ['','', Sprite, Sprite]
    

    # fases

    fases = ['rock',
            'forest',
            'magma'
            ]
    
    fases_print = [Sprite("MdASprites/Menu/rock.png"),
                   Sprite("MdASprites/Menu/forest.png"),
                   Sprite("MdASprites/Menu/magma.png")
                   ]
    
    fases_m = []
    fases_e = 0


    for i in range(len(fases)):
        item = Sprite("MdASprites/Menu/slot10.png")
        item.set_position(int(screen.width)/2-(item.width*((len(fases)-1)*3/2)+item.width)/2+item.width*3/2*i, 520)
        fases_print[i].set_position(item.x+item.width/2-fases_print[i].width/2, item.y+item.height/2-fases_print[i].height/2)
        fases_m.append(item)


    while room[1] == False:
        screen.set_background_color([0, 0, 0])

        title_armas.draw()
        bjoga.draw()
        bfases.draw()

        for item in slots:
            item.draw()
        
        time_click += screen.delta_time()
        for i in range(2, len(slots)):
            if mouse.is_over_object(slots[i]):
                if slots_e[i]==0:
                    x = slots[i].x
                    y = slots[i].y
                    slots[i] = Sprite("MdASprites/Menu/slot1.png")
                    slots[i].set_position(x, y)
                    slots_e[i]=1

                if mouse.is_button_pressed(1) and slots_e[i]==1 and slots_n < 2 and time_click > 0.3:
                    x = slots[i].x
                    y = slots[i].y
                    slots[i] = Sprite("MdASprites/Menu/slot2.png")
                    slots[i].set_position(x, y)
                    slots_e[i]=2

                    for i2 in range(2):
                        if armas_escolhidas[i2+2] == Sprite:
                            x = slots[i2].x
                            y = slots[i2].y
                            slots[i2] = Sprite("MdASprites/Menu/slot2.png")
                            slots[i2].set_position(x, y)

                            armas_escolhidas[i2] = armas[i-2]
                            z = Sprite("MdASprites/Armas/"+str(armas_escolhidas[i2])+".png")
                            z.set_position(x+slots[i2].width/2-z.width/2, y+slots[i2].height/2-z.height/2)
                            armas_escolhidas[i2+2] = z

                            break

                    slots_n +=1
                    time_click = 0

                if mouse.is_button_pressed(1) and slots_e[i]==2 and time_click > 0.3:
                    x = slots[i].x
                    y = slots[i].y
                    slots[i] = Sprite("MdASprites/Menu/slot1.png")
                    slots[i].set_position(x, y)
                    slots_e[i]=1

                    slots_n -=1
                    
                    for i2 in range(2):
                        if armas_escolhidas[i2] == armas[i-2]:
                            armas_escolhidas[i2] = ''
                            armas_escolhidas[i2+2] = Sprite

                            x = slots[i2].x
                            y = slots[i2].y
                            slots[i2] = Sprite("MdASprites/Menu/slot0.png")
                            slots[i2].set_position(x, y)
                        

                    time_click = 0

            else:
                if slots_e[i]==1:
                    x = slots[i].x
                    y = slots[i].y
                    slots[i] = Sprite("MdASprites/Menu/slot0.png")
                    slots[i].set_position(x, y)
                    slots_e[i]=0


        for arma in armas_s:
            arma.draw()

        try:
            armas_escolhidas[2].draw()
        except:
            x=1
        try:            
            armas_escolhidas[3].draw()
        except:
            x=1


        for i in range(len(fases)):
            if mouse.is_over_object(fases_m[i]):
                if mouse.is_button_pressed(1) and time_click > 0.3:
                    item = Sprite("MdASprites/Menu/slot12.png")
                    item.set_position(int(screen.width)/2-(item.width*((len(fases)-1)*3/2)+item.width)/2+item.width*3/2*i, 520)
                    fases_m[i] = item
                    fases_e = i
                    time_click = 0

                elif i != fases_e:
                    item = Sprite("MdASprites/Menu/slot11.png")
                    item.set_position(int(screen.width)/2-(item.width*((len(fases)-1)*3/2)+item.width)/2+item.width*3/2*i, 520)
                    fases_m[i] = item

            else:
                if i != fases_e and fases_m[i] != Sprite("MdASprites/Menu/slot10.png"):
                    item = Sprite("MdASprites/Menu/slot10.png")
                    item.set_position(int(screen.width)/2-(item.width*((len(fases)-1)*3/2)+item.width)/2+item.width*3/2*i, 520)
                    fases_m[i] = item
        
            fases_print[i].draw()
            fases_m[i].draw()


        if mouse.is_button_pressed(1) and mouse.is_over_object(bjoga):
            room[1] = True
            
            if armas_escolhidas[0] == '':
                armas_escolhidas[0] = 'sword'
            if armas_escolhidas[1] == '':
                armas_escolhidas[1] = 'gun'

            if armas_escolhidas[0] == 'punch2':
                armas_escolhidas[0] = 'punch1'

            player[1] = Animation("MdASprites/Armas/"+str(armas_escolhidas[0])+".png",1,False)
            player[1].hand = 1
            player[2] = Animation("MdASprites/Armas/"+str(armas_escolhidas[1])+".png",1,False)
            player[2].hand = 2


            for i in range(2):
                if armas_escolhidas[i] == 'adaga':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 0
                    player[i+1].cooldown = 0.3+1
                if armas_escolhidas[i] == 'arco':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 1
                    player[i+1].cooldown = 0.3
                if armas_escolhidas[i] == 'gun':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 6
                    player[i+1].cooldown = 0.3
                if armas_escolhidas[i] == 'lança-chamas':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 100
                    player[i+1].cooldown = 0.3
                if armas_escolhidas[i] == 'machado':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 10
                    player[i+1].cooldown = 0.3
                if armas_escolhidas[i] == 'metralhadora':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 20
                    player[i+1].cooldown = 0.3
                if armas_escolhidas[i] == 'picareta':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 0
                    player[i+1].cooldown = 0.3
                if armas_escolhidas[i] == 'punch1':
                    player[i+1].name = 'punch'
                    player[i+1].munition = 0
                    player[i+1].cooldown = 1
                if armas_escolhidas[i] == 'punch2':
                    player[i+1].name = 'punch'
                    player[i+1].munition = 0
                    player[i+1].cooldown = 1
                if armas_escolhidas[i] == 'sword':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 0
                    player[i+1].cooldown = 0
                if armas_escolhidas[i] == 'rocket-launcher':
                    player[i+1].name = armas_escolhidas[i]
                    player[i+1].munition = 0
                    player[i+1].cooldown = 10

        fase[0] = fases[fases_e]

        screen.update()