import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
import random

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1

room = Window(1280,720)
room.set_title("ROOM! Chambres")

#Ferramenta para mudar o fps do jogo
clock = pygame.time.Clock()
FPS = 60

moedas = 0

player = Sprite("Cat00.png",1)

#transforma o sprite coins em uma animação de 4 frames
objetivo = Animation("coins.png",4)
#set_sequence_time Usa o frame inicial da animação, o final, o tempo de duração total da animação (que é dividido pelo FPS do game) e se ela se repete
objetivo.set_sequence_time(0,3,120,True)

player.x, player.y = [room.width/2,-player.height]

objetivo.x, objetivo.y = random.randint(0,room.width),random.randint(400,room.height-100)

yspeed = 0

running = True

while running:

    room.set_background_color([0, 0, 0])

    #Desenha a moeda. O update é necessário para que ele entenda que deve mudar o frame atual da animação a ser desenhado
    objetivo.draw()
    objetivo.update()

    #Desenha o player
    player.draw()

    #teclas para a movimentação do player

    direita =  keyboard.Keyboard().key_pressed('d')
    esquerda =  keyboard.Keyboard().key_pressed('a')
    jump =  keyboard.Keyboard().key_pressed('space')


    if  keyboard.Keyboard().key_pressed('escape'):
        room.close() #fecha o jogo

    #velocidades horizontal e vertical do player

    xspeed = (direita-esquerda)*6
    yspeed += 0.3

    if player.y + yspeed >= room.height - 100:
        player.y = room.height - 100
        yspeed = 0
        if jump:
            yspeed -= 15

    #colisão da moeda com o player

    if player.collided(objetivo):
        objetivo.x, objetivo.y = random.randint(0,room.width),random.randint(400,room.height-100)
        moedas+=1;
        
    
    #contador de moedas na tela
    room.draw_text("Moedas: "+str(moedas), 100, 100, size=15, color=(255, 255, 255), bold=True)

    clock.tick(FPS) #modifica a taxa de quadros por segundo da janela

    #velocidades do jogador atualizando sua posição no cenário 

    player.x += xspeed
    player.y += yspeed    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    room.update()