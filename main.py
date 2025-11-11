import pygame
from PPlay import *

# funções do jogo
def menu_principalf():
    menu = True
    while menu:
        ### DESENHOS
        # Fundo
        fundo = pygame.image.load('anexos/img/37412.jpg')
        screen.blit(fundo, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_ENTER]:
            menu = False
            jogof()

        # Update da cena
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

def jogof():        
    jogo = True
    while jogo:
        ### DESENHOS
        # Fundo
        screen.fill((255, 255, 255))

        # Update da cena
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False

# Inicialização do PyGame
pygame.init()

# Variáveis definindo as dimensões da tela
screen_width = 900
screen_heigth = 600

# Criação da tela e preenchimento com uma cor
screen = pygame.display.set_mode((screen_width, screen_heigth))
screen.fill((0,0,0))


# Início do game
menu_principalf()

# Encerra o PyGame
pygame.quit()