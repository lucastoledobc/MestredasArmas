from PPlay.window import *
from PPlay.sprite import *
import pygame
import datetime


# função pra tela de salvamento do ranking
def frank(score):
    # variáveis
    screen = Window(1280,720)
    cor0 = (0,0,0)
    cor1 = (255,255,255)
    loop_rank = False
    teclado = screen.get_keyboard()

    # título
    newrec = Sprite("MdASprites/Menu/newrec.png")
    newrec.set_position(int(newrec.width/2)-newrec.width/2, 50)

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
    
    # agora verifica se o jogador fez mais pontos que o último colocado
    if score > scores[4]["score"]:
        loop_rank=True        
        nome=''
        write_time = 0

        while loop_rank:
            # desenho do fundo, título e botões
            screen.set_background_color(cor0)
            newrec.draw()        
            screen.draw_text("Digite seu nome e aperte enter para salvar:",(screen.width)*1/4, 150, 30, cor1)

            # Escreve na tela o que a pessoa digita
            screen.draw_text("Nome: "+nome, (screen.width)*1/4, screen.height/2, 30, cor1)
            # um tempo para evitar escrita repetida
            write_time += screen.delta_time()
            if write_time > 0.15:
                # Verifica se ela escreve algo entre A e Z
                # pega o valor da tecla pressionada no pygame
                # converte esse valor em ascii e depois em char
                # se não conseguir, x=0
                try:
                    x = int(pygame.key.get_pressed().index(True))   
                    if x > 3 and x < 30 and len(nome)<11:   
                        nome += chr(x+61)
                        write_time=0
                except:
                    x=0

                # se apertar backspace, apaga um char
                if pygame.key.get_pressed()[8] and len(nome)>0:
                    nome=nome[:-1]
                    write_time=0

            # se apertar enter, adiciona novo jogador a lista
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                # pega a data atual e coloca numa string no forma DD/MM/YY
                x = datetime.datetime.now()
                date = str(x.day)+"/"+str(x.month)+"/"+str(x.year)[2:]

                # cria uma biblioteca com nome, score e data e adiciona ao array de scores
                score_novo = {"nome": nome, "score": int(score), "data": str(date)}
                scores.append(score_novo)

                # ordena
                scores = sorted(scores, key=lambda d: d['score'], reverse=True)

                # deleta o 6º item
                if len(scores)==6:
                    del scores[5]
                
                # apaga o conteúdo do arquivo de escores
                with open("scores.txt", "w") as f:
                    f.write("")

                # escreve o novo score de cada um nele
                for i in range(5):
                    with open("scores.txt", "a") as f:
                        texto=" "+str(scores[i]['nome'])+" "+str(scores[i]['score'])+" "+str(scores[i]['data'])
                        f.write(texto)
                
                # vai para tela de ranking
                frank(scores)
            

            screen.update()
            # condição apra voltar ao menu principal
            if teclado.key_pressed('esc'):
                return
    return


def menu_rank():
    # variáveis
    screen = Window(1280,720)
    tam = 30
    cor0 = (0,0,0)
    cor1 = (255,255,255)
    teclado = screen.get_keyboard()

    # título
    rank_title = Sprite("MdASprites/Menu/ranking.png")
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
            screen.draw_text("Nome:", (screen.width)*1/10, (screen.height)*1/4, tam, cor1)
            screen.draw_text("Pontos:", (screen.width)*4/6, (screen.height)*1/4, tam, cor1)
            screen.draw_text(str(i+1)+"º lugar: "+str(scores[i]['nome']), (screen.width)*1/10, (screen.height)*2/5+i*3/2*tam, tam, cor1)
            screen.draw_text(str(scores[i]['score']), (screen.width)*4/6, (screen.height)*2/5+i*3/2*tam, tam, cor1)
            
        screen.update()
        # condição apra voltar ao menu principal
        if teclado.key_pressed('esc'):
            return

def running_menu(room):
    # variáveis
    screen = Window(1280,720)
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
        for i in range(0, 15, 3):
            score={}
            score['nome']=scores2[i]
            score['score']=int(scores2[i+1])
            score['data']=scores2[i+2]
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

        # reseta a array atual
        scores=[]
        # lê os escores do arquivo
        with open("scores.txt") as f:
            scores2=f.read().split()

        # escreve na forma de biblioteca
        for i in range(0, 10, 2):
            score={}
            score['nome']=scores2[i]
            score['score']=int(scores2[i+1])
            scores.append(score)


    # título e botões
    titulo = Sprite("MdASprites/Menu/titulo.png")
    titulo.set_position(int(screen.width/2)-titulo.width/2, 50)

    bjoga = Sprite("MdASprites/Menu/bjoga.png")
    bjoga.set_position(int(screen.width/2)-bjoga.width/2, screen.height/2)
    brank = Sprite("MdASprites/Menu/brank.png")
    brank.set_position(int(screen.width/2)-brank.width/2, bjoga.y + brank.height*5/2)
    bsair = Sprite("MdASprites/Menu/bsair.png")
    bsair.set_position(int(screen.width/2)-bsair.width/2, brank.y + bsair.height*5/2)

    while room[0]=='Menu':
        screen.set_background_color([0, 0, 0])
        titulo.draw()
        bjoga.draw()
        brank.draw()
        bsair.draw()

        if mouse.is_button_pressed(1) and mouse.is_over_object(bjoga):
            room[0] = "Jogo"

        if mouse.is_button_pressed(1) and mouse.is_over_object(brank):
            menu_rank()

        screen.update() 