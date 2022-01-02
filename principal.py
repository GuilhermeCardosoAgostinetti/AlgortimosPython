import pygame
from pygame import draw
from pygame.locals import *


#Tamanho TELA

LARGURA = 1000
ALTURA = 700

#Cores

BRANCO = (255,255,255)
PRETO = (0,0,0)
AZUL = (0,39,118)
AMARELO = (255,253,0)
VERDE = (0,156,59)

pygame.init()
pygame.mixer.music.load('hino.mp3')
pygame.mixer.music.play(-1)

def desenhar():

    pygame.draw.polygon(tela, AMARELO,((85, ALTURA/2), (LARGURA/2, 85), (LARGURA-85, ALTURA/2), (LARGURA/2, ALTURA-85)))
    pygame,draw.circle(tela, AZUL,(LARGURA/2, ALTURA/2), 175)




tela = pygame.display.set_mode((LARGURA, ALTURA))

while True:
    tela.fill(VERDE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        desenhar()


        pygame.display.update()