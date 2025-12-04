from PPlay.window import *
from PPlay.sprite import *


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

        if mouse.is_over_object(bsair) and mouse.is_button_pressed(1):
            screen.close()
            # fecha a janela

        screen.update()


def running_arma(screen, room, player, inimigo, timer, mouse, projetil, background, enemprojeteis, mira):
    # título e botões
    bjoga = Sprite("MdASprites/Menu/bjoga.png")
    bjoga.set_position(int(screen.width)-bjoga.width-40, screen.height-bjoga.height-40)

    while room[1] == False:
        screen.set_background_color([0, 0, 0])
        screen.draw_text("Seleção de armas:", 20, 20, 50, (255,255,255))

        bjoga.draw()

        if mouse.is_button_pressed(1) and mouse.is_over_object(bjoga):
            room[1] = True
            
        screen.update()