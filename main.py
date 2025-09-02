import pygame

# Inicialização do PyGame
pygame.init()

# Variáveis definindo as dimensões da tela
screen_width = 900
screen_heigth = 600

# Criação da tela e preenchimento com uma cor
screen = pygame.display.set_mode((screen_width, screen_heigth))
screen.fill((0,0,0))

# Definição da posição da bola [posição x, posição y, raio]
bola_pos = [screen_width/2, screen_heigth/2, 15]
# Definição da velocidade da bola [velocidade x, velocidade y]
bola_speed = [1, 1]

# Criação das barras do jogador 1 e 2 [posição x, posição y, tamanho x, tamanho y]
barra1 = [100, screen_heigth/2, 10, 100]
barra2 = [screen_width - 100, screen_heigth/2, 10, 100]
# velocidade das barras
vel = 1

# Início do looping
running = True
while running:
    ### DESENHOS
    # Fundo
    screen.fill((0, 0, 0))

    # Bola
    pygame.draw.circle(screen,(255,255,255), [bola_pos[0], bola_pos[1]], bola_pos[2])

    # Atualização da posição da bolinha
    bola_pos[0] += bola_speed[0] * 1
    bola_pos[1] += bola_speed[1] * 1

    # Players
    pygame.draw.rect(screen,(255,255,255),[barra1[0], barra1[1], barra1[2], barra1[3]], 0)
    pygame.draw.rect(screen,(255,255,255),[barra2[0], barra2[1], barra2[2], barra2[3]], 0)

    # Atualização das barras
    # Barra 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and barra1[1] > 0:
        barra1[1] -= vel

    if keys[pygame.K_s] and barra1[1] < screen_heigth - barra1[3]:
        barra1[1] += vel

    # Barra 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and barra2[1] > 0:
        barra2[1] -= vel

    if keys[pygame.K_DOWN] and barra2[1] < screen_heigth - barra2[3]:
        barra2[1] += vel


    ### Colisões
    # Bola-parede
    if (15 < bola_pos[0] < screen_width - 15) == False:
        bola_speed[0] *= -1
    if (15 < bola_pos[1] < screen_heigth - 15) == False:
        bola_speed[1] *= -1

    # Bola-Barra
    if (barra1[0] < bola_pos[0] < barra1[0] + barra1[2] and barra1[1] < bola_pos[1] < barra1[1] + barra1[3]):
        bola_speed[0] *= -1
    if (barra2[0] < bola_pos[0] < barra2[0] + barra2[2] and barra2[1] < bola_pos[1] < barra2[1] + barra2[3]):
        bola_speed[0] *= -1


    # Update da cena
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Encerra o PyGame
pygame.quit()