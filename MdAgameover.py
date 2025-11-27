from PPlay.window import *
from PPlay.keyboard import *
from MdAMenu import *
import pygame


def running_game_over(screen, room):
    # variáveis
    cor0 = (0,0,0)
    cor1 = (255,255,255)
    loop_rank = False
    teclado = screen.get_keyboard()
    tempo_over = 0

    # título
    newrec = Sprite("MdASprites/Menu/newrec.png")
    newrec.set_position(int(screen.width/2)-newrec.width/2, 50)
    over = Sprite("MdASprites/Menu/over.png")
    over.set_position(int(screen.width/2)-over.width/2, int(screen.height/2-over.height/2))

    over.draw()
    while tempo_over < 2:
        tempo_over += screen.delta_time()
        screen.update()

    # cria uma array para receber os scores
    scores=[]
    # lê os dados do arquivo e separa em uma array
    with open("scores.txt") as f:
        scores2=f.read().split()

    # escreve na forma de biblioteca
    for i in range(0, 10, 2):
        player={}
        player['nome']=scores2[i]
        player['score']=int(scores2[i+1])
        scores.append(player)    
    
    # agora verifica se o jogador fez mais pontos que o último colocado
    if room[1] > scores[4]["score"]:
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
            # cria uma biblioteca com nome, score e data e adiciona ao array de scores
            score_novo = {"nome": nome, "score": int(room[1])}
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
                    texto=" "+str(scores[i]['nome'])+" "+str(scores[i]['score'])
                    f.write(texto)
            
            # vai para tela de ranking
            menu_rank()
        

        screen.update()
        # condição apra voltar ao menu principal
        if teclado.key_pressed('esc'):
            loop_rank = False
            room[0] = "Menu"

    room[0] = "Menu"